import hashlib
import subprocess
import os
import re 
from flask import Flask, request

app = Flask(__name__)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    
    if not re.match(r"^[a-zA-Z0-9.-]+$", host):
        return "Invalid host", 400

    try:
        result = subprocess.check_output(["/usr/bin/ping", "-c", "1", host], shell=False) # nosec
        return result
    except Exception as e:
        return str(e), 400

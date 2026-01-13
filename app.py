import hashlib
import subprocess
import os
import re # Ajouté pour la validation
from flask import Flask, request

app = Flask(__name__)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    
    # SECURITÉ SUPPLÉMENTAIRE : On n'autorise que les caractères de type IP ou domaine
    if not re.match(r"^[a-zA-Z0-9.-]+$", host):
        return "Invalid host", 400

    try:
        # B607: Chemin complet /usr/bin/ping (standard Linux)
        # B603: # nosec pour dire à Bandit que l'input est validé par le Regex ci-dessus
        result = subprocess.check_output(["/usr/bin/ping", "-c", "1", host], shell=False) # nosec
        return result
    except Exception as e:
        return str(e), 400

# ... reste du code (debug=False)
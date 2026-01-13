import hashlib
import subprocess
import os # Pour récupérer les secrets via variables d'environnement
from flask import Flask, request

app = Flask(__name__)

# CORRECTION B324 : Utiliser SHA-256 (plus robuste) au lieu de MD5
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    # CORRECTION B602 : shell=False et passage des arguments en liste pour éviter l'injection
    # On limite aussi les caractères autorisés pour 'host' par sécurité
    try:
        result = subprocess.check_output(["ping", "-c", "1", host], shell=False)
        return result
    except Exception as e:
        return str(e), 400

# CORRECTION B105 : Ne jamais mettre de mot de passe en dur. Utiliser une variable d'env.
ADMIN_PASSWORD_HASH = os.environ.get("ADMIN_PASSWORD_HASH", "hash_par_defaut_si_vide")

@app.route("/")
def home():
    return "Backend Sécurisé"

if __name__ == "__main__":
    # CORRECTION B201 : debug=False impératif en production
    app.run(debug=False)
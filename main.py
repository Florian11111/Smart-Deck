from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from functools import wraps

app = Flask(__name__)
api = Api(app)

# Benutzer und Token für die Authentifizierung
users = {
    "username": "password123"
}

# Funktion zur Token-Authentifizierung
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Token")

        if not token:
            return jsonify({"message": "Token fehlt"}), 401

        if token not in users.values():
            return jsonify({"message": "Ungültiger Token"}), 401

        return f(*args, **kwargs)

    return decorated

# Dummy-Speicher für Daten
data = {}

# Ressource für Daten setzen
class DataResource(Resource):
    @token_required
    def get(self, key):
        if key in data:
            return {key: data[key]}
        else:
            return {"message": "Datensatz nicht gefunden"}, 404

    @token_required
    def put(self, key):
        value = request.json.get("value")
        data[key] = value
        return {key: value}

api.add_resource(DataResource, "/data/<string:key>")

if __name__ == "__main__":
    app.run(debug=True, ssl_context=("path/to/your/certificate.pem", "path/to/your/private-key.pem"))

from flask import Flask
from flask_cors import CORS

from routes.auth import auth

from routes.energy import energy

app = Flask(__name__)   # ← app is created here

CORS(app)

app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(energy, url_prefix="/api")

@app.route("/")
def home():
    return {
        "message": "GREENTECH AI Backend Running"
    }

if __name__ == "__main__":
    app.run(debug=True)
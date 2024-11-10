from flask import Flask
from controller.controller import controller_routes
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.register_blueprint(controller_routes)

if __name__ == '__main__':
    app.run(debug=True)

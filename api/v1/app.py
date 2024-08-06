#!/usr/bin/python3
"""
Flask application setup
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    This function is called when the app context tears down.
    """
    storage.close()
    
@app.errorhandler(404)
def not_found(error):
    """

    """
    response = {"Error": "Not found"}
    return jsonify(response),404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(debug=True, host=host, port=port, threaded=True)

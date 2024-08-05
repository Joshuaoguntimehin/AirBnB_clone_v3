#!/usr/bin/python3
"""import statement"""
from models import storage
import os
from flask import Flask
from flask import jsonify
from api.v1.views import app_views

"""Create a Flask application instance"""
app = Flask(__name__)


"""Register the blueprint to the Flask app"""
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """Close the storage on app context teardown."""
    storage.close()


@app.errorhandler(404)
def not_found(Error):
    """
    Handler for 404 errors that returns a JSON response.
    """
    return jsonify({"error":"Notfound"}), 404 
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    
    # Run the Flask application
    app.run(host=host, port=port, threaded=True)
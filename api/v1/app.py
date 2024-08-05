#!/usr/bin/python3
"""import statement"""
from models import storage
import os
from flask import FLask
from api.v1.views import views

"""Create a Flask application instance"""
app = FLask(__name__)

"""Register the blueprint to the Flask app"""
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """Close the storage on app context teardown."""
    storage.close()

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    
    # Run the Flask application
    app.run(host=host, port=port, threaded=True)
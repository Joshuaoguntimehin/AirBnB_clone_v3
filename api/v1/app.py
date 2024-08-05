#!/usr/bin/python3
from models import storage
import os
from flask import FLask
from api.v1.views import views

app = FLask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(exception=None):
    storage.close()

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    
    # Run the Flask application
    app.run(host=host, port=port, threaded=True)
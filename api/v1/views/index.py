#!/usr/bin/python3
""" import statement """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.base_model import BaseModel, Base


@app_views.route('/status', methods=['GET'])
def status():
    """ This route returns the status of the API as a JSON object. """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_stats():
    """
    
    """
    stats ={
        "amenities": storage.count("Amenity"), 
        "cities": storage.count("City"), 
        "places": storage.count("Place"), 
        "reviews": storage.count("Rev"), 
        "states": storage.count("State"), 
        "users": storage.count("User")
    }
    return jsonify(stats)
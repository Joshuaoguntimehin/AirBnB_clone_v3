#!/usr/bin/python3
"""import statement"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', method=['GET'])
def get_status():
    """
    Returns the status of the API.
    """
    return jsonify({"status": "OK"})
@app_views.route('/starts')
def get_start():
    """
    
    """
    stats ={
        "amenities": storage.count("Amenity"), 
        "cities": storage.count("City"), 
        "places": storage.count("Place"), 
        "reviews": storage.count("Review"),
        "states": storage.count("State"), 
        "users": storage.count("user") 
    }
    
    return jsonify(stats)


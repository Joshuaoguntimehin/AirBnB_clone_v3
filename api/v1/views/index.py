#!/usr/bin/python3
"""import statement"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', method=['GET'])
def get_status():
    """
    Returns the status of the API.
    """
    return jsonify({"status": "OK"})
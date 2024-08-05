#!/usr/bin/python3
"""
import statement
"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """
    This route returns the status of the API as a JSON object.
    """
    return jsonify({"status": "OK"})

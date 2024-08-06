#!/usr/bin/python3
"""
RESTful API for State objects
"""

from flask import Flask, jsonify, abort, request
from models.state import State
from models import storage
from api.v1.views import app_views

@app_views.route("/states", methods=['GET'], strict_slashes=False)
def get_all_states():
    """
    Retrieve a list of all State objects
    """
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """
    Retrieve a State object by its ID
    """
    state = storage.get(State, state_id)
    
    if state:
        return jsonify(state.to_dict())
    else:
        return abort(404)
    
@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """
    Delete a State object by its ID
    """
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        return abort(404)
    
@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """
    Create a new State object
    """
    if not request.is_json:
        return abort(400, "Not a JSON")
        
    kwargs = request.get_json()
    
    if 'name' not in kwargs:
        return abort(400, "Missing name")
        
    state = State(**kwargs)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """
    Update a State object by its ID
    """
    if not request.is_json:
        return abort(400, 'Not a JSON')
        
    state = storage.get(State, state_id)
    
    if state:
        data = request.get_json()
        ignore_keys = ['id', 'created_at', 'updated_at']
        
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(state, key, value)
                
        state.save()
        return jsonify(state.to_dict()), 200
    else:
        return abort(404)

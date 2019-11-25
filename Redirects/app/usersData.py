"""This module will serve the api request."""

from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
import imp
import requests
import os

redIp=os.environ['REDIRECTIP']

@app.route("/")
def get_initial_response():

    red=requests.get(url="http://{}:5000/".format(redIp))
    return red.content,red.status_code


@app.route("/api/v1/users", methods=['POST'])
def create_user():
    
    red=requests.post(url="http://{}:5000/api/v1/users".format(redIp),json=request.get_json())
    
    return red.content,red.status_code


@app.route("/api/v1/users", methods=['GET'])
def fetch_users():
    red=requests.get(url="http://{}:5000/api/v1/users".format(redIp))
    
    return red.content,red.status_code


if __name__ == '__main__':
    # Running app in debug mode
    app.run(debug=True,host="0.0.0.0")


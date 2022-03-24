from flask import Blueprint, render_template, jsonify, request
from api import *

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    out = getPay()
    o1 = out[0]
    o2 = out[1]
    return render_template("index.html")

@views.route('/test', methods=['GET', 'POST'])
def testfn():
    out = getPay()
    o1 = out[0]
    o2 = out[1]
    # GET request
    if request.method == 'GET':
        message = {'left': o1, 'right': o2}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

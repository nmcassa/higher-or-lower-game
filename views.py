from flask import Blueprint, render_template, jsonify, request
from api import *
from void import *

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/gameRL")
def game():
    return render_template("gameRL.html")

@views.route('/rl', methods=['GET', 'POST'])
def rlfn():
    rl = randomize(rl_getPay())
    # GET request
    if request.method == 'GET':
        messageRL = {'messageRL': rl}
        return jsonify(messageRL)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

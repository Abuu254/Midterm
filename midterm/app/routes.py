"""application routes"""
import random
from datetime import datetime
from flask import render_template, jsonify
from database import get_object_details
from app import app, db
from app.models import Object


@app.before_first_request
def startup():
    """Get the list of IDS only when the flask app starts"""
    # Code to execute when the Flask app starts
    object_ids = db.session.query(Object.id).all()
    object_ids_list = [obj_id[0] for obj_id in object_ids]
    app.config['OBJECT_IDS'] = object_ids_list

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """Home page"""
    time = datetime.now().strftime("%m/%d/%Y, %I:%M:%S %p")
    print(time)

    # get the list of ids from config
    object_ids_list = app.config.get('OBJECT_IDS', [])

    # object id
    object_id = get_random_id(object_ids_list)
    info = get_object_details(object_id)
    print(info)
    print(object_id)

    return render_template('index.html',
    object_id=object_id, time=time,
    label=info['label'],
    date=info['date'],
    agents=info['agents_and_parts'])

@app.route('/next_object')
def next_object():
    """Get information about a random object and return as a JSON response"""
    object_ids_list = app.config.get('OBJECT_IDS', [])
    object_id = get_random_id(object_ids_list)
    object_details = get_object_details(object_id)
    return jsonify({
        'object_id': object_id,
        'label': object_details['label'],
        'date': object_details['date'],
        'agents': object_details['agents_and_parts']
    })

@app.route('/prev_object/<int:obj_id>')
def prev_object(obj_id):
    """Get information about a given object id and return as a JSON response"""
    object_id = obj_id
    object_details = get_object_details(object_id)
    return jsonify({
        'object_id': object_id,
        'label': object_details['label'],
        'date': object_details['date'],
        'agents': object_details['agents_and_parts']
    })



###-----Helper-----###
def get_random_id(lst):
    """Return random id"""
    return random.choice(lst)

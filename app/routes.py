from flask import jsonify, request

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to the List Sum Api!"


@app.route('/total')
def sum_list(*args):
    if args:
        print("present")
    else:
        numbers_to_add = list(range(10000001))
    
    if len(numbers_to_add) == 0:
        return "List provided is empty"
    else:
        list_sum = sum(numbers_to_add)
        return jsonify(total=list_sum)
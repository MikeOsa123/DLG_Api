from flask import jsonify, request

from app import app

# hard coded a list of numbers to mock list provided from a backend service
numbers_to_add = list(range(10000001))

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to the List Sum Api!"


@app.route('/total')
def sum_list(*args):
    if args:
        print("List provided")
    else:
        args = numbers_to_add
    
    if len(args) == 0:
        return "List provided is empty"
    else:
        list_sum = sum(args)
        return jsonify(total=list_sum)
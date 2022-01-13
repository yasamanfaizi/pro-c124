from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

#creating an array of tasks with each task has a different name
tasks = [
    {
        'id': 1,
        'name': 'Yasaman',
        'contact': '12345678',
        'done': False
    }, 
    {
        'id': 2,
        'name': 'Ms Asma',
        'contact': '87654321',
        'done': False

    }
]
@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "states": "error",
            "message": "please provide the data"
        }, 
        400)
    task = {
        'id': tasks[-1]['id']+1,
        'name': request.json['name'],
        'contact': request.json.get('contact', " "),
        'done': False

    }
    tasks.append(task)
    return jsonify({
        "states": "success",
        "message": "Contact added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

if(__name__ == "__main__"):
    app.run()
from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
id_task_control = 1

@app.route("/tasks", methods=['POST'])
def create_task():
    global id_task_control
    data = request.get_json()
    newTask = Task(id=id_task_control, title=data.get("title"), description=data.get("description"))
    id_task_control += 1    
    tasks.append(newTask)
    return jsonify({"message": "Nova tarefa criada com sucesso."})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE = "tasks.json"

# Load tasks
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f)

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")

    if task:
        tasks.append(task)
        save_tasks()

    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
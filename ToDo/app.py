from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    title = request.form.get("title")
    tasks = load_tasks()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/delete_task/<int:index>")
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{deleted_task['title']}' deleted.")
    return redirect(url_for("index"))

@app.route("/mark_completed/<int:index>")
def mark_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"Task marked as completed.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
from controllers.task_controller import TaskController

app = Flask(__name__, template_folder="templates", static_folder="static")
controller = TaskController()

def task_to_dict(t):
    return {
        "id": t.id,
        "title": t.title,
        "completed": t.completed,
        "created_at": t.created_at.isoformat(timespec="seconds"),
    }


@app.get("/")
def home():
    return render_template("index.html")

@app.get("/tasks")
def list_tasks():
    return jsonify([task_to_dict(t) for t in controller.all()])

@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "title requis"}), 400
    t = controller.add(title)
    return jsonify(task_to_dict(t)), 201

# @app.put("/tasks/<int:task_id>")
# def rename_task(task_id: int):
#     data = request.get_json(silent=True) or {}
#     new_title = (data.get("title") or "").strip()
#     if not new_title:
#         return jsonify({"error": "title requis"}), 400
#     ok = controller.rename(task_id, new_title)
#     if not ok:
#         return jsonify({"error": "id introuvable"}), 404
#     return jsonify(task_to_dict(controller.get_by_id(task_id)))

# @app.patch("/tasks/<int:task_id>/toggle")
# def toggle_task(task_id: int):
#     ok = controller.toggle(task_id)
#     if not ok:
#         return jsonify({"error": "id introuvable"}), 404
#     return jsonify(task_to_dict(controller.get_by_id(task_id)))

@app.delete("/tasks/<int:task_id>")
def delete_task(task_id: int):
    ok = controller.delete(task_id)
    if not ok:
        return jsonify({"error": "id introuvable"}), 404
    return ("", 204)

# @app.delete("/tasks/completed")
# def delete_completed():
#     n = controller.clear_completed()
#     return jsonify({"deleted": n})

if __name__ == "__main__":
    app.run(debug=True)

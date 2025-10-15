from typing import List, Optional
from model.task import Task


class TaskController:
    """Logique métier pour gérer la liste des tâches."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    # CRUD de base
    def add(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Le titre de la tâche est requis.")
        task = Task(id=self._next_id, title=title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def delete(self, task_id: int) -> bool:
        for i, t in enumerate(self._tasks):
            if t.id == task_id:
                del self._tasks[i]
                return True
        return False

    # def toggle(self, task_id: int) -> bool:
    #     task = self.get_by_id(task_id)
    #     if task:
    #         task.toggle()
    #         return True
    #     return False

    # def rename(self, task_id: int, new_title: str) -> bool:
    #     task = self.get_by_id(task_id)
    #     if task:
    #         task.rename(new_title)
    #         return True
    #     return False

    # Lecture
    def all(self) -> List[Task]:
        return list(self._tasks)

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for t in self._tasks:
            if t.id == task_id:
                return t
        return None

    # def clear_completed(self) -> int:
    #     before = len(self._tasks)
    #     self._tasks = [t for t in self._tasks if not t.completed]
    #     return before - len(self._tasks)

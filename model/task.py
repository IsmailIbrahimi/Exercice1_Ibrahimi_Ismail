from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """Représente une tâche de la ToDoList.

    Attributs:
        id: identifiant unique (assigné par le contrôleur)
        title: titre court de la tâche
        completed: état d'avancement
        created_at: date de création (informative)
    """

    id: int
    title: str
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    # def toggle(self) -> None:
    #     """Inverse l'état d'avancement de la tâche."""
    #     self.completed = not self.completed

    # def rename(self, new_title: str) -> None:
    #     """Modifie le titre de la tâche."""
    #     new_title = new_title.strip()
    #     if not new_title:
    #         raise ValueError("Le titre ne peut pas être vide.")
    #     self.title = new_title

    def __str__(self) -> str:  # Pour un affichage simple
        status = "✅" if self.completed else "⏳"
        return f"[{status}] #{self.id} - {self.title} (créée le {self.created_at:%Y-%m-%d %H:%M})"
from typing import Iterable
from model.task import Task


def print_header() -> None:
    print("\n====== ToDoList – CLI (débutant) ======")
    print("Commandes : add <titre> | del <id> | toggle <id> | rename <id> <nouveau titre> | list | clear | help | quit")


def print_tasks(tasks: Iterable[Task]) -> None:
    has_any = False
    for t in tasks:
        has_any = True
        print(f" - {t}")
    if not has_any:
        print("(aucune tâche pour l'instant)")


def print_help() -> None:
    print(
        """
Aide rapide :
  add <titre>                Ajoute une tâche
  del <id>                   Supprime une tâche
  toggle <id>                Marque/démarque une tâche comme terminée
  rename <id> <nouveau>      Renomme une tâche
  list                       Affiche toutes les tâches
  clear                      Supprime toutes les tâches terminées
  help                       Affiche cette aide
  quit                       Quitte le programme
        """.strip()
    )

README = r"""
# ToDoList CLI (Python, MVC, POO – ultra débutant)

Petit projet en ligne de commande pour gérer une liste de tâches.

## Objectifs pédagogiques
- Structurer un mini-projet façon MVC (model / views / controllers).
- Pratiquer la POO très simple (classe `Task`, contrôleur `TaskController`).
- Adopter de bonnes bases: types, docstrings, fonctions pures côté modèle/contrôleur.

## Prérequis & installation
- Python 3.10+
- Pas de dépendances externes (`requirements.txt` est vide).

```bash
python --version
# Cloner / copier le projet puis exécuter :
python main.py
```

## Commandes disponibles
- `add <titre>` : ajoute une tâche
- `del <id>` : supprime la tâche d'identifiant `<id>`
- `toggle <id>` : termine / ré-ouvre la tâche
- `rename <id> <nouveau titre>` : renomme la tâche
- `list` : affiche toutes les tâches
- `clear` : supprime les tâches terminées
- `help` : affiche l'aide
- `quit` : quitte

## Architecture
```
model/            # données et logique métier locale à l'entité
  task.py         # class Task
controllers/      # logique d'orchestration des tâches
  task_controller.py
views/            # affichage CLI
  cli.py
main.py           # point d'entrée (boucle d'interaction)
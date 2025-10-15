# ToDoList CLI (Python, MVC, POO)

Petit projet en ligne de commande pour gérer une liste de tâches.

## Objectifs pédagogiques
- Structurer un mini-projet façon MVC (model / views / controllers).
- Pratiquer la POO très simple (classe `Task`, contrôleur `TaskController`).
- Adopter de bonnes bases: types, docstrings, fonctions pures côté modèle/contrôleur.

## Prérequis & installation
- Python 3.10+

```bash
python --version
python main.py
```

## Création d'un venv et installation des dépendances
```bash
python -m venv venv
```
```bash
cd venv
```
```bash
source Scripts/activate
```
```bash
pip install -r requirements.txt
```



## Commandes disponibles
- `add <titre>` : ajoute une tâche
- `del <id>` : supprime la tâche d'identifiant `<id>`
- `list` : affiche toutes les tâches
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
web/
  templates/
    index.html
  app.py

main.py           # point d'entrée (boucle d'interaction)


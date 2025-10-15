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
cd venv
source Scripts/activate
pip install -r requirements.txt
```



## Commandes disponibles
- `add <titre>` : ajoute une tâche
- `del <id>` : supprime la tâche d'identifiant `<id>`
- `toggle <id>` : termine / ré-ouvre la tâche (commande enlevée)
- `rename <id> <nouveau titre>` : renomme la tâche (commande enlevée)
- `list` : affiche toutes les tâches
- `clear` : supprime les tâches terminées (commande enlevée)
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
from controllers.task_controller import TaskController
from views.cli import print_header, print_tasks, print_help


def main() -> None:
    controller = TaskController()
    print_header()

    while True:
        try:
            raw = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAu revoir ! 👋")
            break

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()
        args = parts[1:]

        try:
            if cmd == "add":
                title = " ".join(args)
                task = controller.add(title)
                print(f"Ajouté : {task}")

            elif cmd == "del":
                if not args:
                    print("Il faut un id : del <id>")
                    continue
                ok = controller.delete(int(args[0]))
                print("Supprimé." if ok else "Id introuvable.")

            # elif cmd == "toggle":
            #     if not args:
            #         print("Il faut un id : toggle <id>")
            #         continue
            #     ok = controller.toggle(int(args[0]))
            #     print("État inversé." if ok else "Id introuvable.")

            # elif cmd == "rename":
            #     if len(args) < 2:
            #         print("Usage: rename <id> <nouveau titre>")
            #         continue
            #     task_id = int(args[0])
            #     new_title = " ".join(args[1:])
            #     ok = controller.rename(task_id, new_title)
            #     print("Renommé." if ok else "Id introuvable.")

            elif cmd == "list":
                print_tasks(controller.all())

            elif cmd == "clear":
                n = controller.clear_completed()
                print(f"{n} tâche(s) terminée(s) supprimée(s).")

            elif cmd == "help":
                print_help()

            elif cmd in {"quit", "exit"}:
                print("Au revoir ! 👋")
                break

            else:
                print("Commande inconnue. Tape 'help' pour l'aide.")

        except ValueError as e:
            print(f"Erreur: {e}")
        except Exception as e:
            print(f"Oups, une erreur est survenue: {e}")


if __name__ == "__main__":
    main()
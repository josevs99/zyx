import typer
from commands import services, users, requests_cmds, config_cmds, system_cmds

app = typer.Typer()
app.add_typer(services.app, name='service')
app.add_typer(users.app, name='user')
app.add_typer(requests_cmds.app, name='request')
app.add_typer(config_cmds.app, name='config')
app.add_typer(system_cmds.app, name='system')

def run_interactive():
    print("Welcome to ZYX CLI")
    print('Type "help" for list of commands or "exit" to quit')

    while True:
        try:
            raw = input("zyx> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if raw in ["exit", "quit"]:
            break
        if raw == "help":
            app(["--help"])
            continue
        if raw == "":
            continue

        # Split command into args
        args = raw.split(" ")
        try:
            app(args)
        except SystemExit:
            pass

if __name__ == "__main__":
    run_interactive()
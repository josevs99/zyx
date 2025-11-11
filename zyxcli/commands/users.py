import typer
from utils.http_client import HttpClient
app = typer.Typer()

@app.command('login')
def login(server: str = typer.Option(None, '--server'), user: str = typer.Option(..., '--user'), password: str = typer.Option(..., '--password')):
    """Login (ephemeral) - just tests credentials and prints result"""
    client = HttpClient(server_url=server, user=user, password=password)
    try:
        r = client.get('/service/get/invalid')  # a cheap authenticated call to verify auth
        if r.status_code in (200,404,401,403):
            typer.echo('Credentials appear valid (server responded with ' + str(r.status_code) + ')')
        else:
            typer.echo('Unexpected response: ' + str(r.status_code))
    except Exception as e:
        typer.echo('Error: ' + str(e))
        raise typer.Exit(code=1)

@app.command('whoami')
def whoami(server: str = typer.Option(None, '--server'), user: str = typer.Option(None, '--user'), password: str = typer.Option(None, '--password')):
    typer.echo('Ephemeral mode: provide --user/--password or set ZYX_USER/ZXY_PASS env vars.')

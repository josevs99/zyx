import typer
from utils.http_client import HttpClient
app = typer.Typer()

@app.command('version')
def version():
    typer.echo('zyxcli (docker) v0.1.0')

@app.command('health')
def health(server: str = typer.Option(None, '--server'), user: str = typer.Option(None, '--user'), password: str = typer.Option(None, '--password')):
    client = HttpClient(server_url=server, user=user, password=password)
    r = client.get('/health')
    if r.status_code == 200:
        typer.echo(r.text)
    else:
        typer.echo(f'Error {r.status_code}: ' + r.text)
        raise typer.Exit(code=1)

import typer
from utils.http_client import HttpClient
app = typer.Typer()

@app.command('list')
def list_requests(server: str = typer.Option(None, '--server'), user: str = typer.Option(None, '--user'), password: str = typer.Option(None, '--password')):
    client = HttpClient(server_url=server, user=user, password=password)
    r = client.get('/requests/list')
    if r.status_code == 200:
        typer.echo(r.text)
    else:
        typer.echo(f'Error {r.status_code}: ' + r.text)
        raise typer.Exit(code=1)

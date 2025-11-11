import typer
from utils.http_client import HttpClient
from utils.formatter import simple_table
app = typer.Typer()

@app.command('list')
def list_services(server: str = typer.Option(None, '--server'), user: str = typer.Option(None, '--user'), password: str = typer.Option(None, '--password')):
    """List services"""
    client = HttpClient(server_url=server, user=user, password=password)
    try:
        r = client.get('/service/list')
    except Exception as e:
        typer.echo('Error contacting server: ' + str(e))
        raise typer.Exit(code=1)
    if r.status_code != 200:
        typer.echo(f'Error {r.status_code}: ' + r.text)
        raise typer.Exit(code=1)
    data = r.json()
    headers = ['ID','Service Name','Status','Ongoing']
    rows = []
    for s in data:
        rows.append([s.get('id',''), s.get('serviceName',''), s.get('status',''), s.get('ongoing','')])
    typer.echo(simple_table(headers, rows))

@app.command('get')
def get_service(id: str, server: str = typer.Option(None, '--server'), user: str = typer.Option(None, '--user'), password: str = typer.Option(None, '--password')):
    client = HttpClient(server_url=server, user=user, password=password)
    r = client.get(f'/service/get/{id}')
    if r.status_code == 200:
        typer.echo(r.text)
    else:
        typer.echo(f'Error {r.status_code}: ' + r.text)
        raise typer.Exit(code=1)

@app.command('add')
def add_service(servicename: str = typer.Option(..., '--servicename'), server: str = typer.Option(None, '--server'), user: str = typer.Option(None, '--user'), password: str = typer.Option(None, '--password')):
    client = HttpClient(server_url=server, user=user, password=password)
    r = client.post('/service/add', params={'servicename': servicename})
    if r.status_code in (200,201):
        typer.echo(r.text)
    else:
        typer.echo(f'Error {r.status_code}: ' + r.text)
        raise typer.Exit(code=1)

@app.command('update')
def update_service(id: str = typer.Option(..., '--id'), servicename: str = typer.Option(..., '--servicename'), server: str = typer.Option(None, '--server'), user: str = typer.Option(None, '--user'), password: str = typer.Option(None, '--password')):
    client = HttpClient(server_url=server, user=user, password=password)
    r = client.put(f'/service/update/{id}', params={'servicename': servicename})
    if r.status_code == 200:
        typer.echo(r.text)
    else:
        typer.echo(f'Error {r.status_code}: ' + r.text)
        raise typer.Exit(code=1)

@app.command('delete')
def delete_service(id: str = typer.Option(..., '--id'), server: str = typer.Option(None, '--server'), user: str = typer.Option(None, '--user'), password: str = typer.Option(None, '--password')):
    client = HttpClient(server_url=server, user=user, password=password)
    r = client.delete(f'/service/delete/{id}')
    if r.status_code == 200:
        typer.echo('Deleted')
    else:
        typer.echo(f'Error {r.status_code}: ' + r.text)
        raise typer.Exit(code=1)

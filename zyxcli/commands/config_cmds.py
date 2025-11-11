import typer
app = typer.Typer()

@app.command('show')
def show():
    typer.echo('Ephemeral Docker CLI (no persistent config).')
    typer.echo('Use --server, or set ZYX_SERVER env var.')

import typer
from rich.console import Console

app = typer.Typer(help="REPOLens: codebase intelligence engine")
console = Console()


@app.command()
def version() -> None:
    """Show the current REPOLens version"""
    console.print("[bold green]REPOLens v0.1.0[/bold green]")


@app.command()
def ingest(repo_path: str) -> None:
    """Placeholder command"""
    console.print(f"[yellow]Ingestion not implemented yet.[/yellow] Repo path: {repo_path}")

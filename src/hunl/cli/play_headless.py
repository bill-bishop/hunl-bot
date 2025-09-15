import typer

app = typer.Typer()

@app.command()
def main():
    print("Starting headless play between agents (stub)")
    # TODO: integrate trained policies, environment loop

if __name__ == "__main__":
    app()
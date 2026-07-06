from rich.console import Console

from core.engine import process_query

console = Console()


def start_chat():
    console.print("=" * 60, style="cyan")
    console.print("[bold green]🤖 Welcome to AI Search Engine[/bold green]")
    console.print("[italic]Your AI-powered search assistant[/italic]")
    console.print("Type 'exit', 'quit', or 'bye' to quit.")
    console.print("=" * 60, style="cyan")

    while True:
        user_input = console.input("\n[bold cyan]You:[/bold cyan] ")

        # Ignore empty messages
        if not user_input.strip():
            continue

        # Exit application
        if user_input.lower() in ["exit", "quit", "bye"]:
            console.print("\n👋 Goodbye! See you soon.", style="bold red")
            break

        try:
            console.print("\n[bold green]AI:[/bold green] ", end="")

            # Stream the response token by token
            for chunk in process_query(user_input):
                console.print(chunk, end="")

            console.print("\n")

        except Exception as e:
            console.print(
                f"\n[bold red]Error:[/bold red] {str(e)}\n"
            )
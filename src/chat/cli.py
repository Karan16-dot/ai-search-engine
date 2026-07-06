import time

from rich.console import Console

from services.chat_service import ChatService
from utils.logger import logger

console = Console()
chat_service = ChatService()


def start_chat():
    logger.info("AI Search Engine started.")

    console.print("=" * 60, style="cyan")
    console.print("[bold green]🤖 Welcome to AI Search Engine[/bold green]")
    console.print("[italic]Your AI-powered search assistant[/italic]")
    console.print("Type 'exit', 'quit', or 'bye' to quit.")
    console.print("=" * 60, style="cyan")

    while True:
        user_input = console.input("\n[bold cyan]You:[/bold cyan] ")

        # Ignore empty input
        if not user_input.strip():
            continue

        # Exit application
        if user_input.lower() in ["exit", "quit", "bye"]:
            logger.info("Application closed by user.")
            console.print(
                "\n[bold red]👋 Goodbye! See you soon.[/bold red]"
            )
            break

        logger.info("User Query: %s", user_input)

        try:
            start_time = time.perf_counter()

            console.print("\n[bold green]AI:[/bold green] ", end="")

            for chunk in chat_service.stream_response(user_input):
                console.print(chunk, end="")

            elapsed = time.perf_counter() - start_time

            console.print()
            console.print(
                f"[dim]Response generated in {elapsed:.2f} seconds[/dim]\n"
            )

            logger.info(
                "Response generated successfully in %.2f seconds",
                elapsed
            )

        except Exception:
            logger.exception("Unexpected error while processing request.")

            console.print(
                "\n[bold red]An unexpected error occurred while generating the response.[/bold red]\n"
            )
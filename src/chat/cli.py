from rich.console import Console

from core.engine import process_query
from core.history import ConversationHistory

console = Console()


def start_chat():
    history = ConversationHistory()

    console.print("=" * 60, style="cyan")
    console.print("[bold green]🤖 Welcome to AI Search Engine[/bold green]")
    console.print("Type 'exit', 'quit', or 'bye' to quit.")
    console.print("=" * 60, style="cyan")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            console.print("\n👋 Goodbye! See you soon.", style="bold red")
            break

        # Store user message
        history.add_user_message(user_input)

        # Generate AI response
        response = process_query(user_input)

        # Store AI response
        history.add_ai_message(response)

        # Display AI response
        console.print(f"\n[bold green]AI:[/bold green] {response}")

        # Temporary: Print conversation history (for debugging)
        console.print("\n[bold yellow]Conversation History:[/bold yellow]")
        for message in history.get_messages():
            console.print(f"{message.role}: {message.content}")
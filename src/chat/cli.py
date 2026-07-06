def start_chat():
    print("=" * 50)
    print("🤖 Welcome to AI Search Engine")
    print("Type 'exit', 'quit', or 'bye' to quit.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\n👋 Goodbye! See you soon.")
            break

        print(f"AI: You said -> {user_input}")
from router import route_query

def main():
    print("🤖 Smart Helpdesk Chatbot (Phase 2) — type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        response = route_query(user_input)

        print("\nBot:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()

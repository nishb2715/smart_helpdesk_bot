from chains import get_helpdesk_chain

def main():
    print("🤖 Smart Helpdesk Chatbot (type 'exit' to quit)\n")

    chain = get_helpdesk_chain()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        response = chain.run(user_query=user_input)
        print("\nBot:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()

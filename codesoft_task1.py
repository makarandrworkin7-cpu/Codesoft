
def chatbot():
    print("🤖 Chatbot: Hello! I am your assistant. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "bye":
            print("Good bye.")
            break

        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How can I help you?")

        # Asking name
        elif "your name" in user_input:
            print("🤖 Chatbot: I am a chatbot.")

        # Asking about user
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm good how are you")

        # Help
        elif "help" in user_input:
            print("🤖 Chatbot: plz carify what kind of help you need ")

        # Time
        elif "time" in user_input:
            from datetime import datetime
            print("🤖 Chatbot:", datetime.now().strftime("%H:%M:%S"))

        # Date
        elif "date" in user_input:
            from datetime import datetime
            print("🤖 Chatbot:", datetime.now().strftime("%Y-%m-%d"))

        # Default response
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

# Run chatbot
chatbot()

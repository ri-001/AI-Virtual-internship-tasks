def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("ChatBot: Hello! How can I help you today?")

        elif "how are you" in user_input:
            print("ChatBot: I'm doing great! Thanks for asking. How are you doing?")
        
        elif "i am fine" in user_input or "i'm fine" in user_input:
            print("ChatBot: Glad to hear that!")

        elif user_input in ["name", " your name"] :
            print("ChatBot: I am a Rule-Based ChatBot.")

        elif "help" in user_input:
            print("ChatBot: I can answer simple questions like greetings, my name, and basic help.")

        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"ChatBot: The current time is {current_time}")
        
        elif "date" in user_input:
            from datetime import date
            current_date = date.today()
            print(f"ChatBot: The current date is {current_date}")
        
        elif "thank you" in user_input or "thanks" in user_input:
            print("Bot: You're welcome! Happy to help.")

        elif user_input in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye! Have a nice day!")
            break

        else:
            print("ChatBot: Sorry, I don't understand that.")
chatbot()



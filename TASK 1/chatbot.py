import re

class RuleBasedChatbot:
    def __init__(self):
        pass

    def greet(self, user_input):
        return "Hi there! How can I help you today?"

    def farewell(self, user_input):
        return "Take care! If you have more questions, feel free to ask!"

    def how_are_you(self, user_input):
        return "I'm just a chatbot, but I'm functioning as expected! How about you?"

    def name(self, user_input):
        return "I'm an AI assistant designed to help you with your inquiries."

    def weather(self, user_input):
        return "I can't give real-time weather updates, but checking a weather app should help!"

    def joke(self, user_input):
        return "Why did the computer go to the doctor? Because it had a virus!"

    def help(self, user_input):
        return "I can chat with you, tell jokes, discuss the weather, and more. What do you need assistance with?"

    def default_response(self, user_input):
        return "I'm not sure I understand. Could you please clarify your question?"

    def respond(self, user_input):
        # Use pattern matching with regex to identify user intent
        if re.search(r'\bhello\b|\bhi\b|\bhey\b|\bhowdy\b', user_input, re.IGNORECASE):
            return self.greet(user_input)
        elif re.search(r'\bbye\b|\bgoodbye\b|\blater\b|\bsee you\b', user_input, re.IGNORECASE):
            return self.farewell(user_input)
        elif re.search(r'\bhow are you\b|\bhow's it going\b', user_input, re.IGNORECASE):
            return self.how_are_you(user_input)
        elif re.search(r'\bwhat is your name\b|\bwho are you\b|\bwho is this\b', user_input, re.IGNORECASE):
            return self.name(user_input)
        elif re.search(r'\bweather\b|\bforecast\b', user_input, re.IGNORECASE):
            return self.weather(user_input)
        elif re.search(r'\bjoke\b|\btell me a joke\b', user_input, re.IGNORECASE):
            return self.joke(user_input)
        elif re.search(r'\bhelp\b|\bassistance\b|\bsupport\b', user_input, re.IGNORECASE):
            return self.help(user_input)
        else:
            return self.default_response(user_input)

if __name__ == "__main__":
    bot = RuleBasedChatbot()
    print("Chatbot: Hi there! How can I help you today? Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if re.search(r'\bbye\b|\bgoodbye\b|\blater\b|\bsee you\b', user_input, re.IGNORECASE):
            print("Chatbot: Take care! If you have more questions, feel free to ask!")
            break
        response = bot.respond(user_input)
        print(f"Chatbot: {response}")

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def get_bot_response(user_input):
    if user_input == "hello":
        return "Hi there! How can I assist you today? 👋"
    
    elif user_input == "how are you":
        return "I'm an AI, so I don't have feelings, but I'm here to help you! 🤖"
    
    elif user_input == "what's your name":
        return "I'm Chatbot, your virtual assistant. Nice to meet you! 😊"
    
    elif user_input == "what can you do":
        return ("I can have a simple conversation with you. You can ask me about the weather, "
                "the time, or just say 'bye' to end our chat. 💬")
        
    elif user_input == "what's the time":
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')} ⏰"
    
    elif user_input == "what's the date":
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%Y-%m-%d')} 📅"
    
    elif user_input == "tell me a joke":
        return ("Why don't scientists trust atoms? 🤔\n"
                "Because they make up everything! ⚛️")
        
    elif user_input.startswith("what is the weather like"):
        return "I can't check the weather right now, but I hope it's sunny where you are! ☀️"
    
    elif user_input.startswith("what is your favorite"):
        if "color" in user_input:
            return "My favorite color is blue! 💙"
        elif "food" in user_input:
            return "I don't eat, but I imagine pizza would be great! 🍕"
        else:
            return "I don't have preferences, but I can help with many topics! 🤓"
        
    elif user_input == "bye":
        return "Goodbye! Have a fantastic day! 👋"
    else:
        return "I'm sorry, I don't understand that. 😕"


@app.route("/", methods=["GET", "POST"])
def index():
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = get_bot_response(user_input)
    return render_template("index.html", bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)

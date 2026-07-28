from datetime import datetime 
import random 
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
    "Why did the Python developer go broke? Because he couldn't C! 😄",
    "Debugging is like being a detective in a crime movie where you are also the criminal. 🤣",
    "There are only 10 types of people: those who understand binary and those who don't. 😎",
    "I told my computer I needed a break, and it said 'No problem, I'll go to sleep.' 😴"
]
quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Believe in yourself and all that you are.",
    "The harder you work, the luckier you get.",
    "Don't stop until you're proud.",
    "Every expert was once a beginner."
]
print("=" * 50)
print("Codeaplha CHATBOT")
print("=" * 50)
name = input("Hey..What should I call you : ")
print(f"Hello, {name} !")
print("How can I help you ?")

while True :

    user_input = input(f"{name} : ").lower()

    if user_input == "hello" or user_input == "hi":
          print(f"Bot : Hi {name} !")
    elif user_input == "who are you":
         print("I am an Python CHATBOT ")
    elif user_input == "what can you do":
         print("I can chat, tell jokes, motivate you, show date & time, and perform calculations.")
    elif user_input == "thank you":
         print("You're welcome! Happy to help.")
    elif user_input == "good morning":
         print(f"Good Morning, {name}! Have a productive day!")
    elif user_input == "good night":
         print(f"Good Night, {name}! Sleep well.")     
    elif user_input == "how are you":
          print("Bot : I am doing great, thankyou !")
    elif user_input == "what is your name":
          print("Bot : I am Codealpha CHATBOT.") 
    elif user_input == "who created you":
          print("Bot : I was created using python")   
    elif user_input == "time":
         current_time = datetime.now().strftime("%I:%M:%S %p")
         print(f"Bot: Current time is {current_time}")
    elif user_input == "date":
         current_date = datetime.now().strftime("%d-%m-%Y")
         print(f"Bot: Today's date is {current_date}") 
    elif user_input == "joke":
          print("Bot : ",random.choice(jokes))
    elif user_input == "qoute" or user_input == "motivational quote" or user_input == "quote":
              print("Bot : ",random.choice(quotes))   
    elif user_input == "calculator":
          num1 = float(input("Enter first no : "))
          op = input("Enter the operator [+,-,%,/ and *] : ")
          num2 = float(input("Enter second no : "))      
          if op == "+":
                print("Bot : Result = ", num1+num2)         
          elif op == "-":
                print("Bot : Result = ", num1-num2)
          elif op == "*":
                print("Bot : Result = ", num1*num2) 
          elif op == "%":
                print("Bot : Result = ", num1%num2)        
          elif op == "/":
                if num2 != 0:
                  print("Bot : Result = ", num1/num2)  
                else :
                  print("Bot : Cannot divide by zero!")      
          else :
                print("Bot : Invalid Operator !")                                                          
    elif user_input == "help":
          print("\n========== AVAILABLE COMMANDS ==========")
          print("hello / hi        - Greet the chatbot")
          print("how are you       - Ask about the chatbot")
          print("time              - Show current time")
          print("date              - Show today's date")
          print("joke              - Hear a joke")
          print("quote             - Get a motivational quote")
          print("calculator        - Open calculator")
          print("bye               - Exit the chatbot")
          print("========================================\n")                    
    elif user_input == "bye":
          print(f"Bot : Good-bye {name} ! ")
          break 
    else :
          print("Bot : Sorry, i don't understand... Type 'help' for more available commands ") 


                
# Chatbot
# Author: Lynn 
# Date: 20 September 2023

# Greet the user
print("Hello there! 🤖")
print("I'm a crude Chatbot, here to talk to you.")

# Get the user's name and store it in the variable
user_name = input("So... What's your name? ")

# Respond with the user's name in a friendly way
print(f"It's good to meet you, {user_name}.")

# Ask the user what their favourite food is
favourite_food = input("I have a quick question... What is your favourite food? ")

# Make a comment about their favourite food but NOT OVERLY REPETITIVE
# Create a list of possible responses 
list_of_food_responses = [
    f"Oh, I've never had {favourite_food} before!",
    "Mmmmm. That sounds good!",
    "I heard that that is very good!",
    "That's cool!",
    "Oh! that does sound pretty good right about now! 🤠"
]

# Choose one of those responses randomly
import random
random_food_response = random.choice(list_of_food_responses)

# Print out that chosen response
print(random_food_response)
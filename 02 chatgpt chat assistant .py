# Import the OpenAI library
import openai

# Set your OpenAI API key
openai.api_key = "####"  # Replace "####" with your actual OpenAI API key

# Initialize an empty list to store chat messages
messages = []

# Prompt the user to define the type of chatbot they want to create
system_msg = input("What type of chatbot would you like to create?\n")

# Add the system message to the list of messages
messages.append({"role": "system", "content": system_msg})

# Display a message indicating that the chatbot is ready
print("Your new assistant is ready!")

# Continue the conversation until the user types "quit()"
while input != "quit()":
    # Prompt the user for their input
    message = input()

    # Add the user's message to the list of messages
    messages.append({"role": "user", "content": message})

    # Use the OpenAI Chat API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract the generated reply from the API response
    reply = response["choices"][0]["message"]["content"]

    # Add the assistant's reply to the list of messages
    messages.append({"role": "assistant", "content": reply})

    # Print the assistant's reply
    print("\n" + reply + "\n")

# Import the OpenAI library
import openai

# Import the Gradio library for creating user interfaces
import gradio

# Set your OpenAI API key
openai.api_key = "####"  # Replace "####" with your actual OpenAI API key

# Initialize the conversation with a system message
messages = [{"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation"}]

# Define a function for the Gradio interface
def CustomChatGPT(user_input):
    # Add the user's input to the list of messages
    messages.append({"role": "user", "content": user_input})
    
    # Use the OpenAI Chat API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Extract the generated reply from the API response
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    
    # Add the assistant's reply to the list of messages
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    
    # Return the generated reply for display in the Gradio interface
    return ChatGPT_reply

# Create a Gradio interface with a custom function for the chatbot
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro")

# Launch the Gradio interface and allow sharing
demo.launch(share=True)

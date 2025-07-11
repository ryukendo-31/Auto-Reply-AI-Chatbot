import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create OpenAI client using the new SDK format
client = openai.OpenAI(api_key=os.getenv("API_KEY"))

command = ''''''#add the text you wish to reply to

# Call Chat API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named Aaryan Sharma from India. You are very friendly, sarcastic, and mock your friends in a funny way. Based on the chat history, respond like Aaryan."},
        {"role": "user", "content": command}
    ]
)

# Print the assistant's response
print(response.choices[0].message.content)


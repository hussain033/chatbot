from fastapi import FastAPI
import uvicorn

# predict is a function which includes the ai chatbot model.
# predict function takes the input text and returns output text
# predict function is defined inside the file - chatBot {temporary - just for example}
from chatbot import chat
app = FastAPI()

@app.get('/')
def predict(data : str):

    # getting the chat Output
    output_text = chat(data)

    # Return the Result
    return { 'chatBot' : output_text }

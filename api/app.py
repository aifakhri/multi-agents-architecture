import logging
from fastapi import FastAPI
from dotenv import load_dotenv


from agents import lead_agent
from schema import ChatMessage

load_dotenv()


app = FastAPI()


@app.post("/supervisor/")
async def chat_supervisor(message: ChatMessage):
    """
    """

    logging.info(message.text)

    user_query = {
            "messages": [
                {
                    "role": "user",
                    "content": message.text
                }
            ]
        }

    response = lead_agent().stream(user_query)

    return {"chat_response": response}
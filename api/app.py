import logging
from fastapi import FastAPI
from dotenv import load_dotenv


from services import research_agent
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

    response = research_agent().stream(user_query)

    return {"chat_response": response}
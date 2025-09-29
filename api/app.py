import logging
from fastapi import FastAPI
from dotenv import load_dotenv


from services import research_agent, math_agent
from schema import ChatMessage

load_dotenv()


app = FastAPI()


@app.post("/researcher/")
async def chat_researcher(message: ChatMessage):
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

@app.post("/math/")
async def chat_math(message: ChatMessage):
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

    response = math_agent().stream(user_query)

    return {"chat_response": response}
import requests
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
import json

from logs import logger, log_execution_time

app = FastAPI()


@log_execution_time
@app.post("/message")
async def twilio_message_endpoint(request: Request):
    data = await request.form()
    user_input = data.get("Body", "")
    reqUrl = "https://mattoofahad-whatsapp-endpoint.hf.space/message"
    headersList = {
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    payload = json.dumps({"user_input": str(user_input)})
    response = requests.request("POST", reqUrl, data=payload, headers=headersList)
    logger.info(response.text)
    return PlainTextResponse(response.text)


if __name__ == "__main__":
    app.run()

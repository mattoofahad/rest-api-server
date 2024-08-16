import requests
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

from logs import logger, log_execution_time

app = FastAPI()


class UserInputModel(BaseModel):
    user_input: str


@log_execution_time
@app.post("/message")
async def twilio_message_endpoint(request: Request):
    data = await request.form()
    user_input = data.get("Body", "")
    user_input = data.user_input
    reqUrl = "https://mattoofahad-whatsapp-endpoint.hf.space/message"
    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = f"Body={user_input}"
    response = requests.request("POST", reqUrl, data=payload, headers=headersList)
    logger.info(response.text)
    return PlainTextResponse(response.text)


if __name__ == "__main__":
    app.run()

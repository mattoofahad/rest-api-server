---
title: This a fastapi middleware.
colorFrom: blue
colorTo: yellow
emoji: 🙌🙌
sdk: docker
app_file: main.py
pinned: false
---

<!-- # Whatsapp-Chatbot
A simple repository to integrate a chatbot with whatsapp. -->

<!-- <p float="left">
  <img src="" alt="screenshot1" width="300" style="margin-right: 20px;" />
  <img src="" alt="screenshot2" width="300" />
</p> -->

<!-- ## Purpose and Features ✨ -->


<!-- ## Prerequisites 🔑

To run and deploy the WhatsApp chatbot, you will need the following:

1. [Twilio Account](https://console.twilio.com/user/account-create): Create a Twilio account and obtain your Account SID and Auth Token.

2. WhatsApp Sandbox: Set up a WhatsApp Sandbox in your Twilio account to receive and send messages.

3. Python: Install Python on your local machine. The recommended version is Python 3.x.

4. Ngrok: [Download](https://ngrok.com/download) and install Ngrok from the official website (https://ngrok.com/) based on your operating system.

5. OpenAI API: Sign up for the OpenAI API and obtain your Secret API key from user settings (you may require a paid account for this). -->

## Installation and Usage 

1. Create conda env
    ```bash
    conda create -n rest_server python=3.10 -y
    ```

2. Activate env
    ```bash
    conda activate rest_server
    ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

<!-- # docker

## Docker 
1. Create the docker container
   ```bash
   docker build -t whatapp-endpoint .
   ```

2. run the container
   ```bash
   docker run -p 7860:7860 whatapp-endpoint
   ``` -->
<!-- 4. Create a `.env` file in the root directory of the project. -->

<!-- 5. Add the following lines to the `.env` file:

   ```plaintext
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   OPENAI_API_KEY=your_openai_api_key
   TWILIO_NUMBER= your_twilio_number
   RECEIPENT_NUMBER= your_number
   ```

   Replace `your_account_sid`, `your_auth_token`, `your_openai_api_key`, `your_twilio_number`, and `your_number` with your actual credentials. -->


5. Run the local server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5000
   ```

<!-- 6. Start Ngrok to create a public URL for your local server:

   ```bash
   ngrok http 5000
   ```

7. Update the WhatsApp sandbox with the Ngrok URL. Set the incoming message webhook to `<your_ngrok_url>/message` , leave the callback url box empty.

8. Send a message to the WhatsApp sandbox number to interact with the bot and receive information. -->

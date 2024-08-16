---
title: This a fastapi middleware.
colorFrom: blue
colorTo: yellow
emoji: 🙌🙌
sdk: docker
app_file: main.py
pinned: false
---

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

3. Run the local server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5000
   ```

## Docker 
1. Create the docker container
   ```bash
   docker build -t rest-server .
   ```

2. run the container
   ```bash
   docker run -p 7860:7860 rest-server
   ```
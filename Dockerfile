FROM python:3.11

# Create a user and switch to it
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY --chown=user ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy application files
COPY --chown=user . /app/

# Expose the port
EXPOSE 7860

# Use CMD or ENTRYPOINT
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

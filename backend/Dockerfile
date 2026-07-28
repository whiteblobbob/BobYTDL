FROM python:3.14-slim

WORKDIR /app

# deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ffmpeg (necessary for conversion)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# run
COPY . .
EXPOSE 8000
CMD [ "fastapi", "run", "main.py" ]
FROM sanicframework/sanic:3.12-latest

WORKDIR /app

COPY src app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "server.py"]

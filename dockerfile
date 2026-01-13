FROM alpine:latest
RUN apk add --no-cache python3
WORKDIR /app
COPY . .
COPY install.sh /app/install.sh
RUN chmod +x install.sh
RUN ./install.sh
CMD ["python3", "main.py"]

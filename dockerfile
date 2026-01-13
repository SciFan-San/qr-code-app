FROM alpine:latest
RUN apk add --no-cache python3 bash
WORKDIR /app
COPY . .
RUN chmod +x install.sh
RUN ./install.sh
EXPOSE 5000
CMD ["python3", "main.py"]

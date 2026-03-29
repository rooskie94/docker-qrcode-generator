# Docker QR Code Generator

A lightweight web-based QR code generator built with Python and packaged as a Docker container. <br>

<img width="1586" height="503" alt="Screen Shot 2026-03-29 at 13 10 06 PM" src="https://github.com/user-attachments/assets/75191788-8eaa-4fd9-84da-39d60cd8688a" /> <br>


The app provides a simple web interface where you:
1. Enter a URL  
2. Click **Generate QR Code**  
3. Download the generated QR code image  

---

## Features

- Simple web UI
- Dark Mode
- Generates downloadable QR codes

---

## Requirements

- Docker (v20+ recommended)  
- OR Docker with the Compose plugin (`docker compose`)

---

## Option 1: Run with Docker (Quick Start)

Pull the image:

```bash
docker pull rooskie94/docker-qrcode-generator:latest
```
```
docker run -d \
  --name qrcode-generator \
  -p 8080:8080 \
  rooskie94/docker-qrcode-generator:latest
```

#### http://localhost:8080


## Option 2: Run with Docker Compose (Recommended)

Create a `compose.yaml` file:

```yaml
services:
  qrcode-generator:
    image: rooskie94/docker-qrcode-generator:latest
    container_name: qrcode-generator
    ports:
      - "8080:8080"
    restart: unless-stopped
```
Start the continer
```
docker compose up -d
```

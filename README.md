# Lululemon Product Scraper API

## Summary
This project is a serverless Python-based web scraper API designed to run on AWS Lambda. It fetches product details from Lululemon's website using Scrapy. The API provides a single GET endpoint that extracts data from specified URLs and returns product details such as display name, category, image, price, currency, and URL.

## Requirements
- Python 3.9
- AWS SAM CLI

## Installation and Running Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/plenzjr/serverless-python-web-scraper
cd serverless-python-web-scraper
```

### Step 2: Install AWS SAM CLI
Follow the installation instructions for your operating system from the [AWS SAM CLI documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).

### Step 3: Build the Application
```bash
sam build
```

### Step 4: Start the Local API
```bash
sam local start-api
```

### Step 5: Invoke the API Endpoint
Use your browser or a tool like `curl` to invoke the endpoint.

```bash
curl http://127.0.0.1:3000/scrape
```

## API Endpoints

### GET /scrape/

Fetch product data from predefined Lululemon URLs.

#### Response Format (json)

```json
[
    {
        "displayName": "Align Pant 28",
        "category": "Women's Leggings",
        "first_image": "https://example.com/image.jpg",
        "price": 98.0,
        "currency": "USD",
        "url": "https://shop.lululemon.com/product/123"
    },
    ...
]
```



# Spam Classifier API

This is a **machine-learning-based API** that detects whether a text message (SMS or email) is spam or not. The API allows sending text and receiving an instant spam/ham prediction.

---

## Tech Stack

* **Flask** – REST API framework
* **scikit-learn** – Machine learning model
* **Astra DB** – Cloud database storage
* **Docker** – Containerization

---

## Features

* Accepts text input via API requests
* Classifies messages as **spam** or **ham**
* Returns prediction with confidence score
* Stores predictions in Astra DB for tracking
* Docker support for easy deployment

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Madhusanka-slc/spam-classifier-api.git
cd spam-classifier-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
python app/app.py
```

Or using Gunicorn for production:

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

Now the API will be running at `http://127.0.0.1:8000`. You can test endpoints using **Postman** or **curl**.

# Subscription Management System with Currency Exchange Tracker

A Django-based system to manage user subscriptions and track real-time currency exchange rates.

## Objective

Build a production-ready backend system that supports:
- REST APIs using Django REST Framework (DRF)
- Background tasks with Celery and Redis
- External API integration for currency exchange
- Admin interface for management
- Basic frontend using Django templates + Bootstrap
- Docker support

---

## Tech Stack

- Python, Django, DRF
- MySQL
- Redis + Celery
- Bootstrap 5 (Frontend)
- Docker & Docker Compose
- External API: [ExchangeRate-API](https://www.exchangerate-api.com/)

---

## Project Structure

```text
subscription_system/
├── manage.py
├── subscription_system/
│   ├── settings.py
│   └── ...
├── core/
│   ├── models.py
│   ├── views.py
│   ├── tasks.py
│   └── templates/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
README.md
```
## 1. Clone the project
```bash
git@github.com:noshinfaria/Subscription-System.git
```
or
```bash
https://github.com/noshinfaria/Subscription-System.git
```
## 2. Change directory
```bash
cd subscription_system
```
## 3. Create .env file(rename env.example to .env)

## 4. Docker Setup
- Requires Docker & Docker Compose installed.


 Build and run the containers:

```bash
docker-compose up --build
```
 Apply migrations (inside container):

```bash
docker-compose exec web python manage.py migrate
```
 Create superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```
## 5. Start Celery worker:

```bash
docker-compose exec web celery -A subscription_system worker --loglevel=info
```
## 6. Start Celery beat:

```bash
docker-compose exec web celery -A subscription_system beat --loglevel=info
```

## API Endpoints

### Subscription APIs

| Method | Endpoint                             | Description                          |
|--------|--------------------------------------|--------------------------------------|
| POST   | `/api/subscribe/`                    | Subscribe to a plan                  |
| GET    | `/api/subscriptions/`                | List current user's subscriptions    |
| POST   | `/api/cancel/`                       | Cancel current user's subscription   |
| GET    | `/api/exchange-rate/?base=USD&target=BDT` | Get live exchange rate               |

---

## Example Request
## Authentication

This API uses **JWT** configuration.

Include the token in your request headers:

```http
Authorization: Bearer <your_jwt_token>
```
## Example Requests & Responses

### 1. Subscribe to a Plan

**Request:**
```http
POST /api/subscribe/
Authorization: Bearer <your_jwt_token>
Content-Type: application/json
```
```json
{
  "plan_id": 1
}
```
### Response:
```json
{
    "id": 5,
    "plan": {
        "id": 1,
        "name": "Basic Plan",
        "price": "10.00",
        "duration_days": 30
    },
    "start_date": "2025-08-03",
    "end_date": "2025-09-02",
    "status": "active",
    "user": 1
}
```

### 2. List User Subscriptions
**Request:**
```http
GET /api/subscriptions/
Authorization: Bearer <your_jwt_token>
```
### Response:
```json
[
    {
        "id": 1,
        "plan": {
            "id": 1,
            "name": "Basic Plan",
            "price": "10.00",
            "duration_days": 30
        },
        "start_date": "2025-08-03",
        "end_date": "2025-09-02",
        "status": "active",
        "user": 1
    }
    {
        "id": 2,
        "plan": {
            "id": 1,
            "name": "Basic Plan",
            "price": "10.00",
            "duration_days": 30
        },
        "start_date": "2025-08-03",
        "end_date": "2025-09-02",
        "status": "active",
        "user": 1
    }
]
```
### 3. Cancel a Subscription
**Request:**
```http
POST /api/cancel/
Authorization: Bearer <your_jwt_token>
Content-Type: application/json

{
  "subscription_id": 1
}
```
**Response:**
```json
{
  "message": "	Subscription cancelled"
}
```
### 4. Get Live Exchange Rate
**Request:**
```http
GET /api/exchange-rate/?base=USD&target=BDT
Authorization: Bearer <your_jwt_token>
```
**Response:**
```json
{
  "rate": 122.332526
}
```
## Django Admin

Access the Django admin panel at: [http://localhost:8000/admin/](http://localhost:8000/admin/)

**Available Models:**

- **Plan**: Add, Edit, or Delete subscription plans.
- **Subscription**: View and manage user subscriptions.
- **ExchangeRateLog**: View the historical exchange rate logs.

---

## Frontend UI

| Route             | Description                                                 |
|-------------------|-------------------------------------------------------------|
| `/subscriptions/` | View all users and their subscriptions (public, no login)   |

> This interface is rendered using Django’s `render()` function and styled with Bootstrap tables.

---

## Celery Task

A periodic background task that runs **hourly**:

- Fetches the current **USD → BDT** exchange rate.
- Saves the result to the `ExchangeRateLog` model with a timestamp.

---

## Contact

If you encounter any issues running this project, feel free to:
- Contact me at: **[noshinfariaprova@gmail.com]**

---
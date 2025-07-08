# Installation

### 1. Clone the repository

```py
git clone https://github.com/Approachablemember/swida_backend.git
cd ./swida_backend
```

### 2. Create virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

OR

```bash
python -m venv venv
.\venv\Scripts\activate # on Windows
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Run server

```bash
python manage.py runserver
```

# Overview

This Django project serves as the backend API for a Transport Order Management System. It allows creation and listing of transport orders with associated waypoints (pickup or delivery).

## Structure

### orders/models.py

Order: Represents a transport order.

Waypoint: Represents a location point (pickup or delivery) linked to an Order.

orders/serializers.py: Handles data validation and nested creation of orders with waypoints.

### orders/views.py

OrderListCreateAPIView: Handles listing and creation of orders.

WaypointViewSet: (Optional) supports separate management of waypoints.

### orders/urls.py: API route definitions

API Endpoints
POST /api/orders/create/ – Create order with waypoints.

GET /api/orders/ – List all orders with nested waypoints.

# Assumptions & Decisions

Used nested serializers to create orders and their waypoints in one request.

Waypoint types are simplified as 'PU' and 'DL'.

CORS is enabled for http://localhost:5173 to support local Vue frontend for case of this test task.

No authentication or pagination was added to keep it simple.

Basic error handling provided for invalid data
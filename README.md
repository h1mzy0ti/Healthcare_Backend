# 🏥 Patient-Doctor Management API

A Django REST API that allows users to manage patient and doctor records, and map doctors to patients. Authenticated users can register/login using JWT, manage their own patients, view public doctors, and assign mappings.

---

## 📚 Features

- User Registration & Login with JWT Auth
- CRUD operations for Patients (User-specific)
- CRUD operations for Doctors (Public)
- Map doctors to patients
- PostgreSQL as the database
- Django ORM for database interaction
- Authentication using JWT with djangorestframework-simplejwt
- Secure patient and doctor-related endpoints with authentication permissions

---

## 🛠 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SimpleJWT
- PostgreSQL
- Docker (optional)

---

Postman Documentation = https://documenter.getpostman.com/view/37555239/2sB34oBGwF

---
## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/patient-doctor-api.git
cd patient-doctor-api
```

### 2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure PostgreSQL database (example in .env.example`)
```env
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

---

## 🔐 Authentication

Use JWT tokens for protected routes.

- Register: `POST /api/auth/register/`
- Login: `POST /api/auth/login/`

Token will be returned on login. Use it as:
```
Authorization: Bearer <your_token> in Postman or any API testing tool
```

---

## 📬 API Endpoints

### 🔑 Auth APIs
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Log in and get JWT token |

### 👤 Patient APIs
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/patients/` | Create new patient (auth required) |
| GET | `/api/patients/` | Get all your patients |
| GET | `/api/patients/<id>/` | Get specific patient |
| PUT | `/api/patients/<id>/` | Update patient |
| DELETE | `/api/patients/<id>/` | Delete patient |

### 👨‍⚕️ Doctor APIs
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/doctors/` | Add a doctor (auth required) |
| GET | `/api/doctors/` | List all doctors |
| GET | `/api/doctors/<id>/` | Get specific doctor |
| PUT | `/api/doctors/<id>/` | Update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

### 🔁 Patient-Doctor Mapping
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/mappings/` | Assign doctor to patient |
| GET | `/api/mappings/` | List all mappings |
| GET | `/api/mappings/<patient_id>/` | Doctors assigned to a patient |
| DELETE | `/api/mappings/<id>/` | Remove mapping |

---

## 🧪 Sample Requests

### Register
```json
POST /api/auth/register/
{
  "name": "Alice",
  "email": "alice@gmail.com",
  "password": "qwertY123"
}
```

### Login
```json
POST /api/auth/login/
{
  "email": "alice@gmail.com",
  "password": "qwertY123"
}
```

### Add Patient
```json
POST /api/patients/
Authorization: Bearer <token>
{
  "name": "Shree R",
  "age": 36,
  "gender": "Male",
  "medical_history": "Hypertension"
}
```

---

## 🚧 Future Improvements

- Role-based access control (Admin, Doctor, Patient)
- Advanced filtering and pagination
- Swagger/OpenAPI docs
- Docker support for easy deployment

---

## 📝 License

MIT License
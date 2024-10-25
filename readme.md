# README.md
# Django + Vue.js Multiplication App

A simple full-stack application with Django REST Framework backend and Vue.js frontend that performs multiplication of two numbers.

## Project Structure
```
DjangoVueTest/
├── backend/              # Django REST Framework backend
│   ├── api/             # API app
│   └── multiplication/  # Django project settings
└── frontend/            # Vue.js frontend
```

## Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn

## Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install django djangorestframework django-cors-headers
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

The backend will be available at http://localhost:8000

## Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

## API Endpoints

### Multiply Numbers
- URL: `http://localhost:8000/api/multiply/`
- Method: `POST`
- Data Params:
  ```json
  {
    "value1": number,
    "value2": number
  }
  ```
- Success Response:
  ```json
  {
    "result": number
  }
  ```

## Local Development

To run the complete application locally:

1. Start the backend server:
```bash
cd backend
source venv/bin/activate  # On macOS/Linux
python manage.py runserver
```

2. In a new terminal, start the frontend development server:
```bash
cd frontend
npm run dev
```

3. Open http://localhost:3000 in your browser
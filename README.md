# Smart Waste Management System

A comprehensive web application for managing waste collection and reporting illegal dumping activities.

## Features

- User Authentication and Authorization
- Dashboard with Waste Collection Statistics
- Bin Management System
- Route Planning for Waste Collection
- Illegal Dumping Reporting System
- Report Management and Tracking

## Technology Stack

- Python 3.x
- Django 5.2
- Bootstrap 5
- PostgreSQL (Production) / SQLite (Development)
- Crispy Forms with Bootstrap 5
- Django Tables2
- Django Filter
- WhiteNoise for Static Files

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/Minari4/Smart_Waste_Management_App.git
cd smart-waste-management
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Navigate to the project directory:
```bash
cd waste_management
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Deployment

This application is configured for deployment on Render.com. The following files are included for deployment:
- `build.sh` - Build script for Render
- `requirements.txt` - Python dependencies
- Production-ready settings in `settings.py`

## Environment Variables

The following environment variables should be set in production:
- `DEBUG`: Set to 'False' in production
- `SECRET_KEY`: Django secret key
- `DATABASE_URL`: PostgreSQL database URL (automatically set by Render)

## License

MIT License 
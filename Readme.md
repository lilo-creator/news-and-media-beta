# News and Media Portal

A Django web application for sharing news, sports updates, and event information.

## Features

- Responsive design using Bootstrap 5
- Different sections for News, Sports, and Events
- Feature details page for each item
- Admin interface for managing content
- Custom styled UI

## Templates

The application uses the following templates:

- **base.html**: The main template that serves as the foundation for all pages
- **Home/home.html**: The landing page showing all active features by section
- **Home/feature_detail.html**: Detailed view for a specific feature
- **404.html**: Custom 404 error page
- **500.html**: Custom 500 error page

## Models

The main model is `LandingFeature` which stores content for the landing page:

- Title and description
- Optional image and link
- Section (News, Sports, or Events)
- Priority for ordering
- Active status

## Running the Project

1. Install dependencies: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Create a superuser: `python manage.py createsuperuser`
4. Run the development server: `python manage.py runserver`
5. Access the admin at: `http://127.0.0.1:8000/admin/`
6. Access the homepage at: `http://127.0.0.1:8000/`

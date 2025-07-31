# News and Media Portal

A Django web application for sharing news, sports updates, and event information.

## Features

- Responsive design using Bootstrap 5
- Different sections for News, Sports, and Events
- Feature details page for each item
- Admin interface for managing content

## Deployment on Railway

This project is configured for deployment on Railway.

### Prerequisites

- A Railway account
- Railway CLI (optional for local deployment)

### Deploying to Railway

1. Fork or clone this repository
2. Connect your GitHub repository to Railway
3. Railway will automatically detect the configuration in `railway.json`
4. Set the required environment variables in the Railway dashboard:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: Set to 'False' for production
   - `ALLOWED_HOSTS`: Your Railway domain and any other domains
   - `CSRF_TRUSTED_ORIGINS`: Your Railway domain and any other domains (with https:// prefix)
   - `DATABASE_URL`: Will be automatically set by Railway if you add a PostgreSQL database

### Local Development Build

Run the build script:

```bash
# On Linux/Mac
chmod +x build.sh
./build.sh

# On Windows
build.bat
```

### Manual Deployment

If you want to deploy manually:

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Link your project
railway link

# Deploy your app
railway up
```

## UI Features

- Custom styled UI
- Enhanced Events section with:
  - Modern UI elements and animations
  - Social sharing capabilities for all events
  - SEO optimization with meta tags and sitemaps
  - Structured data with JSON-LD for improved search visibility
  - Interactive countdown timers for upcoming events
  - Reusable component architecture
  - Adaptive layouts for mobile and desktop
  - Google Calendar integration

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
7. Access the events page at: `http://127.0.0.1:8000/events/`

## Deployment

The application is ready for deployment with:

- Configured allowed hosts for external access
- SEO-optimized content with meta tags
- XML sitemap for search engine indexing
- Social sharing capabilities for better reach
- Structured data with JSON-LD for improved search visibility

When deploying:

1. Set `DEBUG = False` in production
2. Update `ALLOWED_HOSTS` with your domain name
3. Configure a proper database backend (PostgreSQL recommended)
4. Set up static files serving with a CDN or web server
5. Ensure all static files are collected: `python manage.py collectstatic`
6. Set up proper HTTPS to ensure social sharing works correctly
7. Register your sitemap with search engines: `https://yourdomain.com/events/sitemap.xml`

## Enhanced Events Module

The Events section has been fully enhanced with modern UI and features:

1. **Visual Improvements:**
   - Responsive design with modern UI elements
   - Animated elements using animate.css
   - Interactive countdown timers for upcoming events

2. **SEO & Discoverability:**
   - Proper meta tags for SEO
   - JSON-LD structured data for rich search results
   - XML sitemap for search engine indexing
   - Social sharing capabilities

3. **User Experience:**
   - Filter sidebar for easy event navigation
   - Reusable component architecture
   - Improved registration flow
   - Google Calendar integration

For detailed documentation on the Events module enhancements, see the [Events Enhancement Documentation](Events/EVENTS_ENHANCEMENT_DOCS.md).

## Troubleshooting

### CSRF Verification Failed

If you encounter a CSRF verification error with a message like "Origin checking failed":

1. Ensure your domain is added to the `CSRF_TRUSTED_ORIGINS` list in settings.py or as an environment variable
2. Make sure you're using `https://` prefixes for all domains in the CSRF_TRUSTED_ORIGINS list
3. Verify that your forms include the `{% csrf_token %}` template tag
4. If using AJAX requests, ensure proper CSRF headers are being sent

### Database Connection Issues

If you have trouble connecting to the database:

1. Verify the `DATABASE_URL` environment variable is correctly set in Railway
2. Check that the PostgreSQL instance is properly provisioned and running
3. Ensure your IP is allowed if there are any connection restrictions

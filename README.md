# Navigator Assist - Mobile-First CRM Application

A modern, fully functional mobile-responsive CRM (Customer Relationship Management) application built with Django. Perfect for managing clients, tasks, deals, and products on the go.

## Features

### Core Modules
- **Clients** - Manage customer information, emails, phones, companies
- **Tasks** - Track work items with priority levels and due dates
- **Deals** - Monitor sales pipeline with stage tracking
- **Products** - Catalog and pricing management
- **Dashboard** - Real-time statistics and overview

### Functionality
✅ Full CRUD Operations (Create, Read, Update, Delete)
✅ Mobile-First Responsive Design
✅ CSV Data Export/Download
✅ Form Validation & Error Handling
✅ SQLite Database with Migrations
✅ Clean, Intuitive Navigation

## Technology Stack

- **Backend**: Django 5.1.5
- **Database**: SQLite
- **Frontend**: HTML5, CSS3 (Mobile-responsive)
- **Python**: 3.13+

## Installation

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/Ashwanthpv/navi.git
cd navi
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Start development server**
```bash
python manage.py runserver
```

Access the app at: `http://127.0.0.1:8000/`

## Deployment (Heroku/PaaS)

### Prepare for hosting:

1. **Install production requirements**
```bash
pip install -r requirements.txt
pip install gunicorn whitenoise
```

2. **Collect static files**
```bash
python manage.py collectstatic --noinput
```

3. **Create .env file** (for production)
```
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=your-secret-key-here
```

4. **Deploy using Procfile** (included for Heroku/PaaS)

### Environment Variables Required:
- `DEBUG` - Set to False in production
- `ALLOWED_HOSTS` - Your domain
- `SECRET_KEY` - Django secret key

## Project Structure

```
navcrm/
├── manage.py              # Django management
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment config
├── db.sqlite3            # SQLite database
│
├── navcrm/               # Main project config
│   ├── settings.py       # Django settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI app
│
├── clients/             # Clients app
├── tasks/              # Tasks app
├── deals/              # Deals app
├── products/           # Products app
├── reports/            # Dashboard/Reports
│
└── templates/          # Mobile-responsive templates
    ├── base.html       # Base template
    ├── dashboard_mobile.html
    ├── clients/
    ├── tasks/
    ├── deals/
    └── products/
```

## API Endpoints

### Clients
- `GET /clients/` - List all clients
- `GET /clients/add/` - Add client form
- `POST /clients/add/` - Save new client
- `GET /clients/edit/<id>/` - Edit client
- `GET /clients/delete/<id>/` - Delete client
- `GET /clients/download/` - Export as CSV

### Tasks
- `GET /tasks/` - List all tasks
- `GET /tasks/add/` - Add task form
- `POST /tasks/add/` - Save new task
- `GET /tasks/edit/<id>/` - Edit task
- `GET /tasks/delete/<id>/` - Delete task
- `GET /tasks/download/` - Export as CSV

### Deals
- `GET /deals/` - List all deals
- `GET /deals/add/` - Add deal form
- `POST /deals/add/` - Save new deal
- `GET /deals/edit/<id>/` - Edit deal
- `GET /deals/delete/<id>/` - Delete deal
- `GET /deals/download/` - Export as CSV

### Products
- `GET /products/` - List all products
- `GET /products/add/` - Add product form
- `POST /products/add/` - Save new product
- `GET /products/edit/<id>/` - Edit product
- `GET /products/delete/<id>/` - Delete product
- `GET /products/download/` - Export as CSV

## Features by Module

### Dashboard
- Real-time statistics for all modules
- Quick access to all CRM functions
- Mobile-optimized navigation

### Data Management
- Add new records with validation
- Edit existing records
- Delete with confirmation
- Export data as CSV files

### Mobile Optimization
- Responsive design for all devices
- Touch-friendly buttons and forms
- Optimized for mobile browsers
- Fast loading times

## Admin Panel

Access Django admin at `/admin/`:
```bash
python manage.py createsuperuser
```

## Support & Issues

For issues or feature requests, please visit: https://github.com/Ashwanthpv/navi/issues

## License

MIT License - Feel free to use and modify

## Author

Developed by Ashwanth PV  
GitHub: https://github.com/Ashwanthpv

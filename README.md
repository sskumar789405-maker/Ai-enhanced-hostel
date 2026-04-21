# 🏢 Hostel Management System

A modern, full-featured hostel/PG management system built with Django 6.0.4 and Python 3.11+

## ✨ Features

### 📋 Core Management
- **Room Management** - Add, edit, and manage hostel rooms
- **Student Profiles** - Track student information and room assignments
- **Fee Management** - Payment tracking and billing
- **Complaint System** - Issue reporting and resolution tracking
- **Maintenance Requests** - Room maintenance and repair tracking
- **Announcements** - Hostel-wide announcements and notifications

### 📅 Daily Operations (New!)
- **Daily Attendance** - Check-in/Check-out tracking
- **Leave Requests** - Student leave application & approval system
- **Guest Passes** - Visitor management and tracking
- **Meal Bookings** - Daily meal planning with dietary preferences
- **Daily Tasks** - Task assignment and completion tracking
- **Emergency Contacts** - Quick access to emergency numbers
- **Daily Expenses** - Track daily shared expenses by category

### 🎨 Design Features
- Modern Glassmorphism UI with gradient backgrounds
- Fully responsive mobile-friendly design
- Light theme with purple gradients
- Font Awesome icons (6.4.0)
- Bootstrap 5.3.0 framework
- 80+ CSS animations and transitions
- Professional color scheme

## 🛠️ Tech Stack

- **Backend**: Django 6.0.4
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite3
- **Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.4.0
- **Server**: Gunicorn (production)

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hostel-management.git
cd hostel-management
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
cd hostel_pg_system
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Collect static files:
```bash
python manage.py collectstatic --noinput
```

7. Run development server:
```bash
python manage.py runserver
```

Visit `http://localhost:8000/` in your browser.

## 🚀 Deployment

### Deploy to PythonAnywhere

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

**Quick Summary:**
1. Create PythonAnywhere account (free tier available)
2. Upload code via Git or ZIP
3. Create virtual environment
4. Configure web app and static files
5. Run migrations and create superuser
6. Reload and go live!

### Deploy to Other Platforms

**Heroku**: [Heroku Deployment Guide](https://devcenter.heroku.com/articles/getting-started-with-django)

**AWS EC2**: [AWS Django Deployment](https://aws.amazon.com/getting-started/hands-on/deploy-python-application/)

**DigitalOcean**: [DigitalOcean App Platform](https://docs.digitalocean.com/products/app-platform/)

## 📊 Database Models

### Core Models
- **Room** - Room details, capacity, availability
- **StudentProfile** - Student information and room assignments
- **Fee** - Payment tracking and due dates
- **Complaint** - Issue reporting and tracking
- **Maintenance** - Maintenance request management
- **Announcement** - Hostel announcements

### Daily Operations Models
- **DailyAttendance** - Check-in/checkout records
- **LeaveRequest** - Leave applications and approvals
- **GuestPass** - Visitor registration and tracking
- **MealBooking** - Meal reservations with dietary info
- **DailyTask** - Task assignments and completion
- **DailyExpense** - Shared expense tracking
- **EmergencyContact** - Emergency contact directory

## 👥 User Roles

### Admin/Staff
- Full access to all management features
- Approve/reject leave and guest requests
- Create announcements
- Track attendance and expenses
- View analytics and reports

### Students
- View their profile and room details
- Submit complaints and maintenance requests
- Check fee status and payments
- Request leave and guest passes
- Book meals
- Track assigned tasks
- View emergency contacts

## 🔐 Security Features

- CSRF Protection
- Secure session management
- Password hashing
- User authentication
- Role-based access control
- SSL/HTTPS ready for production

## 📝 API & Views

### Student Views
- Dashboard: `/dashboard/`
- Attendance: `/attendance/`
- Leave: `/leave/` and `/leave/create/`
- Guests: `/guests/` and `/guests/create/`
- Meals: `/meals/` and `/meals/create/`
- Tasks: `/tasks/`
- Emergency: `/emergency/`
- Fees: `/fees/`
- Complaints: `/complaints/`
- Profile: `/profile/`

### Admin Views
- Dashboard: `/dashboard/`
- Students: `/staff/students/`
- Complaints: `/staff/complaints/`
- Maintenance: `/staff/maintenance/`
- Fees: `/staff/fees/`
- Announcements: `/staff/announcements/`
- Expenses: `/staff/expenses/`

## 📱 Responsive Design

Works perfectly on:
- Desktop (1920px+)
- Tablet (768px - 1024px)
- Mobile (320px - 768px)

## 🎯 Future Enhancements

- [ ] Online payment integration (Razorpay, Stripe)
- [ ] SMS notifications
- [ ] Mobile app (iOS/Android)
- [ ] Advanced analytics dashboard
- [ ] Document upload system
- [ ] Staff scheduling system
- [ ] Visitor log printing
- [ ] Export reports to PDF/Excel

## 🐛 Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic --noinput
```

### Database errors
```bash
python manage.py migrate
```

### Permission issues
```bash
chmod -R 755 hostel_pg_system/
```

## 📞 Support

- **Django Documentation**: https://docs.djangoproject.com/
- **PythonAnywhere Help**: https://help.pythonanywhere.com/
- **Bootstrap Documentation**: https://getbootstrap.com/docs/5.0/

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Contributors

- Developed for hostel management automation
- Built with ❤️ using Django

---

## 🎉 Getting Started

1. Read this README
2. Follow installation instructions
3. Check DEPLOYMENT_GUIDE.md for cloud deployment
4. Start managing your hostel!

**Questions?** Create an issue on GitHub or check the documentation.

---

**Happy Hostel Management! 🏢**

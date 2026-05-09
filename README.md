# 🗂️ Dynamic Portfolio — Django-Powered Personal Portfolio Platform

A modern, fully dynamic, and admin-controlled personal portfolio web application built with Django. Designed for developers, students, and professionals who want to showcase their work through a clean, responsive, and always up-to-date portfolio — without ever touching the frontend code.

---

## 📖 About

**Dynamic Portfolio** eliminates the hassle of maintaining a static portfolio website. All content — skills, projects, education, experience, achievements, certificates, and social profiles — is managed through a secure admin backend and rendered dynamically on the frontend in real time.

The standout feature of this project is its **automatic resume generation system**. Instead of uploading and manually updating a separate resume file, the resume is generated directly from your portfolio data. This ensures your portfolio and resume are always perfectly in sync — update once, reflect everywhere.

---

## ✨ Features

- 🔄 **Fully Dynamic Portfolio** — All content managed via admin panel, no frontend code changes needed
- 📄 **Automatic Resume Generation** — Resume is auto-generated from portfolio data; no manual upload or update required
- 🎨 **Responsive Modern UI** — Clean, professional design that works across all devices
- ⚡ **Real-Time Content Rendering** — Changes made in admin are instantly reflected on the portfolio
- 🔧 **Admin-Controlled Content Management** — Secure login-based panel to manage all sections
- 🖼️ **Media Upload Functionality** — Upload profile photos, project images, logos, and more
- 📬 **Contact Form with Email Notifications** — Visitors can reach out; emails sent to admin and auto-reply sent to sender *(optional, see setup)*

---

## 📋 Portfolio Sections

| Section | Description |
|---|---|
| Profile | Name, title, bio, photo, social links |
| About | Personal summary and key highlights |
| Skills | Categorized technical skills |
| Projects | Project showcase with tech stack and images |
| Experience | Work experience with roles and durations |
| Education | Academic background |
| Achievements | Awards and notable accomplishments |
| Certificates | Professional certifications |
| Contact | Contact form with email integration |
| Resume | Auto-generated resume from all portfolio data |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.x, Python 3.11 |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite (default) |
| Image Handling | Pillow |
| Email | Django Email (SMTP) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repo-url>
cd dynamic-portfolio
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate        # Windows
# source venv/bin/activate     # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install django
python.exe -m pip install --upgrade pip
python -m pip install Pillow
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔑 Admin Access

To access the admin panel, click the **logo in the navbar**.

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `admin123` |

From the admin panel you can manage every section of the portfolio — profile, skills, projects, education, experience, achievements, certificates, and more.

---

## 📬 Email Notification System (Optional)

The platform includes an email system for the contact form that:
- Notifies the **admin** when a visitor submits the contact form
- Sends an **auto-reply** to the visitor confirming their message was received

> ⚠️ **Email credentials are intentionally hidden for privacy.** The email system is disabled by default and must be configured manually.

### Step 1 — Set Email Credentials

Open `portfolio/settings.py` and fill in your Gmail (or SMTP) credentials:

```python
EMAIL_HOST_USER = 'youremail@example.com'
EMAIL_HOST_PASSWORD = '**** **** **** ****'  # Use an App Password, not your regular password
```

> 💡 For Gmail, generate an **App Password** from your Google Account → Security → 2-Step Verification → App Passwords.

### Step 2 — Uncomment Email Calls in Views

#### `home/views.py` — Lines 470 & 471

Uncomment the following lines to activate email sending on contact form submission:

```python
contact_mail(name, email, subject, message, full_name)
auto_reply_mail(name, email, subject, message, full_name)
```

> ℹ️ If email credentials are not configured, the portfolio and all other features will continue to work normally — only the contact form emails will be skipped.

---

## 📁 Project Structure

```
dynamic-portfolio/
├── home/               # Core portfolio views, models, and URLs
├── accounts/           # Admin authentication and profile management
├── base/               # Shared utilities (email helpers, base models)
├── portfolio/          # Project settings and URL configuration
├── templates/
│   ├── base/           # Shared layout, header, footer, forms
│   └── home/           # Portfolio homepage and auto-generated resume
├── public/
│   ├── static/         # CSS, JS, and static assets
│   └── media/          # Uploaded images, logos, and resume files
├── manage.py
└── requirements.txt
```

---

## 📄 Auto-Generated Resume

One of the most powerful features of this project is that **no resume file needs to be manually created or uploaded**. The system compiles all portfolio data — skills, education, experience, projects, achievements, and certificates — and renders a formatted resume page (`/resume/`) that can be printed or saved as a PDF directly from the browser.

This guarantees that your resume is **always in sync** with your latest portfolio content.

---

## ⚙️ Configuration Notes

- **Database** — SQLite is used by default. Can be switched to PostgreSQL in `portfolio/settings.py`.
- **Media Files** — Uploaded files (profile images, project screenshots, logos) are stored under `public/media/`.
- **Static Files** — CSS and JS assets are located under `public/static/`.

---

## 🌐 Browser Support

| Browser | Supported |
|---|---|
| Google Chrome | ✅ |
| Mozilla Firefox | ✅ |
| Microsoft Edge | ✅ |

---

## 📄 License

This project is open source and intended for personal and educational use. Feel free to fork, customize, and deploy your own version.

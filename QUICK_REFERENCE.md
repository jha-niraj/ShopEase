# 🚀 RushX Quick Reference Card

## Admin Commands

### Create Superuser (Admin Account)
```bash
python3 manage.py createsuperuser
```

### Run Development Server
```bash
python3 manage.py runserver
```

### Apply Database Migrations
```bash
python3 manage.py migrate
```

### Create New Migrations (after model changes)
```bash
python3 manage.py makemigrations
```

---

## Important URLs

| Page | URL | Description |
|------|-----|-------------|
| Homepage | `http://127.0.0.1:8000/` | Main landing page |
| Admin Panel | `http://127.0.0.1:8000/admin/` | Add/manage products |
| Login | `http://127.0.0.1:8000/login/` | User login |
| Sign Up | `http://127.0.0.1:8000/signup/` | Create account |
| Profile | `http://127.0.0.1:8000/profile/` | User profile (requires login) |
| Shop | `http://127.0.0.1:8000/shop/` | All products |
| Cart | `http://127.0.0.1:8000/cart/` | Shopping cart |
| Contact | `http://127.0.0.1:8000/contact/` | Contact form |

---

## Category URLs

| Category | URL |
|----------|-----|
| Web Applications | `http://127.0.0.1:8000/WebApplications/` |
| Desktop Applications | `http://127.0.0.1:8000/GraphicalApplications/` |
| Console Applications | `http://127.0.0.1:8000/ConsoleApplications/` |

---

## Adding Products (Admin Panel)

1. Go to `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials
3. Click **"Products"** → **"Add Product +"**
4. Fill required fields:
   - **Product Name**: e.g., "Django CMS Pro"
   - **Cateogary**: Choose from dropdown
     - `Web Applications`
     - `Graphical Applications`
     - `Console Applications`
   - **Price**: e.g., 4999 (in rupees)
   - **Description**: Product details
   - **Pub date**: Click calendar to select
   - **Image**: Upload product image (JPG/PNG)
   - **Link To Download**: Download URL
5. Click **"Save"**

---

## Product Categories

Use these exact values for the **Cateogary** field:

✅ `Web Applications` - For web-based software
✅ `Graphical Applications` - For desktop GUI apps
✅ `Console Applications` - For CLI tools

---

## User Features

### For Guests (Not Logged In)
- ✅ Browse products
- ✅ View categories
- ✅ Search products
- ✅ View product details
- ✅ Add to cart (stored in browser)
- ✅ Sign up for account
- ✅ Contact support

### For Logged-In Users
- ✅ All guest features +
- ✅ View/edit profile
- ✅ Change password
- ✅ Place orders
- ✅ View order history
- ✅ Persistent cart across devices

---

## Profile Page Features

Access: Click username → "My Profile" (or `/profile/`)

**Can Edit:**
- First Name
- Last Name
- Username (must be unique)
- Email Address
- Password (requires current password)

**View:**
- Member since date
- Last login timestamp
- User avatar (auto-generated)

---

## File Structure

```
finalproject/
├── manage.py
├── db.sqlite3
├── ADMIN_GUIDE.md          # Detailed admin instructions
├── UPDATE_SUMMARY.md       # Complete update documentation
├── QUICK_REFERENCE.md      # This file
├── setup.sh               # Quick setup script
├── icommerce/
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   ├── templates/
│   │   ├── basic.html     # Base template with nav
│   │   ├── index.html     # Homepage
│   │   ├── login.html     # Login page
│   │   ├── signup.html    # Signup page
│   │   ├── profile.html   # User profile
│   │   ├── contact.html   # Contact page
│   │   ├── shop.html      # Product listing
│   │   └── ...
│   └── static/            # CSS, JS, images
└── media/                 # Uploaded product images
    └── icommerce/
        └── images/
```

---

## Common Issues & Solutions

### Issue: Can't access admin panel
**Solution:** Create superuser first
```bash
python3 manage.py createsuperuser
```

### Issue: Images not showing
**Solution:** Check media directory permissions
```bash
mkdir -p media/icommerce/images
chmod -R 755 media/
```

### Issue: Database errors
**Solution:** Run migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Issue: Homepage shows mock products
**Solution:** Add real products from admin panel

### Issue: Contact form emails not sending
**Solution:** Email is optional by default. To enable:
1. Set environment variables: `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`
2. Or edit `views.py` and set `send_email = True`

---

## Quick Setup (New Installation)

Run the setup script:
```bash
./setup.sh
```

Or manually:
```bash
# 1. Create superuser
python3 manage.py createsuperuser

# 2. Run migrations
python3 manage.py migrate

# 3. Start server
python3 manage.py runserver

# 4. Access admin: http://127.0.0.1:8000/admin/
# 5. Add products
# 6. View site: http://127.0.0.1:8000/
```

---

## Sample Product Data

**Product 1:**
- Name: Django E-Commerce Platform
- Category: Web Applications
- Price: 4999
- Description: Complete e-commerce solution with cart, checkout, and admin

**Product 2:**
- Name: Python Photo Editor Pro
- Category: Graphical Applications
- Price: 2999
- Description: Professional image editing with filters and effects

**Product 3:**
- Name: Developer Tools Suite
- Category: Console Applications
- Price: 1999
- Description: Essential CLI tools for developers

---

## Testing User Accounts

### Test Admin Account
```
Username: admin
Password: [your choice]
```

### Test User Account
```
Username: testuser
Password: [your choice]
```

Create via signup page: `http://127.0.0.1:8000/signup/`

---

## Design Colors

- **Primary Purple**: `#667eea` → `#764ba2`
- **Secondary Pink**: `#f093fb` → `#f5576c`
- **Accent Blue**: `#4facfe` → `#00f2fe`
- **Background**: `#f8f9fa`
- **Text Dark**: `#333333`
- **Text Medium**: `#666666`
- **Text Light**: `#999999`

---

## Need Help?

1. 📖 Read `ADMIN_GUIDE.md` for detailed admin instructions
2. 📋 Check `UPDATE_SUMMARY.md` for all features and changes
3. 🐛 Check "Common Issues & Solutions" section above
4. 💬 Use contact form to report issues

---

**Version:** 2.0  
**Last Updated:** November 3, 2025  
**Developers:** Dharmendra Sah & Niraj Jha

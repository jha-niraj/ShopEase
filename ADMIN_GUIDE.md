# RushX Admin Guide

## How to Add Products from Admin Panel

### Step 1: Create a Superuser (Admin Account)

Run the following command in your terminal:

```bash
cd /home/niraj/Documents/7thsemester/finalproject
python3 manage.py createsuperuser
```

You'll be prompted to enter:
- **Username**: Choose an admin username (e.g., `admin`)
- **Email address**: Your email (can be left blank by pressing Enter)
- **Password**: Choose a strong password (you won't see it while typing)
- **Password (again)**: Confirm your password

Example:
```
Username: admin
Email address: admin@rushx.com
Password: ********
Password (again): ********
Superuser created successfully.
```

### Step 2: Start the Development Server

```bash
python3 manage.py runserver
```

### Step 3: Access the Admin Panel

1. Open your browser and go to: `http://127.0.0.1:8000/admin/`
2. Login with the superuser credentials you just created

### Step 4: Add Products

1. **Click on "Products"** in the admin panel
2. **Click "Add Product +"** button (top right)
3. **Fill in the product details**:
   
   - **Product Name**: Name of the software (e.g., "Django E-Commerce Pro")
   - **Cateogary**: Choose from:
     - `Web Applications`
     - `Graphical Applications`
     - `Console Applications`
   - **Price**: Enter price in rupees (e.g., 4999)
   - **Description**: Detailed description of the product
   - **Pub date**: Publication date (click calendar icon to select)
   - **Image**: Click "Choose File" to upload product image
     - Recommended size: 800x600px or higher
     - Format: JPG, PNG
   - **Link To Download**: URL where the product can be downloaded after purchase

4. **Click "Save"** to add the product

### Step 5: View Your Products

- Go to `http://127.0.0.1:8000/` to see your products on the homepage
- Products will automatically appear in the appropriate category pages

---

## Sample Product Data for Testing

Here are some example products you can add:

### Product 1: Django E-Commerce Platform
- **Product Name**: Django E-Commerce Platform
- **Cateogary**: Web Applications
- **Price**: 4999
- **Description**: A complete e-commerce solution built with Django. Features include user authentication, shopping cart, checkout system, and admin panel.
- **Link To Download**: https://github.com/yourusername/django-ecommerce

### Product 2: Python Photo Editor
- **Product Name**: Python Photo Editor Pro
- **Cateogary**: Graphical Applications
- **Price**: 2999
- **Description**: Professional image editing software with filters, effects, and batch processing capabilities.
- **Link To Download**: https://github.com/yourusername/photo-editor

### Product 3: CLI Dev Tools
- **Product Name**: Developer Tools Suite
- **Cateogary**: Console Applications
- **Price**: 1999
- **Description**: Essential command-line tools for developers including file managers, code analyzers, and productivity utilities.
- **Link To Download**: https://github.com/yourusername/dev-tools

---

## Managing Products

### Edit a Product
1. Go to Admin Panel → Products
2. Click on the product name you want to edit
3. Make your changes
4. Click "Save"

### Delete a Product
1. Go to Admin Panel → Products
2. Select the checkbox next to the product(s) you want to delete
3. Select "Delete selected products" from the Action dropdown
4. Click "Go"
5. Confirm deletion

### View Orders
1. Go to Admin Panel → Orders
2. You can see all customer orders with their details

### View Contact Messages
1. Go to Admin Panel → Contacts
2. View all customer inquiries and messages

---

## Quick Commands Reference

```bash
# Create superuser
python3 manage.py createsuperuser

# Start development server
python3 manage.py runserver

# Make migrations (after model changes)
python3 manage.py makemigrations

# Apply migrations
python3 manage.py migrate

# Collect static files (for production)
python3 manage.py collectstatic
```

---

## Troubleshooting

### Can't upload images?
Make sure the `media` directory exists and has proper permissions:
```bash
mkdir -p media/icommerce/images
chmod -R 755 media/
```

### Database errors?
Run migrations:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Admin panel not styled?
Clear your browser cache or use incognito mode.

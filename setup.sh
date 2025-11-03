#!/bin/bash

# RushX Quick Start Script
# This script helps you get started with the RushX e-commerce platform

echo "========================================="
echo "  RushX E-Commerce Platform Setup"
echo "========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: manage.py not found!"
    echo "Please run this script from the project root directory."
    exit 1
fi

echo "✓ Project directory found"
echo ""

# Check if superuser exists
echo "📝 Step 1: Creating Admin Account"
echo "--------------------------------------"
echo "You'll be prompted to create a superuser account."
echo "This account will be used to access the admin panel."
echo ""

python3 manage.py createsuperuser

if [ $? -eq 0 ]; then
    echo "✓ Superuser created successfully!"
else
    echo "ℹ️  Superuser may already exist or creation was cancelled."
fi

echo ""
echo "📦 Step 2: Running Database Migrations"
echo "--------------------------------------"
python3 manage.py migrate

if [ $? -eq 0 ]; then
    echo "✓ Database migrations completed!"
else
    echo "❌ Migration failed!"
    exit 1
fi

echo ""
echo "========================================="
echo "  Setup Complete! 🎉"
echo "========================================="
echo ""
echo "📚 What's Next?"
echo ""
echo "1. Start the development server:"
echo "   python3 manage.py runserver"
echo ""
echo "2. Access the website:"
echo "   Homepage: http://127.0.0.1:8000/"
echo "   Admin Panel: http://127.0.0.1:8000/admin/"
echo ""
echo "3. Add products from the admin panel"
echo "   - Login with your superuser credentials"
echo "   - Click 'Products' → 'Add Product +'"
echo "   - Fill in the details and save"
echo ""
echo "4. Read the documentation:"
echo "   - Admin Guide: ADMIN_GUIDE.md"
echo "   - Update Summary: UPDATE_SUMMARY.md"
echo ""
echo "========================================="
echo "  Happy Coding! 💻"
echo "========================================="

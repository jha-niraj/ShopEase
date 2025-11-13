#!/usr/bin/env python3
"""
Script to mark all existing products as approved
This is a one-time migration script after adding approval feature
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imac.settings')
django.setup()

from icommerce.models import Product
from django.utils import timezone

def approve_all_products():
    """Mark all existing products as approved"""
    print("=" * 60)
    print("📋 Approving All Existing Products")
    print("=" * 60)
    print()
    
    # Get all products that are not approved
    unapproved_products = Product.objects.filter(is_approved=False)
    count = unapproved_products.count()
    
    if count == 0:
        print("✅ All products are already approved!")
        return
    
    print(f"Found {count} unapproved product(s)")
    print()
    
    # Approve all products
    for product in unapproved_products:
        product.is_approved = True
        product.approved_date = timezone.now()
        product.save()
        print(f"✅ Approved: {product.Product_Name}")
    
    print()
    print("=" * 60)
    print(f"✅ Successfully approved {count} product(s)!")
    print("=" * 60)
    
    # Show summary
    total_products = Product.objects.count()
    approved_products = Product.objects.filter(is_approved=True).count()
    
    print()
    print(f"📊 Summary:")
    print(f"   Total products: {total_products}")
    print(f"   Approved: {approved_products}")
    print(f"   Pending: {total_products - approved_products}")
    print()

if __name__ == "__main__":
    try:
        approve_all_products()
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please ensure:")
        print("1. Django server is not running")
        print("2. Database is accessible")
        print("3. You're in the correct directory")

#!/usr/bin/env python3
"""
Quick script to view and update product categories
Run this when Django server is NOT running
"""

import os
import sys

# Disable auto-reload
os.environ['DJANGO_SETTINGS_MODULE'] = 'imac.settings'

import django
django.setup()

from icommerce.models import Product

def main():
    products = Product.objects.all()
    
    print("\n" + "=" * 80)
    print("📦 CURRENT PRODUCTS IN DATABASE")
    print("=" * 80 + "\n")
    
    if products.count() == 0:
        print("No products found.\n")
        return
    
    for p in products:
        print(f"ID: {p.id}")
        print(f"Name: {p.Product_Name}")
        print(f"Category (DB): {p.Cateogary}")
        
        # Show display name
        if p.Cateogary == 'Web Applications':
            display = '🏺 Pottery & Ceramics'
        elif p.Cateogary == 'Graphical Applications':
            display = '💍 Jewelry & Accessories'
        elif p.Cateogary == 'Console Applications':
            display = '🧵 Textiles & Fabrics'
        else:
            display = p.Cateogary
        
        print(f"Category (Display): {display}")
        print(f"Price: ₹{p.Price}")
        print(f"Approved: {'Yes' if p.is_approved else 'No'}")
        print(f"Seller: {p.seller.username if p.seller else 'Admin'}")
        print(f"Description: {p.Description[:100]}...")
        print("-" * 80)
    
    print(f"\nTotal: {products.count()} products\n")
    
    # Category distribution
    pottery = products.filter(Cateogary='Web Applications').count()
    jewelry = products.filter(Cateogary='Graphical Applications').count()
    textiles = products.filter(Cateogary='Console Applications').count()
    
    print("📊 CATEGORY DISTRIBUTION:")
    print(f"  🏺 Pottery & Ceramics: {pottery}")
    print(f"  💍 Jewelry & Accessories: {jewelry}")
    print(f"  🧵 Textiles & Fabrics: {textiles}")
    print()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        sys.exit(1)
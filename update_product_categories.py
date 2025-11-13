#!/usr/bin/env python3
"""
Script to update product categories to match artisan marketplace theme
This script intelligently categorizes existing products based on their names and descriptions
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imac.settings')
django.setup()

from icommerce.models import Product

# Category mapping rules
CATEGORY_RULES = {
    'Web Applications': {  # Pottery & Ceramics
        'keywords': ['bowl', 'ceramic', 'pottery', 'vase', 'plate', 'cup', 'terracotta', 'clay', 'mug', 'dish'],
        'display_name': 'Pottery & Ceramics',
        'emoji': '🏺'
    },
    'Graphical Applications': {  # Jewelry & Accessories
        'keywords': ['pendant', 'necklace', 'jewelry', 'jewellery', 'ring', 'bracelet', 'earring', 'bag', 'satchel', 'purse', 'wallet', 'leather', 'accessory', 'belt', 'watch'],
        'display_name': 'Jewelry & Accessories',
        'emoji': '💍'
    },
    'Console Applications': {  # Textiles & Fabrics
        'keywords': ['blanket', 'throw', 'textile', 'fabric', 'scarf', 'shawl', 'cushion', 'pillow', 'rug', 'carpet', 'weave', 'woven', 'cotton', 'wool', 'silk', 'linen', 'tablecloth'],
        'display_name': 'Textiles & Fabrics',
        'emoji': '🧵'
    }
}

def detect_category(product):
    """
    Detect the best category for a product based on its name and description
    Returns (category_db_value, display_name, emoji)
    """
    product_text = (product.Product_Name + ' ' + product.Description).lower()
    
    # Check each category's keywords
    scores = {}
    for db_category, rules in CATEGORY_RULES.items():
        score = 0
        for keyword in rules['keywords']:
            if keyword in product_text:
                score += 1
        scores[db_category] = score
    
    # Find category with highest score
    if max(scores.values()) > 0:
        best_category = max(scores, key=scores.get)
        return best_category, CATEGORY_RULES[best_category]['display_name'], CATEGORY_RULES[best_category]['emoji']
    
    # Default to Pottery & Ceramics if no keywords match
    return 'Web Applications', 'Pottery & Ceramics', '🏺'

def categorize_products():
    """Categorize all products intelligently"""
    print("=" * 80)
    print("🎨 ShopEase Artisan Marketplace - Product Category Update")
    print("=" * 80)
    print()
    
    # Get all products
    products = Product.objects.all()
    
    if products.count() == 0:
        print("❌ No products found in database!")
        return
    
    print(f"Found {products.count()} product(s) to categorize\n")
    
    # Track changes
    updated_count = 0
    unchanged_count = 0
    category_distribution = {
        'Web Applications': 0,
        'Graphical Applications': 0,
        'Console Applications': 0
    }
    
    print("📋 Analyzing and updating categories...\n")
    print("-" * 80)
    
    for product in products:
        old_category = product.Cateogary
        new_category, display_name, emoji = detect_category(product)
        
        # Update if different
        if old_category != new_category:
            product.Cateogary = new_category
            product.save()
            
            print(f"{emoji} UPDATED: {product.Product_Name}")
            print(f"   Old: {old_category}")
            print(f"   New: {new_category} ({display_name})")
            print()
            updated_count += 1
        else:
            print(f"{emoji} UNCHANGED: {product.Product_Name} → {display_name}")
            unchanged_count += 1
        
        category_distribution[new_category] += 1
    
    print("-" * 80)
    print()
    print("=" * 80)
    print("📊 Update Summary")
    print("=" * 80)
    print(f"✅ Updated: {updated_count} product(s)")
    print(f"⏹️  Unchanged: {unchanged_count} product(s)")
    print(f"📦 Total: {products.count()} product(s)")
    print()
    
    print("📁 Final Category Distribution:")
    print("-" * 80)
    print(f"🏺 Pottery & Ceramics:      {category_distribution['Web Applications']:>2} items")
    print(f"💍 Jewelry & Accessories:   {category_distribution['Graphical Applications']:>2} items")
    print(f"🧵 Textiles & Fabrics:      {category_distribution['Console Applications']:>2} items")
    print()
    
    print("✨ Category update complete!")
    print()

def show_current_products():
    """Display all products with their current categories"""
    print("=" * 80)
    print("📦 Current Products in Database")
    print("=" * 80)
    print()
    
    products = Product.objects.all().order_by('Cateogary', 'Product_Name')
    
    if products.count() == 0:
        print("No products found.")
        return
    
    current_category = None
    for product in products:
        # Print category header when it changes
        if product.Cateogary != current_category:
            current_category = product.Cateogary
            
            if current_category == 'Web Applications':
                display = '🏺 Pottery & Ceramics'
            elif current_category == 'Graphical Applications':
                display = '💍 Jewelry & Accessories'
            elif current_category == 'Console Applications':
                display = '🧵 Textiles & Fabrics'
            else:
                display = current_category
            
            print()
            print(f"─── {display} " + "─" * (70 - len(display)))
            print()
        
        # Print product info
        status = "✓ Approved" if product.is_approved else "⏳ Pending"
        seller = f"by {product.seller.username}" if product.seller else "Admin Import"
        print(f"  • {product.Product_Name} (₹{product.Price}) - {status} {seller}")
        print(f"    {product.Description[:80]}...")
        print()
    
    print("=" * 80)
    print()

if __name__ == "__main__":
    try:
        # Show current state
        print("\n🔍 BEFORE UPDATE:")
        show_current_products()
        
        # Ask for confirmation
        print("\n" + "=" * 80)
        response = input("Proceed with category update? (yes/no): ").strip().lower()
        
        if response in ['yes', 'y']:
            print()
            categorize_products()
            
            # Show updated state
            print("\n🔍 AFTER UPDATE:")
            show_current_products()
        else:
            print("\n❌ Category update cancelled.")
    
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        print("\nPlease ensure:")
        print("1. Django server is not running")
        print("2. Database is accessible")
        print("3. You're in the correct directory")

#!/usr/bin/env python3
"""
Bulk Product Import Script for ShopEase Artisan Marketplace
This script populates the database with sample handmade artisan products.
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imac.settings')
django.setup()

from icommerce.models import Product

# Artisan Products Data
# Note: Categories map to database fields but display with artisan names:
# - "Pottery & Ceramics" = Web Applications in database
# - "Jewelry & Accessories" = Graphical Applications in database  
# - "Textiles & Fabrics" = Console Applications in database

PRODUCTS = [
    # Pottery & Ceramics
    {
        "name": "Rustic Ceramic Bowl Set",
        "price": 2499,
        "description": "Set of 4 hand-thrown ceramic bowls with unique glazing. Perfect for serving salads, soups, or as decorative pieces. Each bowl is one-of-a-kind with natural variations. Made using traditional pottery wheel techniques.",
        "category": "Web Applications",  # DB category
        "display_category": "Pottery & Ceramics",  # Display name
        "artisan": "Priya Ceramics Studio"
    },
    
    # Jewelry & Accessories
    {
        "name": "Moonstone Tear Drop Pendant",
        "price": 3499,
        "description": "Handcrafted sterling silver pendant featuring a natural moonstone. Wire-wrapped with intricate detailing. Comes with 18 inch sterling silver chain. Each stone is unique with beautiful natural variations.",
        "category": "Graphical Applications",  # DB category
        "display_category": "Jewelry & Accessories",  # Display name
        "artisan": "Silver Lining Jewelry"
    },
    
    # Textiles & Fabrics
    {
        "name": "Indigo Striped Throw Blanket",
        "price": 3299,
        "description": "Hand-woven cotton throw with traditional indigo stripe pattern. Made on a traditional floor loom. Soft, breathable, and perfect for all seasons. 100% organic cotton with natural indigo dye. 60 x 50 inches.",
        "category": "Console Applications",  # DB category
        "display_category": "Textiles & Fabrics",  # Display name
        "artisan": "Weaver's Cottage"
    },
    
    # Jewelry & Accessories
    {
        "name": "Vintage Brown Leather Satchel",
        "price": 4999,
        "description": "Hand-stitched leather crossbody bag with adjustable strap. Features multiple pockets and antique brass hardware. Full-grain vegetable-tanned leather develops beautiful patina over time. 10 x 8 x 3 inches.",
        "category": "Graphical Applications",  # DB category
        "display_category": "Jewelry & Accessories",  # Display name
        "artisan": "Leather Legacy Studio"
    },
    
    # Pottery & Ceramics
    {
        "name": "Contemporary Terracotta Vase",
        "price": 1899,
        "description": "Minimalist terracotta vase with hand-etched geometric patterns. Ideal for dried flowers or as a standalone art piece. Handmade using traditional pottery wheel techniques. 10 inches tall, perfect for any room.",
        "category": "Web Applications",  # DB category
        "display_category": "Pottery & Ceramics",  # Display name
        "artisan": "Earthen Touch Pottery"
    }
]

def add_products():
    """Add all products to the database"""
    print("=" * 60)
    print("🎨 ShopEase Artisan Marketplace - Product Import")
    print("=" * 60)
    print()
    
    added_count = 0
    skipped_count = 0
    
    for product_data in PRODUCTS:
        try:
            # Check if product already exists
            existing = Product.objects.filter(Product_Name=product_data["name"]).first()
            
            if existing:
                print(f"⚠️  SKIPPED: {product_data['name']} (already exists)")
                skipped_count += 1
                continue
            
            # Create new product
            product = Product.objects.create(
                Product_Name=product_data["name"],
                Price=product_data["price"],
                Description=product_data["description"],
                Cateogary=product_data["category"],
                pub_date=__import__('datetime').date.today(),
                linkToDownload=f"https://shopease.com/products/{product_data['name'].lower().replace(' ', '-')}",
                is_approved=True,  # Auto-approve admin-imported products
                approved_date=__import__('django.utils.timezone').timezone.now()
            )
            
            print(f"✅ ADDED: {product_data['name']} (₹{product_data['price']}) - {product_data['display_category']}")
            added_count += 1
            
        except Exception as e:
            print(f"❌ ERROR adding {product_data['name']}: {str(e)}")
    
    print()
    print("=" * 60)
    print("📊 Import Summary")
    print("=" * 60)
    print(f"✅ Successfully added: {added_count} products")
    print(f"⚠️  Skipped (already exist): {skipped_count} products")
    print(f"📦 Total in database: {Product.objects.count()} products")
    print()
    print("🎉 Product import complete!")
    print()
    print("Next steps:")
    print("1. Visit http://localhost:8000/admin to add product images")
    print("2. Check http://localhost:8000/shop/ to see your products")
    print("3. Test the shopping cart and checkout flow")
    print()

def show_category_breakdown():
    """Show breakdown by category"""
    print("📁 Products by Category:")
    print("-" * 60)
    
    web_apps = Product.objects.filter(Cateogary="Web Applications").count()
    print(f"🏺 Pottery & Ceramics: {web_apps} items")
    
    graphical = Product.objects.filter(Cateogary="Graphical Applications").count()
    print(f"💍 Jewelry & Accessories: {graphical} items")
    
    console = Product.objects.filter(Cateogary="Console Applications").count()
    print(f"🧵 Textiles & Fabrics: {console} items")
    print()

if __name__ == "__main__":
    try:
        add_products()
        show_category_breakdown()
    except Exception as e:
        print(f"❌ Fatal error: {str(e)}")
        print("Please ensure:")
        print("1. Django server is not running")
        print("2. Database is accessible")
        print("3. You're in the correct directory")

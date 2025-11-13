from django.shortcuts import redirect, render
from .models import Product, Order, Contact, admin
import requests
from itertools import chain
import smtplib
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import os

# Create your views here.
# def home(request):
#     catprods = Product.objects.values()
#     length = len(catprods)-1
#     idd = catprods[length]['id']
#     newprod = Product.objects.filter(id=idd)
#     allprod = Product.objects.values()
#     webprod = Product.objects.filter(Cateogary = "Graphical Applications")
#     params = {'newprod': newprod, 'allprod': allprod, 'gui': webprod, 'clas': 'active'}
#     return render(request, 'index.html', params)

from django.shortcuts import render
from .models import Product

def home(request):
    # latest approved product as a queryset (0 or 1 element)
    newprod = Product.objects.filter(is_approved=True).order_by('-id')[:1]

    allprod = Product.objects.filter(is_approved=True)
    webprod = Product.objects.filter(Cateogary="Graphical Applications", is_approved=True)
    params = {'newprod': newprod, 'allprod': allprod, 'gui': webprod, 'clas': 'active'}
    return render(request, 'index.html', params)


def about(request):
    params = {'abou': 'active'}
    return render(request, 'about.html',params)

def cart(request):
    return render(request, 'cart.html', {'on_cart_page': True})

def checkout(request):
    return render(request, 'checkout.html', {'on_checkout_page': True})

def contact(request, methods = ['GET', 'POST']):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        
        # Save contact to database
        contact = Contact(fname=fname, lname=lname, subject=subject, message=message, email=email)
        contact.save()
        
        # Email functionality (optional - disabled by default)
        # To enable email notifications:
        # 1. Set environment variables: EMAIL_HOST_USER and EMAIL_HOST_PASSWORD
        # 2. Or update the settings below with your SMTP credentials
        
        import os
        send_email = False  # Set to True to enable email notifications
        
        if send_email:
            try:
                sender_add = os.getenv('EMAIL_HOST_USER', 'your-email@gmail.com')
                password = os.getenv('EMAIL_HOST_PASSWORD', 'your-app-password')
                
                if sender_add != 'your-email@gmail.com' and password != 'your-app-password':
                    reciever_add = email
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    subb = f'Thank you for contacting RushX'
                    mailBody = f"Hello {fname} {lname},\n\n"
                    mailBody += f"Thank you for contacting us! We have received your message.\n\n"
                    mailBody += f"Subject: {subject}\n"
                    mailBody += f"Your Message: {message}\n\n"
                    mailBody += f"Our team will get back to you shortly at {email}\n\n"
                    mailBody += f"Best regards,\nRushX Team"
                    msg1 = f"""Subject : {subb}\n\n{mailBody}"""
                    server.starttls()
                    server.login(sender_add, password)
                    server.sendmail(sender_add, reciever_add, msg1)
                    server.quit()
            except Exception as e:
                print(f"Email sending failed: {e}")
                # Continue anyway - message is saved in database
        
        messages.success(request, f'Thank you {fname}! Your message has been successfully submitted. We will contact you soon.')
        return redirect('contact')
    
    params2 = {'cont': 'active'}
    return render(request, 'contact.html', params2)

def shop(request, methods=['GET', 'POST']):
    # Get filter parameters
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    category = request.GET.get('category', '')
    sort_by = request.GET.get('sort', '')
    search_query = request.GET.get('search', '')
    
    # Start with approved products only
    catProds = Product.objects.filter(is_approved=True)
    
    # Apply search filter
    if search_query:
        catProds = catProds.filter(Product_Name__icontains=search_query) | catProds.filter(Description__icontains=search_query)
    
    # Apply category filter
    if category:
        catProds = catProds.filter(Cateogary=category)
    
    # Apply price filter
    if min_price:
        try:
            catProds = catProds.filter(Price__gte=float(min_price))
        except ValueError:
            pass
    
    if max_price:
        try:
            catProds = catProds.filter(Price__lte=float(max_price))
        except ValueError:
            pass
    
    # Apply sorting
    if sort_by == 'price_low':
        catProds = catProds.order_by('Price')
    elif sort_by == 'price_high':
        catProds = catProds.order_by('-Price')
    elif sort_by == 'name_asc':
        catProds = catProds.order_by('Product_Name')
    elif sort_by == 'name_desc':
        catProds = catProds.order_by('-Product_Name')
    elif sort_by == 'newest':
        catProds = catProds.order_by('-id')
    else:
        catProds = catProds.order_by('-id')  # Default: newest first
    
    # Get category counts (only approved products)
    lengthofConsole = Product.objects.filter(Cateogary="Console Applications", is_approved=True).count()
    lengthofWeb = Product.objects.filter(Cateogary="Web Applications", is_approved=True).count()
    lengthofDesktop = Product.objects.filter(Cateogary="Graphical Applications", is_approved=True).count()
    
    params = {
        'allprods': catProds, 
        'shop': 'active', 
        'console': lengthofConsole, 
        'web': lengthofWeb, 
        'desktop': lengthofDesktop,
        'current_min': min_price,
        'current_max': max_price,
        'current_category': category,
        'current_sort': sort_by,
        'search_query': search_query,
        'total_products': catProds.count()
    }
    return render(request, 'shop.html', params)

def thankyou(request, methods = ['GET', 'POST']):
    allprods = Product.objects.values()
    if request.method == 'POST':
        country = request.POST.get('countryinput')
        itemsJson = request.POST.get('itemsJson')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        state = request.POST.get('state')
        zipcode = request.POST.get('zip')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        link = {}
        name = {}
        space = 0
        mailBody=f'Hey {fname},\n\nYour Order has been placed successfully! You can download your orders from the links below:\n\n'
        # str(itemsJson).split('"')[3]
        try:
            for i in range(0, len(allprods)):
                space = space + 3
                if allprods[i]["Product_Name"] == str(itemsJson).split('"')[space]:
                    link.update( {f'product{i}': allprods[i]["linkToDownload"] } )
                    name.update( {f'product{i}': allprods[i]["Product_Name"] } )
                    j = i + 1
                    mailBody += f'{j}. {allprods[i]["Product_Name"]}: {allprods[i]["linkToDownload"]} \n\n'
                    space = space + 3
        except IndexError as e:
            pass
        link2 = {'item': link, 'name': name}
        
        # Save order to database
        order = Order(itemsJson=itemsJson, firstName=fname, lastName=lname, email=email, address=address,
                       state=state, zipcode=zipcode, phone=phone, amount=amount, country=country)
        order.save()
        
        # Send order confirmation email using Django's email backend
        try:
            mailBody += f"\n\nOrder Details:\n"
            mailBody += f"Order Amount: ₹{amount}\n"
            mailBody += f"Shipping Address: {address}, {state} - {zipcode}\n"
            mailBody += f"Contact: {phone}\n\n"
            mailBody += "Thank you for shopping with ShopEase!\n"
            mailBody += "We hope to see you again soon.\n\n"
            mailBody += "Best regards,\nShopEase Team\n\n"
            mailBody += "For support, contact us at: dharmendrasahteli23@gmail.com"
            
            subject = f'{fname}, Your Order Has Been Placed Successfully!'
            
            # Use Django's send_mail function
            send_mail(
                subject=subject,
                message=mailBody,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            messages.success(request, f'Order placed successfully! Confirmation email sent to {email}')
        except Exception as e:
            # Order is saved even if email fails
            print(f"Email sending failed: {e}")
            messages.success(request, f'Order placed successfully! Please check your email for details.')
        
        return render(request, 'thankyou.html', link2)

def view(request, Product_Name, ID_of_the_Product):
    allProds = []
    idprod = int(ID_of_the_Product)
    catProds = Product.objects.filter(id=idprod)
    allProds = Product.objects.values()
    params = {'allprods': allProds, 'catprods': catProds}
    return render(request, 'shop-single.html', params)

def web(request):
    head = "Pottery & Ceramics"
    Prods = Product.objects.filter(Cateogary = "Web Applications", is_approved=True)
    allprods = Product.objects.filter(is_approved=True).values()
    lengthofConsole = Product.objects.filter(Cateogary = "Console Applications", is_approved=True)
    lengthofWeb = Product.objects.filter(Cateogary = "Web Applications", is_approved=True)
    lengthofDesktop = Product.objects.filter(Cateogary = "Graphical Applications", is_approved=True)
    prods = {'head': head, 'style': 'active', 'prod': Prods, 'allprods': allprods, 'web': len(lengthofWeb), 'desktop': len(lengthofDesktop), 'console': len(lengthofConsole)}
    return render(request, 'DiffrentiatedPoducts.html', prods)

def desktop(request):
    head = "Jewelry & Accessories"
    Prods = Product.objects.filter(Cateogary = "Graphical Applications", is_approved=True)
    allprods = Product.objects.filter(is_approved=True).values()
    lengthofConsole = Product.objects.filter(Cateogary = "Console Applications", is_approved=True)
    lengthofWeb = Product.objects.filter(Cateogary = "Web Applications", is_approved=True)
    lengthofDesktop = Product.objects.filter(Cateogary = "Graphical Applications", is_approved=True)
    prods = {'head': head, 'style': 'active', 'prod': Prods, 'allprods': allprods, 'web': len(lengthofWeb), 'desktop': len(lengthofDesktop), 'console': len(lengthofConsole)}
    return render(request, 'DiffrentiatedPoducts.html', prods)

def console(request):
    head = "Textiles & Fabrics"
    Prods = Product.objects.filter(Cateogary = "Console Applications", is_approved=True)
    allprods = Product.objects.filter(is_approved=True).values()
    lengthofConsole = Product.objects.filter(Cateogary = "Console Applications", is_approved=True)
    lengthofWeb = Product.objects.filter(Cateogary = "Web Applications", is_approved=True)
    lengthofDesktop = Product.objects.filter(Cateogary = "Graphical Applications", is_approved=True)
    prods = {'head': head, 'style': 'active', 'prod': Prods, 'allprods': allprods, 'web': len(lengthofWeb), 'desktop': len(lengthofDesktop), 'console': len(lengthofConsole)}
    return render(request, 'DiffrentiatedPoducts.html', prods)

def frontend(request):
    params = {'style': 'active'}
    return render(request, 'currentlyInBuild.html', params)

def backend(request):
    params = {'style': 'active'}
    return render(request, 'currentlyInBuild.html', params)

def search(request, keyword):
    catprods = Product.objects.filter(Cateogary = keyword)
    allprods = Product.objects.values()
    params = {'allprods': allprods, 'catprods': catprods, 'cat': keyword}
    return render(request, 'search.html', params)

def sub(request, email):
    response = requests.post('https://coderaman07.ck.page/', data = {'name' : email})

def signup_view(request):
    if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if password == confirm:
            if(User.objects.filter(username=username).exists()):
                messages.error(request, "Username already taken")
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, "User created successfully")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
    return render(request, 'signup.html')

def login_view(request):
    if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')

@login_required(login_url='/login')
def profile_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'update_profile':
            # Update user profile information
            user = request.user
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.email = request.POST.get('email', '')
            
            # Check if username is being changed and if it's already taken
            new_username = request.POST.get('username', '')
            if new_username != user.username:
                if User.objects.filter(username=new_username).exists():
                    messages.error(request, 'Username already taken. Please choose a different one.')
                    return redirect('profile')
                user.username = new_username
            
            try:
                user.save()
                messages.success(request, 'Profile updated successfully!')
            except Exception as e:
                messages.error(request, f'Error updating profile: {str(e)}')
        
        elif action == 'change_password':
            # Change password
            old_password = request.POST.get('old_password')
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')
            
            # Verify old password
            if not request.user.check_password(old_password):
                messages.error(request, 'Current password is incorrect.')
                return redirect('profile')
            
            # Check if new passwords match
            if new_password1 != new_password2:
                messages.error(request, 'New passwords do not match.')
                return redirect('profile')
            
            # Check password length
            if len(new_password1) < 8:
                messages.error(request, 'Password must be at least 8 characters long.')
                return redirect('profile')
            
            # Update password
            request.user.set_password(new_password1)
            request.user.save()
            
            # Keep user logged in after password change
            update_session_auth_hash(request, request.user)
            
            messages.success(request, 'Password changed successfully!')
        
        return redirect('profile')
    
    return render(request, 'profile.html')


# Product Listing Views
@login_required(login_url='/login/')
def list_product(request):
    """View for sellers to list their handmade products"""
    from .forms import ProductListingForm
    from django.utils import timezone
    
    if request.method == 'POST':
        form = ProductListingForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.pub_date = timezone.now().date()
            product.is_approved = False  # Needs admin approval
            product.linkToDownload = f"https://shopease.com/products/{product.Product_Name.lower().replace(' ', '-')}"
            product.save()
            
            messages.success(request, 'Your product has been submitted for review! It will be visible once approved by our team.')
            return redirect('my_products')
    else:
        form = ProductListingForm()
    
    return render(request, 'list_product.html', {'form': form})


@login_required(login_url='/login/')
def my_products(request):
    """View for sellers to see their listed products and their status"""
    products = Product.objects.filter(seller=request.user).order_by('-created_at')
    
    # Count by status
    pending_count = products.filter(is_approved=False).count()
    approved_count = products.filter(is_approved=True).count()
    
    context = {
        'products': products,
        'pending_count': pending_count,
        'approved_count': approved_count,
    }
    
    return render(request, 'my_products.html', context)


@login_required(login_url='/login/')
def delete_product(request, product_id):
    """View for sellers to delete their own products"""
    try:
        product = Product.objects.get(id=product_id, seller=request.user)
        product_name = product.Product_Name
        product.delete()
        messages.success(request, f'Product "{product_name}" has been deleted successfully.')
    except Product.DoesNotExist:
        messages.error(request, 'Product not found or you do not have permission to delete it.')
    
    return redirect('my_products')
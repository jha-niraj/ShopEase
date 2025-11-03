# 📧 Email Configuration Guide for ShopEase

This guide will help you set up Gmail SMTP for sending order confirmation emails to customers.

## 🎯 What You Need

To send emails from ShopEase, you need:
1. **A Gmail account** (any Gmail address will work)
2. **A Google App Password** (NOT your regular Gmail password)
3. **Environment variables** set up on your system

---

## 📝 Step-by-Step Setup Instructions

### Step 1: Enable 2-Factor Authentication on Gmail

1. Go to your Google Account: https://myaccount.google.com/
2. Click on **Security** in the left sidebar
3. Under "How you sign in to Google", click on **2-Step Verification**
4. Follow the prompts to enable 2-Step Verification (you'll need your phone)

### Step 2: Generate an App Password

1. After enabling 2-Step Verification, go back to **Security**
2. Under "How you sign in to Google", click on **App passwords**
   - If you don't see this option, make sure 2-Step Verification is enabled
3. You may need to sign in again
4. Under "Select app", choose **Mail**
5. Under "Select device", choose **Other (Custom name)**
6. Type "ShopEase" as the name
7. Click **Generate**
8. Google will show you a 16-character password (like: `abcd efgh ijkl mnop`)
9. **IMPORTANT**: Copy this password immediately! You won't be able to see it again
   - Example: `abcdefghijklmnop` (remove spaces)

### Step 3: Set Environment Variables

You need to set these environment variables on your system:

#### On Linux/Mac:

**Option A: Temporary (for current terminal session only)**
```bash
export EMAIL_HOST_USER="your-email@gmail.com"
export EMAIL_HOST_PASSWORD="your-app-password-here"
```

**Option B: Permanent (recommended)**

1. Edit your shell configuration file:
   ```bash
   nano ~/.bashrc    # For bash
   # OR
   nano ~/.zshrc     # For zsh
   ```

2. Add these lines at the end:
   ```bash
   export EMAIL_HOST_USER="your-email@gmail.com"
   export EMAIL_HOST_PASSWORD="your-app-password-here"
   ```

3. Save and reload:
   ```bash
   source ~/.bashrc   # For bash
   # OR
   source ~/.zshrc    # For zsh
   ```

#### On Windows:

**Option A: Command Prompt (temporary)**
```cmd
set EMAIL_HOST_USER=your-email@gmail.com
set EMAIL_HOST_PASSWORD=your-app-password-here
```

**Option B: PowerShell (temporary)**
```powershell
$env:EMAIL_HOST_USER="your-email@gmail.com"
$env:EMAIL_HOST_PASSWORD="your-app-password-here"
```

**Option C: System Environment Variables (permanent - recommended)**

1. Right-click on "This PC" or "My Computer" → Properties
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Add:
   - Variable name: `EMAIL_HOST_USER`
   - Variable value: `your-email@gmail.com`
6. Click "New" again and add:
   - Variable name: `EMAIL_HOST_PASSWORD`
   - Variable value: `your-app-password-here`
7. Click OK on all windows
8. **Restart your terminal/command prompt**

---

## ✅ Testing Your Email Configuration

### Method 1: Using Django Shell

```bash
python manage.py shell
```

Then run:
```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    subject='Test Email from ShopEase',
    message='If you receive this, email configuration is working!',
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=['your-test-email@gmail.com'],
    fail_silently=False,
)
```

If successful, you'll see `1` as output and receive an email!

### Method 2: Place a Test Order

1. Start your server: `python manage.py runserver`
2. Add a product to cart
3. Go through the checkout process
4. Enter your email address
5. Complete the order
6. Check your email for the order confirmation!

---

## 🔧 Configuration Details

The email settings are configured in `imac/settings.py`:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER', 'noreply@shopease.com')
```

### What happens when an order is placed?

The customer receives an email with:
- ✅ Order confirmation message
- ✅ List of purchased products with download links
- ✅ Order amount
- ✅ Shipping address details
- ✅ Contact information
- ✅ Support contact details

---

## 🚨 Troubleshooting

### "SMTPAuthenticationError: Username and Password not accepted"
- ✅ Make sure you're using an **App Password**, not your regular Gmail password
- ✅ Check that 2-Step Verification is enabled
- ✅ Verify the environment variables are set correctly
- ✅ Remove any spaces from the App Password

### "SMTPSenderRefused: Sender address rejected"
- ✅ Make sure EMAIL_HOST_USER matches your actual Gmail address
- ✅ Check that the Gmail account is active and not suspended

### Email not received
- ✅ Check spam/junk folder
- ✅ Verify the recipient email address is correct
- ✅ Check Django logs for error messages
- ✅ Try testing with Django shell (Method 1 above)

### Environment variables not working
- ✅ Restart your terminal after setting environment variables
- ✅ Verify with: `echo $EMAIL_HOST_USER` (Linux/Mac) or `echo %EMAIL_HOST_USER%` (Windows)
- ✅ Make sure there are no typos in variable names

---

## 🔒 Security Best Practices

1. **NEVER commit credentials to Git**
   - App passwords should only be in environment variables
   - Never hardcode them in your code

2. **Use different emails for development and production**
   - Development: Personal Gmail
   - Production: Business email or dedicated service email

3. **Keep your App Password secret**
   - Treat it like your password
   - Don't share it with anyone
   - Regenerate if compromised

4. **Monitor your email sending**
   - Gmail has daily sending limits (500 emails/day for free accounts)
   - Consider using dedicated email services for production (SendGrid, Mailgun, etc.)

---

## 📊 Email Sending Limits

**Gmail Free Account Limits:**
- 500 emails per day
- 500 recipients per email
- Best for: Development, testing, small businesses

**For Production/High Volume:**
Consider using:
- **SendGrid** (100 emails/day free tier)
- **Mailgun** (First 1000 emails free)
- **Amazon SES** (62,000 emails/month free with AWS)
- **Mailchimp Transactional** (500 emails/month free)

---

## 🎉 Quick Start Checklist

- [ ] Enable 2-Factor Authentication on Gmail
- [ ] Generate App Password from Google Account
- [ ] Set EMAIL_HOST_USER environment variable
- [ ] Set EMAIL_HOST_PASSWORD environment variable  
- [ ] Restart terminal/command prompt
- [ ] Test email with Django shell
- [ ] Place a test order and verify email receipt
- [ ] Check spam folder if email not in inbox

---

## 📞 Need Help?

If you're still having issues:
1. Double-check all steps above
2. Verify environment variables are set: 
   - Linux/Mac: `printenv | grep EMAIL`
   - Windows: `set EMAIL` or `gci env: | findstr EMAIL`
3. Check Django error logs
4. Test with a simple Python script first

---

## Example: Complete Setup (Linux)

```bash
# 1. Set environment variables (add to ~/.bashrc for permanence)
export EMAIL_HOST_USER="shopease.orders@gmail.com"
export EMAIL_HOST_PASSWORD="abcdefghijklmnop"

# 2. Reload shell configuration
source ~/.bashrc

# 3. Verify variables are set
echo $EMAIL_HOST_USER

# 4. Test with Django
python manage.py shell
```

Then in Python shell:
```python
from django.core.mail import send_mail
send_mail('Test', 'Testing ShopEase emails!', 'shopease.orders@gmail.com', ['customer@example.com'])
```

**Success!** 🎉 You should receive the test email!

---

## 📝 Notes

- Emails are sent automatically when customers place orders through `/checkout`
- The order is saved to the database even if email sending fails
- Email sending errors are logged but don't stop the order process
- Customers see a success message regardless of email status (for better UX)

---

**Created for ShopEase E-Commerce Platform**  
*Making online shopping seamless and secure!* 🛍️

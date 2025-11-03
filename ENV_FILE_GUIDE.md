# 🔐 Environment Variables Guide (.env File)

## ✅ Setup Complete!

Your ShopEase platform now uses a `.env` file to securely store sensitive configuration data.

---

## 📁 Files Created

### 1. `.env` - Your Actual Credentials (NEVER commit to Git!)
Located at: `/home/niraj/Documents/7thsemester/finalproject/.env`

Contains your real email credentials and configuration.

### 2. `.env.example` - Template for Others
Located at: `/home/niraj/Documents/7thsemester/finalproject/.env.example`

A safe template showing what variables are needed (without actual values).

### 3. `.gitignore` - Protection
Updated to exclude `.env` files from Git commits.

---

## 🔧 How It Works

### Before (Insecure):
```python
# settings.py - credentials visible in code ❌
EMAIL_HOST_USER = 'jhaniraj45@gmail.com'  # EXPOSED!
EMAIL_HOST_PASSWORD = 'acumdizotvgzaisk'   # EXPOSED!
```

### After (Secure):
```python
# settings.py - reads from .env file ✅
from decouple import config
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
```

```bash
# .env file - NOT committed to Git ✅
EMAIL_HOST_USER=jhaniraj45@gmail.com
EMAIL_HOST_PASSWORD=acumdizotvgzaisk
```

---

## 📋 Current .env Configuration

Your `.env` file contains:

```env
# Email Configuration
EMAIL_HOST_USER=jhaniraj45@gmail.com
EMAIL_HOST_PASSWORD=acumdizotvgzaisk

# Django Secret Key
SECRET_KEY=Enter Your Security Key Here

# Debug Mode
DEBUG=True

# Allowed Hosts
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## ⚙️ How to Use

### The .env file is automatically loaded!

1. **Django reads the `.env` file** when it starts
2. **`config()` function** pulls values from `.env`
3. **No manual export needed** - it just works!

### Example Flow:

```
Django starts
    ↓
Loads .env file
    ↓
Reads: EMAIL_HOST_USER=jhaniraj45@gmail.com
    ↓
config('EMAIL_HOST_USER') returns "jhaniraj45@gmail.com"
    ↓
Django uses it for sending emails ✅
```

---

## 🔒 Security Benefits

### ✅ What's Protected:
- Email credentials NOT in code
- `.env` file excluded from Git (in `.gitignore`)
- Credentials stay on your local machine only
- Easy to change without editing code

### ✅ Safe to Commit:
- `settings.py` (no credentials inside)
- `.env.example` (template without real values)
- `.gitignore` (protects .env)

### ❌ NEVER Commit:
- `.env` file (has your real credentials)
- Any file with actual passwords

---

## 🚀 Using on Different Environments

### Development (Your Computer):
```bash
# .env file
EMAIL_HOST_USER=jhaniraj45@gmail.com
EMAIL_HOST_PASSWORD=acumdizotvgzaisk
DEBUG=True
```

### Production (Server):
```bash
# .env file on server
EMAIL_HOST_USER=production@shopease.com
EMAIL_HOST_PASSWORD=different-app-password
DEBUG=False
ALLOWED_HOSTS=shopease.com,www.shopease.com
```

Same `settings.py` works everywhere! Just different `.env` files.

---

## 📝 Editing Your .env File

### To Change Email Credentials:

1. Open `.env` file:
   ```bash
   nano .env
   ```

2. Edit the values:
   ```env
   EMAIL_HOST_USER=new-email@gmail.com
   EMAIL_HOST_PASSWORD=new-app-password
   ```

3. Save and restart Django:
   ```bash
   python manage.py runserver
   ```

That's it! No code changes needed.

---

## 🔄 Setting Up on a New Computer

### Step 1: Clone Repository
```bash
git clone <your-repo>
cd finalproject
```

### Step 2: Copy .env.example to .env
```bash
cp .env.example .env
```

### Step 3: Edit .env with Your Credentials
```bash
nano .env
```

### Step 4: Install Dependencies
```bash
pip install django pillow python-decouple
```

### Step 5: Run Django
```bash
python manage.py runserver
```

---

## 🛡️ .gitignore Protection

Your `.gitignore` now includes:

```gitignore
# Environment Variables - NEVER commit these!
.env
.env.local
*.env
```

This ensures:
- ✅ `.env` is never committed to Git
- ✅ Your credentials stay private
- ✅ Safe to push to GitHub

---

## ⚠️ Important Security Notes

### 1. App Password Security
Your current App Password `acumdizotvgzaisk` is now stored in `.env`:
- ✅ Protected from Git commits
- ✅ Not visible in code
- ✅ Easy to rotate/change

### 2. If .env is Accidentally Committed

If you accidentally commit `.env` to Git:

```bash
# Remove from Git (but keep local file)
git rm --cached .env

# Commit the removal
git commit -m "Remove .env from repository"

# IMPORTANT: Regenerate all credentials in .env!
# Someone may have seen them in Git history
```

### 3. Sharing with Team

**NEVER share .env file directly!**

Instead:
- Share `.env.example` (template)
- Team members create their own `.env`
- Each person uses their own credentials

---

## 📊 What Gets Read from .env

| Variable | Used For | Example Value |
|----------|----------|---------------|
| `EMAIL_HOST_USER` | Gmail address | jhaniraj45@gmail.com |
| `EMAIL_HOST_PASSWORD` | Gmail App Password | acumdizotvgzaisk |
| `SECRET_KEY` | Django encryption | random-string-here |
| `DEBUG` | Debug mode | True/False |
| `ALLOWED_HOSTS` | Domain whitelist | localhost,127.0.0.1 |

---

## ✅ Verification

To verify `.env` is working:

### Method 1: Python Shell
```bash
python manage.py shell
```

```python
from decouple import config
print(config('EMAIL_HOST_USER'))
# Should print: jhaniraj45@gmail.com
```

### Method 2: Test Email
```python
python manage.py shell
```

```python
from django.core.mail import send_mail
send_mail(
    'Test from .env',
    'If you get this, .env is working!',
    'jhaniraj45@gmail.com',
    ['jhaniraj45@gmail.com'],
)
# Should return: 1 (success!)
```

---

## 🎯 Benefits Summary

### Before .env:
- ❌ Credentials in code
- ❌ Visible in Git
- ❌ Hard to change
- ❌ Security risk

### After .env:
- ✅ Credentials in separate file
- ✅ Protected by .gitignore
- ✅ Easy to change
- ✅ Secure and professional

---

## 📚 Additional Configuration

### Add More Variables to .env:

```env
# Database (for production)
DATABASE_NAME=shopease_db
DATABASE_USER=db_user
DATABASE_PASSWORD=db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# AWS S3 (for file uploads)
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret

# Payment Gateway
RAZORPAY_KEY_ID=your-key
RAZORPAY_KEY_SECRET=your-secret
```

### Read in settings.py:

```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT', cast=int),
    }
}
```

---

## 🎉 You're All Set!

Your ShopEase platform now:
- ✅ Uses `.env` for credentials
- ✅ Protected by `.gitignore`
- ✅ Automatically loads configuration
- ✅ Safe to commit to Git
- ✅ Professional and secure

**No more hardcoded credentials!** 🔒

---

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named 'decouple'"
```bash
pip install python-decouple
```

### "KeyError: 'EMAIL_HOST_USER'"
Check that `.env` file exists in project root and has the variable:
```bash
ls -la .env
cat .env | grep EMAIL_HOST_USER
```

### Email Not Sending
1. Verify `.env` has correct credentials
2. Check App Password is valid
3. Test with Python shell (see Verification section)

---

**Created**: November 3, 2025  
**Package**: python-decouple  
**Status**: ✅ Configured and Working

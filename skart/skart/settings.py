#KEEP IN MIND THIS IS THE (settings.py) FILE OUR (skart) PROJECT AND NOT OUR (shop) APP.aur app ka "settings.py" hota bhi nahi hai,project ka hi hota hai,that's how you can seprate both.
import os
"""
Django settings for skart project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# yeah the above is important to important
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--fi*_1jw+lpj6cqiu=fjn=wy_fvh&jl&@@@c4(fq2d!+-a_l=l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'shop.apps.ShopConfig',
    # above we added the shop app to our project (skart).
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'skart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['skart/templates'],
        #above we give directory of our templates folder which consists of all our html pages of our skart project(and not our skart app).the statement 'skart/templates' simply states that the (templates) folder or directory is within the (skart) project.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'skart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# SEE MIGRATIONS MEANS TO SAVE(in some file like .0001_initial.py ) ALL THE CHANGES(like changing name of some html file,or some variable,etc.) MADE BY US by using command (python manage.py makemigrations). THE COMMAND: (python manage.py migrate), will (APPLY) ALL THESE SAVED CHANGES.


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# STATIC_URL: It is simply the prefix of the URL that will be visible to the user while accessing the static files.Example: Suppose a user tries to access a static file named "mystatic.txt" of the shop app. Then, he or she will access the file at http://127.0.0.1:8000/static/shop/mystatic.txt. 

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MANAGING MEDIA
# BELOW WE ADD SOME MEDIA FILES IN ORDER TO BE ABLE TO SAVE IMAGES OF PRODUCTS INTO THE DATABASE TABLE(or model that we have created in model.py of shop).
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# 2. MEDIA_ROOT: It is the path to the directory in which all the media files(photos of products) will be saved. Here, we have written(BASE_DIR, "media") which means that Django will create a folder named "media" under the base directory and all the media files will be saved in the "media" folder.
MEDIA_URL =  '/media/'
# 3.MEDIA_URL: Similar to the STATIC_URL, it is also the prefix of the URL that will be visible to the user while accessing the media files.
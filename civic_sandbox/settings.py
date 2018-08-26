"""
Django settings for civic_sandbox project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == "True"

ALLOWED_HOSTS = ['*']


# Application definition

if DEBUG == True:

    INSTALLED_APPS = [
         'test_without_migrations',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'api',
        'corsheaders',
        'django_filters',
        'rest_framework',
        'rest_framework_swagger',
        'rest_framework_gis',
        'neighborhood_development_18',
        'transportation_systems_18',
        'registry',
        'disaster_resilience_18',
        'housing_affordability_18',

        ]

else:
    INSTALLED_APPS = [
         'test_without_migrations',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'api',
        'corsheaders',
        'django_filters',
        'rest_framework',
        'rest_framework_swagger',
        'rest_framework_gis',
        'neighborhood_development_18',
        'transportation_systems_18',
        'registry',
        'disaster_resilience_18',
        'housing_affordability_18',
        ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'civic_sandbox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'civic_sandbox.wsgi.application'


DATABASE_ROUTERS = ['civic_sandbox.routers.CivicSandboxRouter']

DATABASES = {
    'default': {},
    'neighborhood-development': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_PASSWORD'),
        'NAME': os.environ.get('NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_NAME'),
        'USER': os.environ.get('NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_USER'),
        'HOST': os.environ.get('NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    },
    'transportation-systems-main': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },
    'odot_crash_data': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'OPTIONS': {
                'options': '-c search_path=django,odot_crash_data'
            },
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },

    'passenger_census': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'OPTIONS': {
                'options': '-c search_path=django,passenger_census'
            },
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },

    'safety_hotline_tickets': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'OPTIONS': {
                'options': '-c search_path=django,safety_hotline_tickets'
            },
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },
    'pudl': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'OPTIONS': {
                'options': '-c search_path=django,pudl'
            },
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },
    'disaster-resilience-disaster': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('DISASTER_RESILIENCE_18_POSTGRES_PASSWORD'),
        'NAME': os.environ.get('DISASTER_RESILIENCE_18_POSTGRES_NAME'),
        'USER': os.environ.get('DISASTER_RESILIENCE_18_POSTGRES_USER'),
        'HOST': os.environ.get('DISASTER_RESILIENCE_18_POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    },
    'housing-affordability': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('HOUSING_AFFORDABILITY_18_POSTGRES_PASSWORD'),
        'NAME': os.environ.get('HOUSING_AFFORDABILITY_18_POSTGRES_NAME'),
        'USER': os.environ.get('HOUSING_AFFORDABILITY_18_POSTGRES_USER'),
        'HOST': os.environ.get('HOUSING_AFFORDABILITY_18_POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    },
}

if DEBUG == False:

    DATABASES = {
    'default': {},
    'neighborhood-development': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_PASSWORD'),
        'NAME': os.environ.get('NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_NAME'),
        'USER': os.environ.get('NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_USER'),
        'HOST': os.environ.get('NEIGHBORHOOD_DEVELOPMENT_18_POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    },
    'transportation-systems-main': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },
    'odot_crash_data': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'OPTIONS': {
                'options': '-c search_path=django,odot_crash_data'
            },
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },

    'passenger_census': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'OPTIONS': {
                'options': '-c search_path=django,passenger_census'
            },
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },

    'safety_hotline_tickets': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'OPTIONS': {
                'options': '-c search_path=django,safety_hotline_tickets'
            },
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },
    'pudl': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PASSWORD'),
        'OPTIONS': {
                'options': '-c search_path=django,pudl'
            },
        'NAME': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_NAME'),
        'USER': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_USER'),
        'HOST': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_HOST'),
        'PORT': os.environ.get('TRANSPORTATION_SYSTEMS_18_POSTGRES_PORT')
    },
        'disaster-resilience-disaster': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('DISASTER_RESILIENCE_18_POSTGRES_PASSWORD'),
        'NAME': os.environ.get('DISASTER_RESILIENCE_18_POSTGRES_NAME'),
        'USER': os.environ.get('DISASTER_RESILIENCE_18_POSTGRES_USER'),
        'HOST': os.environ.get('DISASTER_RESILIENCE_18_POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    },
    'housing-affordability': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('HOUSING_AFFORDABILITY_18_POSTGRES_PASSWORD'),
        'NAME': os.environ.get('HOUSING_AFFORDABILITY_18_POSTGRES_NAME'),
        'USER': os.environ.get('HOUSING_AFFORDABILITY_18_POSTGRES_USER'),
        'HOST': os.environ.get('HOUSING_AFFORDABILITY_18_POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

#custom test runner to toggle between Managed=True and Managed=False for models handling test db
#TEST_RUNNER = 'api.utils.UnManagedModelTestRunner'

#rest framework settings for API
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

#add CORS support for all domains
CORS_ORIGIN_ALLOW_ALL = True

import sys
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-9!90p$96t%-bk0=j2z04e2gdmg%*a-12h%$f3a9#s-t681uo8i"

ALLOWED_HOSTS = ["*"]

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap5",
    "debug_toolbar",
    "accounts",
    "messenger",
    "log"
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "base.middlewares.LoggingMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "log": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "log.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.User"

LOGIN_REDIRECT_URL = "messenger:home"

# email
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "your-email@gmail.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "password")
EMAIL_PORT = os.getenv("EMAIL_PORT", 587)

MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "media/"

# TODO DON'T FORGET TO HIDE THEM IN ENV
STORAGES = {
    "default": {
        "BACKEND": "base.storages.WindowsCompatibleDropboxStorage",
        "OPTIONS": {
            "oauth2_access_token": "sl.u.AF57GdOY6Mq8Ri7QvMxD9eZVv7kFVRRaDuFSGM-rot_jJcqgAb1PfgkkkswULu9LQpM1ZVnX36yn0tiKaas9diku4jJJ-n2ERXqcODoPDglRPWM11L_pRaZhy3dRVYcAR0EPYHgBzSz0ENjlk4ZqROfLVPXYEfIGpKfJ5M8xXqXZSwPT9PEC6xcmdw6svneroJvMzuFpsPW2t66VIBxUh91zp2WRwCfmpW5mzalaxygePtWu9KIooTiOhvjdf9e6222z-4da3f3FwHddfq4ThUv5C40jox3EppKO4A2HpmrVPr_op-ItI1YKXH9iVbBT7C06lP0Lobzwis4kvZeba2sXIi3cVrsNyEHZuq2OZ76pMIJ-pUESHlEHQlmKcO7b4AHzjGboxu1EIk_RU4-SYkx65rLmyRlYodDBYWDLZrsyJNwYWR79NIubRIP0TxMHKESY2SeNxL__FT6cXB9xvBB5QOWRuoSKpBbMLBTjk9l6BTBM9ydASRGxEKdRfdp3DPDJFKv_kNqEAkMZcV2pcig-oFKcFRvWWbAEj_nQ4m6rKZSwmr4z8YK9AnTZm4AE_2So4A-A2_br_dYGLZ_DFB-8Vf3V5nK-J6oDdI_Ok3zmo1AByI63WQcpHnAaB-xfJVLSW9pHCOKY_Q06uGO1F9gVMmEu33r7JVYdSTHfCdy7ljkoR09Vlq0wrGkUZojCArLgXLz87za3goL2e_GKJFfLpiyeVH_nQ7iH0OjaU8Jbtv7krzxLvZ35I_0WdL8TGozgY3Usz07iWWXjPzqjSPym51s3p-MxdtUGxqKln0IlXEiixU9ijgXbe-7gzrNDiYnZOvWkp7OAExLktDPn2ffFn32t4CvlbXVHYKGuvTAC6e5Ud0QUQRkD8_k7oHo1WoNLIuOneA0Jzq8U45soZDjbJb1PIMicMLJPHSBYI3NS6ILt4_FlazkVeUj6o3XbXVOY1OA3Jl6ZvZ2X7PtMNmPB1Fba3BO64H-VO3NIYvZEaWfBRn19Cd9P1mgyj9iPy31nDOYIN9YO2xxHLP8_jjafgn55xde2Xamnello7rC7xpdl0Tf438YoksvqGydCD4E9yooBHsvEklj0WV-DG9ADzveBfUlCiEACBiB829MZRrkYbz5AvRn3wz0VfUmyKYT9m9HMZU7YIIW5PZyHKECA_2w_I-KRrys13ItOX185dxdtBFdr-TSSbImTBr8uvg_e7QPP5p9VwT3efDtHiFktc0TZwbWQzAMg6B_5L20HzGCSDjJJOTFV45WlJ_6wXF7uYTJ1_BdUKSPIW6OQQQ41KOMDxSXPxBvz5lSE8QUrnFKU8bxFsPgVYbvjY-4MJIkvNlXUCkaZiXq1ONT3njypoBA7l3983e2Lu2pINg28DPcOu-CFcu9ElH2KAMiU7A24AY9944qGZuGH2-D_m__Q",
            "oauth2_refresh_token": "XGMH56Ek3GoAAAAAAAAAATCcc1APyc_AJlpyIvREoBy1XoKECegOING5mv607vrK",
            "app_secret": "e2l4kgt3yr101td",
            "app_key": "5pmnsz1v2x1bhbq",
            "root_path": "media/",
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

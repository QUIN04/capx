# Inside apps.py
from django.apps import AppConfig

class BugConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bug'

default_app_config = 'bug.apps.BugConfig'
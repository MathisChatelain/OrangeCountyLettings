# pytest_settings.py

from .settings import *

# Override the STATICFILES_STORAGE setting to use the StaticFilesStorage backend.
# This backend performs no file operations during testing, effectively ignoring static files.
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Add any other pytest-specific settings or configurations as needed.

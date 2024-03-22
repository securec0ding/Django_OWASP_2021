# views.py

import logging
from django.http import HttpResponse  # Import HttpResponse class

def vulnerable_view(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')

    # Vulnerable logging: Log sensitive information without proper sanitization
    logging.debug(f"Login attempt: username={username}, password={password}")

    return HttpResponse("Login failed")


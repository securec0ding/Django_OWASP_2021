# views.py

from django.http import HttpResponse
from django.db import connection

def vulnerable_view(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')

        # Vulnerable SQL query susceptible to SQL injection
        query = f"SELECT * FROM auth_user WHERE username = '{username}'"

        # Execute the query
        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()

        # Check if user exists
        if row:
            return HttpResponse(f"Welcome, {username}!")
        else:
            return HttpResponse("Invalid username or password.")


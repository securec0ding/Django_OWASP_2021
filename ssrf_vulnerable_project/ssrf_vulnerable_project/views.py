import requests
from django.http import HttpResponse

def vulnerable_view(request):
    url = request.GET.get('url', '')
    if url:
        response = requests.get(url)
        return HttpResponse(response.text)
    else:
        return HttpResponse('Please provide a URL parameter.')


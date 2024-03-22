from django.http import HttpResponse

def vulnerable_view(request):
    query_param = request.GET.get('q', '')
    return HttpResponse(f'<p>You searched for: {query_param}</p>')


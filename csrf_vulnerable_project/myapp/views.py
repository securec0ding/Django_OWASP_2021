from django.http import HttpResponse

def vulnerable_transfer(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        # Transfer money
        return HttpResponse(f'Transferred {amount} to another account!')
    else:
        return HttpResponse('Please use POST method to transfer money.')


from django.contrib.sessions.backends.db import SessionStore

from django.http import HttpResponse

def vulnerable_set_session(request):
    session_id = request.GET.get('session_id', '')
    if session_id:
        # Regenerate the session key
        #request.session.cycle_key()
        request.session = SessionStore()
        request.session.save()  # Save the session
        return HttpResponse(f'Session ID set to: {request.session.session_key}')
    else:
        return HttpResponse('Please provide a session ID parameter.')


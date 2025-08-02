import json, uuid
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import RequestLog

def generate_session_id():
    return uuid.uuid4().hex

def home(request):
    if not request.session.get('inspector_id'):
        request.session['inspector_id'] = generate_session_id()
    return redirect(f"/{request.session['inspector_id']}/")

def view_requests(request, session_id):
    requests = RequestLog.objects.filter(session_id=session_id).order_by('-timestamp')[:50]
    return render(request, 'inspector/view.html', {'requests': requests, 'session_id': session_id})

def receive_hook(request, session_id):
    RequestLog.objects.create(
        session_id=session_id,
        method=request.method,
        headers=json.dumps(dict(request.headers)),
        body=request.body.decode('utf-8', errors='ignore'),
    )
    return JsonResponse({"status": "received"})

from django.shortcuts import redirect
from functools import wraps 

def hardcoded_admin_only(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('is_admin_authenticated') or (request.user.is_authenticated and request.user.is_superuser):
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

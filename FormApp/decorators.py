from django.http import HttpResponseForbidden
from functools import wraps

def admin_only(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'profile') and request.user.profile.designation == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to perform this action. Only designation=admin can perform this action")
    return _wrapped_view

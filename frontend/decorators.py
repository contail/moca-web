from django.contrib.auth.models import AnonymousUser
from django.shortcuts import redirect


def login_required(func):
    def newfunc(request, *args, **kwargs):
        if not request.user == AnonymousUser:
            return redirect('/admin/login')
        return func(request, *args, **kwargs)
    newfunc.__name__ = func.__name__
    newfunc.__doc__ = func.__doc__
    return newfunc
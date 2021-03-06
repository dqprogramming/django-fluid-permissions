from functools import wraps
from urllib.parse import urlencode

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse

from fluid_permissions import models


def base_check(request, login_redirect=False):
    """Equivalent to Django's login_required logic

    It also considers request being None and request.user not being
    active
    """

    if (
        request is None
        or request.user is None
        or request.user.is_anonymous
        or not request.user.is_active
    ):
        if login_redirect is True:
            params = urlencode({"next": request.path})
            return redirect('{0}?{1}'.format(reverse(settings.LOGIN_URL), params))
        elif isinstance(login_redirect, str):
            params = urlencode({"next": redirect})
            return redirect('{0}?{1}'.format(reverse(settings.LOGIN_URL), params))
        else:
            return False

    return True


def base_check_required(func):
    """ Decorator similar to django login_required

    Validates the request user against base_check instead
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        check = base_check(request, login_redirect=True)
        if check is True:
            return func(request, *args, **kwargs)
        else:
            return check
    return wrapper


def user_in_authorised_group(func):
    """
    This decorator checks that the current user is in a group that has permission
    to access the current view.

    :param func: the function to callback from the decorator
    :return: either the function call or raises an Http404
    """

    @base_check_required
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        view_name = func.__name__

        try:
            view_group = models.ViewGroup.objects.get(
                view_name=view_name,
            )
            group_names = [group.name for group in view_group.groups.all()]
            if request.user.groups.filter(name__in=group_names).exists():
                return func(request, *args, **kwargs)
        except models.ViewGroup.DoesNotExist:
            raise PermissionDenied(
                'This view has no authorised groups.',
            )

        raise PermissionDenied(
            'You do not have permission for this view.',
        )

    return wrapper



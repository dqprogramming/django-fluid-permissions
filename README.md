Django Fluid Permissions
========================

Django Fluid Permissions is a package that allows you to determine access to a view based on groups and users.

For a given view you can determine which groups have permission. Users in given groups can then access the views.

Setup
-----
You can install the package with the following command:

`pip3 install git+https://gitlab.com/dq-programming/django-fluid-permissions@master#django-fluid-permissions`

- As there are currently no stable builds of the package we recommend you use the master branch. 
- Once installation is complete add `'fluid_permissions'` to `INSTALLED_APPS` in your settings file.
- Migrate your database to add the required tables `python3 manage.py migrate`.


Decorating a Function
---------------------
Fluid Permissions provides a decorator you can use to limit access to certain views. See the example below for usage.

```
from django.shortcuts import reverse

from fluid_permissions import decorators


@decorators.user_in_authorised_group
def limited_access_view(request):
    """
    A view with access limited to a group.
    """
    template = 'test.html'
    context = {}
    return render(request, template, context)
```

Groups and Permissions
----------------------
Once the package is installed and the db updated we can now create permissions.

1. If you haven't already create a Group in django. This can be done via the admin interface under Authentication and Authorization > Groups.
2. Once you have a group you can create a ViewGroup. This ties a given view name to a group. You can do this in admin under Fluid_Permissions > View groups.
3. Add a user to the group created in step 1.
4. Decorate a view (as in the example above), access is now limited to users in ViewGroup.groups manytomany.
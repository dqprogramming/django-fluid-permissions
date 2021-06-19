Django Fluid Permissions
------------------------

Django Fluid Permissions is a package that allows you to determine access to a view based on groups and users.

For a given view you can determine which groups have permission. Users in given groups can then access the views.

Setup
-----
You can install the package with the following command:

`pip3 install git+https://gitlab.com/dq-programming/django-fluid-permissions@master#django-fluid-permissions`

- As there are currently no stable builds of the package we recommend you use the master branch. 
- Once installation is complete add `'fluid_permissions'` to `INSTALLED_APPS` in your settings file.
- Migrate your database to add the required tables `python3 manage.py migrate`.


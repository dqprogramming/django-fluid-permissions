from setuptools import setup

setup(
    name='FluidPermissions',
    version='0.0.1',
    author='Andy Byers',
    author_email='ajrbyers@gmail.com',
    packages=['fluid_permissions'],
    url='https://gitlab.com/dqprogramming/',
    license='LICENSE.txt',
    description='A Django permissions package.',
    long_description=open('README.txt').read(),
    install_requires=[
       "Django >= 3.2.4",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    include_package_data=True
)

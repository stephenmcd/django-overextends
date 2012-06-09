
from setuptools import setup, find_packages


setup(
    name = "django-overextends",
    version = __import__("overextends").__version__,
    author = "Stephen McDonald",
    author_email = "stephen.mc@gmail.com",
    description = ("A Django reusable app providing the ability to use "
                   "circular template inheritance."),
    long_description = open("README.rst").read(),
    url = "http://github.com/stephenmcd/django-overextends",
    zip_safe = False,
    include_package_data = True,
    packages = find_packages(),
    install_requires = [
        "sphinx-me >= 0.1.2",
        "django >= 1.3.1",
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ]
)

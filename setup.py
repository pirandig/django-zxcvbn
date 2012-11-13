from setuptools import setup

setup(
    name = "django-zxcvbn",
    version = __import__("django_zxcvbn").__version__,
    author = "Rich Atkinson",
    author_email = "rich@piran.com.au",
    description = "Django app providing zxcvbn password validation (see http://tech.dropbox.com/?p=165)",
    long_description = open("README.rst").read(),
    url = "http://github.com/atkinsonr/django-zxcvbn/",
    license = "BSD",
    packages = [
        "django_zxcvbn",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
        "Framework :: Django",
    ]
)

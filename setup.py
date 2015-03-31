#!/usr/bin/env python

from setuptools import setup, find_packages
import provider
import sys

if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version(provider.__version__, __file__)
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()

setup(
    name='django-oauth2-provider',
    version=version,
    description='Provide OAuth2 access to your app',
    long_description=open('README.rst').read(),
    author='Alen Mujezinovic',
    author_email='alen@caffeinehit.com',
    url = 'https://github.com/caffeinehit/django-oauth2-provider',
    packages= find_packages(exclude=('tests*',)),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        "shortuuid>=0.3"
    ],
    test_requires=[
        "mock>=1.0.1",
        "South>=0.8.4"
    ],
    include_package_data=True,
    zip_safe=False,
)

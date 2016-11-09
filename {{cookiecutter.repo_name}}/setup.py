#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import os.path as op


from codecs import open
from setuptools import setup


def read(fname):
    ''' Return the file content. '''
    here = op.abspath(op.dirname(__file__))
    with open(op.join(here, fname), 'r', 'utf-8') as fd:
        return fd.read()

readme = read('README.rst')
changelog = read('CHANGES.rst').replace('.. :changelog:', '')

requirements = read('requirements.txt').split()

if sys.version_info[0] == 2:
    # TODO: put python2-only package requirements
    # requirements.append('example-package')
    pass


if sys.version_info[0] == 3:
    # TODO: put python3-only package requirements
    # requirements.append('example-package')
    pass

version = ''
version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                    read(op.join('{{ cookiecutter.package_name }}', '__init__.py')),
                    re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name='{{ cookiecutter.repo_name }}',
    author='{{ cookiecutter.full_name.replace('\"', '\\\"') }}',
    author_email='{{ cookiecutter.email }}',
    version=version,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}',
    packages=[
        '{{ cookiecutter.package_name }}',
    ],
    package_dir={'{{ cookiecutter.package_name }}':
                 '{{ cookiecutter.package_name }}'},
    install_requires=requirements,
    include_package_data=True,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license='{{ cookiecutter.open_source_license }}',
{%- endif %}
    zip_safe=False,
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme + '\n\n' + changelog,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

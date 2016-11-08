{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
===============================
{{ cookiecutter.project_name }}
===============================


{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}
    :alt: CI Status

.. image:: http://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/coverage.svg?branch=master
    :target: http://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}?branch=master
    :alt: Coverage Status

.. image:: https://readthedocs.org/projects/{{ cookiecutter.github_repo_name }}/badge/?version=latest
    :target: https://readthedocs.org/projects/{{ cookiecutter.github_repo_name }}/?badge=latest
    :alt: Documentation Status

.. image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/master/landscape.svg?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/master
    :alt: Code Health
{%- endif %}

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/
     :alt: Updates

{{ cookiecutter.project_short_description}}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.repo_name }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

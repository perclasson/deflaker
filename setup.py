#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['GitPython==2.1.11', 'unidiff==0.5.5', 'pytest==3.8.2', 'coverage==4.5.1']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Per Classon",
    author_email='perwclasson@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Automatically detect flaky tests. Inspired by https://github.com/gmu-swe/deflaker",
    entry_points={
        'console_scripts': [
            'deflaker=deflaker.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='deflaker',
    name='deflaker',
    packages=find_packages(include=['deflaker']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/perclasson/deflaker',
    version='0.1.0',
    zip_safe=False,
)

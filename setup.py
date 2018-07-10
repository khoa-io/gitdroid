# -*- coding: utf-8 -*-

"""Git Droid Package

See:
https://github.com/khoa-io/gitdroid
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gitdroid',
    version='0.0.1',
    description='Git Droid',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/khoa-io/gitdroid',
    author='Hoàng Văn Khoa',
    author_email='hoangvankhoa@outlook.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Version Control',
        'Topic :: Software Development :: Version Control :: Git',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='git development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'gitdroid=gitdroid:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/khoa-io/gitdroid/issues',
        'Source': 'https://github.com/khoa-io/gitdroid/',
    },
)

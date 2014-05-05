#!/usr/bin/env python


from setuptools import setup


setup(
    name='mdx_figcaption',
    version='0.1',
    author='Helder Correia',
    author_email='me@heldercorreia.com',
    description='Extension for Python-Markdown to parse images with captions inside a figure element.',
    url='https://github.com/helderco/markdown-figures',
    py_modules=['mdx_figcaption'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)

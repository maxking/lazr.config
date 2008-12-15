# Copyright 2008 Canonical Ltd.  All rights reserved.

from setuptools import setup, find_packages

# generic helpers primarily for the long_description
def generate(*docname_or_string):
    res = []
    for value in docname_or_string:
        if value.endswith('.txt'):
            f = open(value)
            value = f.read()
            f.close()
        res.append(value)
        if not value.endswith('\n'):
            res.append('')
    return '\n'.join(res)
# end generic helpers

setup(
    name='lazr.config',
    version='1.0b1',
    namespace_packages=['lazr'],
    packages=find_packages('src'),
    package_dir={'':'src'},
    include_package_data=True,
    zip_safe=False,
    maintainer='LAZR Developers',
    maintainer_email='lazr-developers@lists.launchpad.net',
    description=open('README.txt').readlines()[0].strip(),
    long_description=generate(
        'src/lazr/config/README.txt',
        'src/lazr/config/CHANGES.txt'),
    license='LGPL v3',
    install_requires=[
        'setuptools',
        'zope.interface',
        'lazr.delegates',
        ],
    url='https://launchpad.net/lazr.config',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python"],
    )

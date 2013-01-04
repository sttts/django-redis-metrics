from os import path
from setuptools import setup, find_packages

from redis_metrics import VERSION


desc = ('django-redis-metrics is a Django application for '
        'tracking application metrics backed by Redis.')

f = open(path.join(path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='django-redis-metrics',
    version=".".join(map(str, VERSION)),
    description=desc,
    long_description=readme,
    author='Brad Montgomery',
    author_email='brad@bradmontgomery.net',
    url='https://github.com/bradmontgomery/django-redis-metrics',
    packages=find_packages(),
    package_dir={'redis_metrics': 'redis_metrics'},
    package_data={
        '': ['README.rst', 'LICENSE.txt'],
        'redis_metrics': [
            'templates/*',
        ]
    },
    include_package_data=True,
    install_requires=['django', 'redis'],
    tests_require=['mock'],
    license='LICENSE.txt',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
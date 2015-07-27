from setuptools import setup, find_packages
setup(
    name       = '6-Nimt',
    version    = '0.1',
    packages   = ['nimt6', 'nimt6.tests'],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Topic :: Games'
    ],
    test_suite = 'nimt6.tests'
)

from setuptools import setup

setup(
    name = 'hw_package',
    version = '0.1.0',
    author = 'Hallie Parten',
    author_email = 'zsk4gm@virginia.edu',
    packages = ['booklover', 'test'],
    url = 'https://github.com/hparten/hw_package',
    license = 'Creative Commons',
    description = 'An awesome package that tracks evolving changes to a reader's book list',
    long_description = open('README.txt').read()
)

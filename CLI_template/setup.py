"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from skele import __version__


this_dir = abspath(dirname(__file__))
# app description is fetched from README.md.
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

# this class is triggered whenever the command:
# $ python setup.py test
# is given.
class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=skele', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'skele',
    version = __version__,
    description = 'A skeleton command line program in Python.',
    long_description = long_description,
    url = '',
    author = 'Aldo Strofaldi',
    author_email = 'aldo.strofaldi@gmail.com',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    # extras required for tests only
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    # this defines what command has to be given in terminal to open our app.
    # by default, giving:
    # $ skele
    # triggers what is defined in main method of cli.py file.
    entry_points = {
        'console_scripts': [
            'skele=skele.cli:main',
        ],
    },
    # needed for execution of tests.
    cmdclass = {'test': RunTests},
)

## Description

This is a template to use in order to create a simple and powerful CLI program with Python.

### Installation

To install the CLI program, open a terminal in the app root folder and type the following command:

```console
$ pip install -e .
```
This will trigger the installation of the CLI program according to what is found in the
**setup.py** file.
If you want to install the program including the development dependencies (the ones required to execute
tests) the command to execute is:

```console
$ pip install -e .[test]
```

(**Remember to escape square bracket with \ if you use zsh!**)

### Usage

If you installed the development dependencies, you can run the app tests with the command:
```console
$ python setup.py test
```
This will trigger [py.test](http://pytest.org/latest/), along with its popular [coverage](https://pypi.python.org/pypi/pytest-cov) plugin.
Otherwise, if you just want to run the CLI app itself, you can type the following command:
```console
$ skele
```

The app entry point can be configured and customized inside the **setup.py** file.

#### Organization

The app is build around the python module [docopt](http://docopt.org/).
This module simplifies the building of a CLI app by just writing its *help* message, in the form of a Python documentation.
The structure of the CLI commands directly follows the most common conventions for CLI apps, and can be highly customized.
This is found in the **cli.py** file.
This file represents the main node of the application: whenever the app gets invoked in the terminal with the command:
```console
$ skele <command>
```
the application will match the given <command> with a python file contained in **commands** folder, which must have the same name
of the given command.
So, whenever a match occurs, the *run()* method of the matching file is executed.
In this way, whenever we need to add a new command, we just have to create a new Python file under **commands** folder, and write
its *run()* method in order to define what the app will do when this new command will be requested.


# Python Client Search Tool

This software is a basic application to show how a user can interact with the SPARC eco-system using the sparc.client Python library.
The application enables a user to search the SPARC Portal and perform operations on files.
The operations available in this simple application are:

* Download file,
* Export file to VTK; and
* Analyse file.

The analyse file functionality illustrates how a user may connect different tools in the SPARC eco-system to each other.

## Outline

The software is a PySide6 based application that uses *ui* files to construct a user interface.
The software has a simple build script that integrates with *pip* to create a usable package.

## Build User Interface

The user interface is built using *Qt Designer* and compiled to Python with the following command:

    pyside6-uic qt/retrieveportaldatawidget.ui -o src/ui_retrieveportaldatawidget.py

This command is suitable for a terminal type application and assumes the current directory is the root directory of this repository.
The user interface only needs to be compiled when changes are made to the source *ui* file, it does not in general require compiling.

## Install

The application can be installed into an existing Python environment with the following command:

    pip install .
 
Again, assuming that the current directory is the root directory of this repository.
It is quite often desirable to install the application in developer mode:

    pip install -e .

This is usually done if the user is intending on making changes to the code and wanting to run the code with these changes without having to re-install the application.
Both of these commands are given with respect to the current working directory being the root directory of the repository.

## Run

With the application installed it can be launched with the following command:

    sparc-search-tool
 
This command is available from any directory where the Python environment is available.

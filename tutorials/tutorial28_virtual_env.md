# Python Virtual Environment

## What is Python Virtual Environment?
- It is an isolated environment that contains necessary libraries (aka packages, modules, dependencies) that are 
specific to our prog. It is all you need to run your project. It doesn't affect your system or your other projects
- By itself, it is just a folder. However, once activated, it works like a sub-system. Once deactivated, it is just a folder
- A folder structure that gives us everything we need to run a light-weight yet isolated Python environment
- Contains a lot of files and folders that follow a tree structure

    - `bin/`: contain executable files of our virtual environment. The most notable are Python interpreter `python` and 
pip executable `pip` and their respective symlinks `python3`, `pip3`, etc.
    - `include/`: an initially empty folder Python uses for packages we might install later that depend on C extensions
    - `lib/` : the most important dir: it contains your libraries
    - `pyvenv.cfg`: crucial file for our virtual environment. It contains a couple of key-value pairs that Python uses 
to set variables to determine which Python interpreter and packages the current Python session uses
- In general, there are 3 essential parts of Python virtual environment:

    - A copy or a symlink of **Python Binary**
    - A **pyvenv.cfg** file
    - A **site-package directory**

## Create 

There are different ways to create a Python virtual environment. One of them is to use the following command with
`my_venv` is the name of the virtual env:

`python3 -m venv my_venv`

`venv` is a sub command (tool) of Python3

## Activate

After creating `my_venv`, we have to activate it (Note: it might be activated automatically after being created):

`source my_venv/bin/activate`

## Install packages
Now we can install packages into our virtual env. There are 2 ways of installation, one is using `pip` and the other one
is `pipenv`

- `pip install <package-name>@<version>`

  - e.g: `pip install ordered-set@3.2`
  - With `pip` command, we basically just install packages into our virtual env without documenting them in any specific
  file, unlike the `pipenv` command
  - We don't need to call `python3` or `pip3` explicitly since we already create a virtual environment using Python3.
  As long as our venv is active, `python` and `pip` are linked to the same executable files that `python3` and `pip3` do 


A more modern way to install packages into an env is to use `pipenv`. Beside installing, it also create 
2 files (`Pipfile` and `Pipfile.Lock`) to document the installed packages and their versions. A benefit of this fike
is for other developers to quickly install all the dependencies of a specific project.

- `pipenv install <package-name>@<version>`

  - This is a more efficient way to install packages to a virtual env. With `pipenv`, `Pipfile` and
  `Pipfile.Lock` will be automatically created. `Pipfile` stores all the installed packages to the prog, basically juts 
  the names and versions of packages; `Pipfile.Lock` stores some more details of the packages.
Once we share our prog with others, they just need to install `Pipfile` and then they have all packages needed for the prog

  - If a `Pipfile` already exist in a project, we can install the libs listed in it by running:
  `pipenv install` in the dir that contains the `Pipfile`


**NOTE:** We can install several packages at once by listing the packages' names in one command line

- e.g: `pip install pandas pyarrow venv-pack`


## Deactivate
If we want to exit/deactivate our current virtual environment, `my_venv`, use the following command:

`deactivate`

If we want to use `my_venv`, we just need to activate it again

We can also delete a virtual env, make sure to deactivate it first and then delete the folder


## Create `Pipfile` with `freeze` command

Assume tthat we have been using `pip` to install packages into an env and we don't have `Pipfile`.
To create a `Pipfile` follow the 2 steps below:

- Record the installed packages in the virtual env into a file:
  - `pip freeze > requirements.txt`
  
  - This step with the `freeze` command is to document/record all the installed packages into a file named `requirements.txt`


- Now, to create a Pipfile, run `pipenv install -r requirements.txt`

  - This may or may not reinstall the packages again because they are already in there. The goal is just to 
generate a Pipfile

  - Now we use `pipenv` to install the libs from this `requirements.txt` file. 
  A `Pipfile` and `Pipfile.Lock` will be created.

**Note:** `pip freeze` is just to print out the packages without pushing them into any file


## Why using venv?
- ### Avoid system pollution
  - To avoid mixing external packages/dependencies with the system-relevant packages  

- ### Avoid dependency conflicts

  - To avoid installing packages into only one place, then you CANNOT work with two different versions of the same library

      - For example: Installing 2 versions of Python into our global Python environment, the second installation overrides
  the first one. Therefore, we cannot have 2 versions of the same package in a single Python environment

- ### Minimize reproducibility issues

  - Without `my_venv`, we have to manually go through all the packages and pin needed packages for the project. 
  However, it's hard to do so since we don't know if the packages live in a single place.
  - With separate `my_venv`, it's a lot more straightforward to read requirements from the pinned dependencies of that `my_venv`

- ### Avoid installation privilege lockouts

  - Sometimes, we need to request to install packages into the host Python's site-package dir. Most of the time in 
  corporate work environment, we don't have that high-level access. Therefore, it's a lot easier to use a virtual environment,
  then we can create a new installation location within the scope of our privileges, which allows us to install and
  work with external packages



  


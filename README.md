[![Build Status](https://travis-ci.org/malrefai/todo.svg?branch=master)](https://travis-ci.org/malrefai/todo)
[![codecov](https://codecov.io/gh/malrefai/todo/branch/master/graph/badge.svg)](https://codecov.io/gh/malrefai/todo)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmalrefai%2Ftodo.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmalrefai%2Ftodo?ref=badge_shield)

# Todo App
Todo app is a ...

**Todo app** built with [Python][0]

## Technology Stack

- [Python][0]
- [Django][1]
- [Django REST framework][2]

## Installation Guide

### 1. Install [Python 3.6.*][3]

    # https://www.python.org/downloads/

### 2. Install virtualenv

	$ pip install virtualenv
	
### 3. Setup virtualenv

	# Create and activate virtual env
	$ virtualenv <ENV_DIR>
	$ . <ENV_DIR>/bin/activate
	
### 4. Fork the repository

    # Fork repository to your github account

### 5. Clone the repository

    # Create a project directory 
	# Clone todo repository into project directory
    $ git clone git@github.com:<GITHUB_ACCOUNT>/todo.git <YOUR_PROJECT_DIR>
    $ cd <YOUR_PROJECT_DIR>

### 6. Install dependencies

On the project root there is a requirements.txt file. 

Make sure you install all the required dependencies before running todo app

    $ pip install -r requirements.txt

### 7. Demo

    $ python manage.py runserver

## Copyright

Copyright (c) 2018 Mohammad Alrefai. See LICENSE.txt for further details.

## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmalrefai%2Ftodo.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmalrefai%2Ftodo?ref=badge_large)

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: http://www.django-rest-framework.org/
[3]: https://www.python.org/downloads/

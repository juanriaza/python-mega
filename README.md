# python-mega

[![Build Status](https://travis-ci.org/juanriaza/python-mega.png?branch=master)](https://travis-ci.org/juanriaza/python-mega)

## Overview

Wrapper around the [Mega API](https://mega.co.nz/#developers). Based on the work of [Julien Marchand](http://julien-marchand.fr/blog/using-mega-api-with-python-examples/).

## Installation

Install using `pip`, including any optional packages you want...
	
	$ pip install python-mega

...or clone the project from github.

    $ git clone git@juanriaza/python-mega.git
    $ cd python-mega
    $ pip install -r requirements.txt

## How to use it?

With your credentials:

```python
from mega import Mega

email = 'kim@dot.com'
password = 'olakase'

m = Mega.from_credentials(email, password)
```

…or you can use an ephemeral account:

```python
m = Mega.from_ephemeral()
```

And fire some requests:

```python
# list of files
files = m.get_files()
# download a file
m.download_file(file_id, file_key)
# upload a file
m.uploadfile('/home/kim/mega/secret_plans')
# download from an url
m.download_from_url('https://mega.co.nz/#!wYo3AYZC!Zwi1f3ANtYwKNOc07fwuN1enOoRj4CreFouuGqi4D6Y')
```

## Running the tests

    $ ./tests.py

## Changelog

### 0.1.0

**31th Jan 2012**

* First release.

## Acknowledgements

- Many thanks to Julien Marchand for the initial work.
- All of the [contributors](https://github.com/juanriaza/python-mega/blob/master/CONTRIBUTORS.md) to this project.

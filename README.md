# python-app-template

A ready to use python app template. Based on `pipenv`. 

## What's included

Simple python app stub with the following dev time helpers/checkers:

- [`black`](https://github.com/psf/black)
- [`bandit`](https://pypi.org/project/bandit/)
- [`flake8`](https://flake8.pycqa.org/en/latest/)
- [`mypy`](http://mypy-lang.org/)

all integrated with git commit hooks using [`pre-commit`](https://pre-commit.com/).

Additionally:

- Apache licence
- simple `setup.py`
- CHANGELOG.md

## How to use

Create a repo based on this one, then initialize `pipenv` (adjust python version):

```bash
pipenv --python 3.8
pipenv install --dev
```

and enable `pre-commit` hooks:

```bash
pipenv run pre-commit install
```

Edit your project information in `setup.py`.


# Ecommerce3
Env: Poetry, Tests: unittest

Another aproach to create some simple ecommerce service using TDD. Still I'm limited to use json files instead of database, but it's perfectly fine for training the
abilities to test aplications and manage virtual enviroments.
I will base all validations on raising Exceptions this time.
My goal is to use abstractions, try to get better understanding of SOLID principles, use unittest insted of pytest to learn mocks better. 
Still, tests will be run using pytest, but it's also interesting future to notice that you have choice to do it.
Also what I started to do more often is to use git, because this week I'll start to properly work with it on my course.



## Installation

  !ENTER MAIN DIRECTORY

First install poetry if u don't have it yet.
```bash
  pip install poetry
```

then set up virtual enviroment:

```bash
  poetry install
```

if for some reason you want to install it as it is production use:
```bash
  poetry install --sync
```


access enviroment

```bash
  poetry shell
```
    
## Running Tests

To run tests, run the following command from ecommerce3/tests

```bash
  poetry run pytest
```

## Tests Coverage

Not ready yet


## Authors

- [@DSmolke](https://www.github.com/DSmolke)

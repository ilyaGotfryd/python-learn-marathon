# Testing with Pytest
We are going to undertake a testing exercise using PyTest as our tool of choice.
In this session we will simultaniously look at conventions by which module is structured,
how Python path is processed and how pytest finds tests and modules.

Creating our module:
* create `src` folder and add empty `__init__.py` file to it
* create `string_calculator.py` in the `src` folder

Creating test suit:
* create `tests` folder in the root
* add `__init__.py` file to `tests` folder
* create `test_string_calculator.py` in `tests` folder

Install PyTest:
* Go over to console window
* run `pip install pytest`

To run your test suite from the root folder enter:
```bash
pytest tests
```

Let's add some fun to our TDD session:
* install pytest-xdist package by typing `pip install pytest-xdist` in console window.
* let pytest watch your tests and files as you change them `pytest -f tests`
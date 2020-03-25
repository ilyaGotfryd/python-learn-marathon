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

## To the exercise
 We are going to work through a TDD Kata called String Calculator. The idea is to add the following suite of tests and refactor our calculator as we go along to pass all the new and old tests as we add them.

 Implement these tests one by one, have the function fail, refactor function to pass current and all the previous tests:

 1) When I pass empty string into add function it returns 0
 2) When I pass a string with 0 into add function it returns int 0
 3) When I pass a string with a number into add function it returns that number as int
 4) When I pass two or more numbers separated by coma into the add function it returns a sum of those numbers
 5) When I pass a string starting with a delimiter character followed by `//` then the delimiter character is used instead of a comma and I get back an integer sum of numbers
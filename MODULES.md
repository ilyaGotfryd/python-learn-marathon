# Modules
As our code grows larger it is often useful to logically group code into separate files. Python packages and modules are exactly the mechanism to do that.

Let's create a function that does random selection for PC user in Rock Papper Scisors game.
```python
from random import choice
choices = ["Rock", "Papper", "Scisors"]

def pc_move():
  return choice(choices)
```

Let's add an entry point at the bottom.
```python
if __name__ == "__main__":
  result = pc_move()
  print(f"PC move was {result}")
```

## Python Path and Virtual Environment

Let's take a look at all the possible locations where it would be looking for a module. Go to console window and type in `python`. We have just opened Python in the current root folder. Add the following to look at the list of paths where Python is going to search.
```python
import sys
sys.path
```
Output has all the paths that this currently ran module is able to import from.

Let's `import nodules` and then see what `modules.choices` produces. 

Let's type `exit()` to get out of the interpreter. Let's take a quick look at python virtual environments. This is going to be MacOS and Linux specific, but Windows works relatively similarly.

In Console run `python -m venv .env` and let it simmer for a while. We have just created a virtual environment in .env folder under ourproject root folder. 
* list files in `.env`
* list files in `.env/bin/`
* see what libraries we have deployed globaly `pip freeze`
* run `which pip` and `which python` to see location of these files
* activate `source .env/bin/activate`
* see what libraries we have deployed in virtual env `pip freeze`
* run `which pip` and `which python` to see location of these files

Let's take a look at contents of Python Path. Run `python` from console. In interpreter enter:
```python
import sys
sys.path
```
look for `.env` in one of the paths.

## Debugging
Let's use `ipdb`. Run `pip install ipdb` to add that to our environment.

Add `import ipdb; ipdb.set_trace()` to the top of the modules file. Let's run `python modules.py` in console.

* l - show 10 lines around current point
* n - for next step
* s - step into function
* a - show passed in parameters
* variable name - to print current vale of the variable

## Creating a module
All that module in Python is in a long run is a separate python file that can be discovered via Python path from location of the script.

Let's move game logic functionality to a separate module `game.py` and import it in our `modules.py` file.

Imagine we have more items that will end up in the game logic and we want all of them to end up in a separate pacakge. Make `game` folder and move `game.py` there. In python 2.X we needed to have a `__init__.py` file in a given folder for python to consider it a pacakge. That is no longe the case. However some of the other packages still rely on that convention so let's add it. `__init__.py` file exists to initialize stuff before module gets imported.

Let's seed our random in there with miliseconds timestamp to ensure better random results.

Let's debug to see where the order of execution takes us.
# Explore the code

Even though you can run workflows without understanding what happens behind the scenes, you should avoid using Simmate like a [black box](https://en.wikipedia.org/wiki/Black_box). In this tutorial, you will learn how to explore Simmate's code and features, rather than just copying/pasting code from other tutorials.

1. [The quick tutorial](#the-quick-tutorial)
2. [The full tutorial](#the-full-tutorial)
    - [Getting help through Spyder](#getting-help-through-spyder)
    - [Introduction to Python Modules](#introduction-to-python-modules)
    - [Exploring Simmate's Modules](#exploring-simmates-modules)

> :warning: we have not added a documentation server yet, but will have either [sphinx](https://www.sphinx-doc.org/en/master/examples.html) or [pdoc](https://pdoc.dev/) implemented shortly

<br/><br/>

# The quick tutorial

For advanced users, we have README.rst files in each of our python modules -- so you can explore our source code on github just how you would explore documentation produced by sphinx. We do this because we are a high-level code and want to avoid researchers using it as a [black box](https://en.wikipedia.org/wiki/Black_box). Start by jumping to our [src/simmate directory](https://github.com/jacksund/simmate/tree/main/src/simmate) and scrolling down to read the page description.

<br/><br/>

# The full tutorial

> :bulb: This entire tutorial should be run on your local computer because we will be using Spyder.

<br/>

## Getting help through Spyder

Where we left off in Tutorial 3, we saw how to list all available properties and methods on an object. We did this by typing the object name plus a period (ex: `nacl_structure.`) and then hitting `tab`:

```python
from simmate.toolkit import Structure

nacl_structure = Structure.from_file("POSCAR")

nacl_structure.  # hit "tab" on your keyboard
```

> :warning: for this next part, pymatgen's documentation isn't always complete or beginner-friendly. This is why you won't see much. We're working on this at Simmate, so we hope this improves in the future. For now, don't expect too much guidance from the `Structure` class.

Now let's take a step back and get a full guide on a these methods and properties. We'll start with the `Structure` class that we previously imported using `from simmate.toolkit import Structure` and try the line `Structure?`:

```python 
from simmate.toolkit import Structure

Structure?  # <-- the ? here will bring up documentation help
```

What pops up is the documentation. Just like how we were using `--help` in the command-line for tutorial 1, we can use `?` in python to get help with python classes and objects!

We can also format this nicely using Spyder. In bottom part of Spyder's top-right window, select the `help` tab. And in the search bar (with "object") right next to it, type in `Structure`. You'll see the help information pop up again, but now it's nicely formatted for us.

Let's try this with our NaCl structure from before. Now try typing `nacl_structure.get_primitive_structure` in our help window. We can now see a description of what this does and the arguments/options ("Args") that it accepts.

You can also get this help information by typing `nacl_structure.get_primitive_structure` in the python terminal and then using the `ctrl+I` shortcut.

```python
nacl_structure.get_primitive_structure  # hit "ctrl+I" BEFORE hitting enter on this line
```

<br/>

## Introduction to Python Modules

One big question still remains though: how did we know to type `from simmate.toolkit import Structure`? Here, you should learn to think of python packages (such as Simmate) as many classes and functions organized into folders. 

As an example, you can read `from simmate.toolkit import Structure` as "Inside of the `simmate` folder, go to the `toolkit` file and load the `Structure` class". 

Here's a second example: `from simmate.toolkit.base_data_types.lattice import Lattice` is the same as saying "Go to the `simmate` folder --> `toolkit` folder --> `base_data_types` folder --> `lattice.py` file --> grab the `Lattice` class".

So whenever you see an `import` line, it's just telling you where the actual code is located. All of Simmate's code (and all python codes everywhere) is organized like this.

To prove it, let's go through these steps:

1. run `import simmate` in your python terminal
2. get the help docs for `simmate` in the Spyder help window using ctrl+I
3. on Simmate's github homepage, go the [src/simmate folder](https://github.com/jacksund/simmate/tree/main/src/simmate) (src = source code)
4. You should see the same thing! Also you'll see the `toolkit` folder that we were using before.
5. Navigate through the folders. `simmate` --> `toolkit` --> `base_data_types` --> `lattice.py`. 
6. You see a Lattice class where all of it's methods and properties are defined.

Each of these folders and files are referred to as python "modules" -- it's just python terminology.

<br/>

## Exploring Simmate's Modules

Now that we know Simmate is just a bunch of classes organized into folders, let's explore a bit.

We'll start with the `toolkit` module ([here](https://github.com/jacksund/simmate/tree/main/src/simmate/toolkit), but try finding it yourself without the link). When you open it up, you'll see an overview/guide. You can also access this module using `from simmate import toolkit` and getting help directly in spyder.

```
from simmate import toolkit

toolkit  # use ctrl+I before hitting enter
```

A good folder to look through is the `simmate.toolkit.creators` module, which provides many ways to create lattices, sites, and structures (e.g. randomly, random symmetry, etc.) and also incorporates third-party codes.

> :warning: because simmate is still at the early stages, some folders will be more complete than others. Keep this in mind while exploring. If you aren't seeing a guide or documentation, we probably haven't finished that module yet.

Take some time to look through the features and functions. Always feel free to ask if a feature exists, and if not, request one too. Post those questions in our [discussions page](https://github.com/jacksund/simmate/discussions/categories/q-a).

Once you're done exploring, you can move on to [the next tutorial](https://github.com/jacksund/simmate/blob/main/tutorials/05_Search_the_database.md).

<br/>

## Using the web docs

> :warning: we don't have our web server set up yet.

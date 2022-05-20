[FR]

# How to start the project

To start and run the tests:

```
$ git clone https://github.com/lumapps/test-goban.git
$ cd test-goban
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$pytest.
```

# Technical test

The theme of this test is the game of go.

The goal is to write a function that determines if the stone at position x, y on a goban is taken or not.

Vocabulary :

* Goban: the board on which stones are placed to play
* Shape: a group of one or more adjacent stones of the same color (adjacent: stones that are left, right, above, below each other, diagonals don't count)
* Freedom: empty space adjacent to a shape

Reminder of the rules:

1. The goban has an indefinite size
2. There are two players and each plays a stone color: black or white
3. The stones are placed one after the other in turn
5. When a form has no more freedom it is taken

The objective of the test is to write an `is_taken` function which takes x, y as 
a parameter and which returns true if the stone at position x, y is taken and false otherwise.
To do this function, we use a `get_status(x, y)` function which returns:

* Status.BLACK: when the stone at position x, y is black
* Status.WHITE: when the stone at position x, y is white
* Status.EMPTY: when there is no stone at position x, y
* Status.OUT: when position x, y is out of the goban


Complete the `Goban.is_taken` method with your solution 
(you can add parameters to the method if needed). 
This must respect the good practices of Python.
You can test your solution at any time with `py.test` (tests are in test_goban.py file).

Examples:

```
# = black
o = white
. = empty


.#.
#o# <= o is taken because it has no freedom, it has no adjacent empty space
.#.


...
#o# <= o is not taken because it has a freedom above
.#.


o# <= o is taken because it has no liberties (top and left are out of the goban so they are not liberties)
#.


oh.
##o <= the form # is taken because it has no freedom
o#o
.o.


oh.
##. <= the form # is not taken because it has freedom at x=2, y=1 (0, 0 top left)
o#o
.o.
```

---

[IN]

# How to launch the project

To start and launch tests:

```
$ git clone https://github.com/lumapps/test-goban.git
$ cd test-goban
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$pytest.
```

# Technical Test

The theme of this test is the game of go.

The goal is to write a function that determines whether the stone at an x, y position on a goban is taken or not.

Vocabulary:
- Goban: the board on which stones are placed to play
- Shape: a group of one or more adjacent stones of the same color (adjacent: stones that are left, right, top, bottom of each other, diagonals do not count)
- Freedom: empty space adjacent to a shape

Reminder of the rules:

1. The goban has an indefinite size
2. There are two players and everyone plays a stone color: black or white
3. The stones are laid one after the other each turn
4. When a form has no more freedom it is taken

The objective of the test is to write an is_taken function which takes in parameter x, y and which returns true if the stone with the position x, is taken there and false otherwise. To do this function we use a function get_status (x, y) which returns:

- Status.BLACK: when the stone at position x, y is black
- Status.WHITE: when the stone at the x position, y is white
- Status. EMPTY: when there is no stone at position x, y
- Status.OUT: when the position x, y is out of the goban

Complete the Goban.is_taken method with your solution 
(you can add parameters to the method if needed). 
This one must respect the good practices of Python. 
You can test your solution at any time with py.test 
(the tests are in the file test_goban.py).

Examples:
```
# = black
o = white
. =empty


. #.
# o # <= o is taken because she has no freedom, she has no adjacent empty space
. #.


...
# o # <= o is not taken because she has a freedom over
. #.


o # <= o is taken because she has no freedom (the top and the left are out of the goban so they are not freedoms)
#.


oh.
## o <= the form # is taken because it has no freedom
o o #
.o.


oh.
##. <= the form # is not taken because it has a freedom in x = 2, y = 1 (0, 0 on the top left)
o o #
.o.
```

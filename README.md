# Sheypoor Interview Task

## Task Description

Consider the following infinite sequence:
```
  0, 1, 1, 2, 3, 5, 8, 13, 12, 7, 10, 8, 9, ...
```
The **0th** element is `0` and the **1st** element is `1`. **Each of the next elements is equal to the sum of the digits
of the previous two elements.**
I must write a function that takes the number **`n`** (between **0** and **1,000,000,000**) as input and it
returns the **`nth`** member of the above sequence.

## Testing my script
You can run my script to get the nth sentence of above sequence simply what you see in the shell snippet below:
```
➜ sheypoor-interview git:(master) ✗ python main.py 
Enter a number between 0 and 1000000: 10
The value of sentence you're looking for is: 10
```

## Running Unit tests of my script
Also you can run some before-ready unit tests on my script to be sure about script simply what you see in the shell 
snippet below:
```
(venv) ➜  sheypoor-interview git:(master) ✗ python tests.py 

Test for a non-integer(float) number as number of sentence in the sequence
.
Test for a negative number as number of sentence in the sequence
.
Test for a non-integer(string) input as number of sentence in the sequence
.
Test for a negative number as number of sentence in the sequence
.
Test The 2nd sentence of sequence
.
Test The 6th sentence of sequence
.
Test The 10th sentence of sequence
.
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```

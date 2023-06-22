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
➜ sheypoor-interview git:(master) ✗ python tests.py 

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
### Time and Space Complexity of my script

The time complexity of the `find_nth_sentence` method is equal to **`O(n)`**, 
because in this method, a loop of length of **`n`** is executed, and for each round of the loop, two addition 
and division operations are performed, both of which have a complexity of **`O(1)`** 
And actually something similar to the picture below happens:
![](https://i.postimg.cc/T3n7RQ48/1-l-SNey-Lt-ALCPdm-HXr-Xeww-w.webp)

(Why we said the time complexity of`sum_digits(value)` is O(1) While there is a `while` loop in that method? That's 
becuase the max for sum of digits with mod of 10 is for example is 9 and 9 which means that the max of time complexity
of that method is 2 (**`O(1)`**)).

The memory complexity of `find_nth_sentence` function is also **`O(1)`**, because only a few variables are used to store
the input and output values of the function, and no larger data structures (such as `lists`) are used to store the data.

### Running with Docker
To run script with a default number (I've set `n = 10` in `main.py` module), you just need to run below command in
working directory of project:

```
➜ sheypoor-interview git:(master) ✗ docker-compose up
```

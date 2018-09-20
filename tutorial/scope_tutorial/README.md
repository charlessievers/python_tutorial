Scope Lesson
============

It is important to keep track of the scope of a variable.
```python
a = 5
```
a is a global variable.

Why is scope important?

Let's look at scope.py

The first thing you will see is
```python
def scope(a):
    b = 5
    a += b
    return a
```
This function will take in an argument, which we have named a.
The function then locally defines a variable b and sets it equal to 5 plus the value of a.
After setting local variable b, the function sets value of variable a to the value of b.
Finally the function returns a, which is 5.
After the function is finished the variable b loses scope and is removed.

Now let's ignore `if __name__ == "__main__":` for the time being.
Focus on the following.
```python
    number = 1
    print(number)
    new_number = scope(number)
    print(number, new_number)
```
We set the variable number to a value of 1.
Then we print this value.
Now we set a new variable, named new_number, to the value our scope function returns.
We then print both variables.
Notice how number stays 1, and new_number has the value of 6.
This may be intuitive to you, but number was passed to our scope function.
The scope function took the value and did not change the variable itself.
The local scope of the function did not affect the global variable.



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

Let's look at the scope class.
```python
class Scope:
    def __init__(self):
        self.scope = 'initialized'

    def local_change(self):
        scope = 'local_scope'

    def change_scope(self):
        self.scope = 'changed'

    def print_scope(self):
        print(self.scope)
```
Think of a class as a function which holds more functions. (Not always the case)
Here you can see that the class Scope has four functions, class functions are called methods.
__init__ is a reserved method name. This method will be called whenever an instance of Scope is initialized.
The first argument in the initialization method is the current instance of the class, which we have called self.
Any variables or objects within a class are called members. Within this class members have a `self.` in front of them.
The first member `self.scope` is defined when the class in initialized.

Now let's uncomment out the following block.
```python
#    new_scope = Scope()
#    new_scope.print_scope()
#
#    new_scope.local_change()
#    new_scope.print_scope()
#
#    new_scope.change_scope()
#    new_scope.print_scope()
```
The first line we create an instance of Scope() that we have called new_scope.
We will now use the print_scope method. To use a method, place `.method_name()` after the instantiated class.
Now let's try to out the local_change method. Did the method change the scope member? Why not?
Compare the local_change method to the change_scope method.

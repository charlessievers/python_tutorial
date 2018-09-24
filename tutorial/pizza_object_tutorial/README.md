Pizza Object
============

Take a moment to look over Pizza.py. This class creates a pizza object.
The initialization method initializes eight members.
Some of the members are even objects themselves, such as the list _crusts and the dictionaries.
Lists and dictionaries are both a type of class known as containers, because they hold other data types.
A dictionary is a container that holds data as a set of keys and values.

Take a moment to look over a few of the methods, we wont have time to get into all of them.
Hopefull,y the other methods will give you some ideas to help you implement future methods.
The point of this tutorial will be to make a new method that removes toppings from a pizza.

Think about why you might need to have a method to remove toppings.
Think about what members need to be changed if toppings change.
How should the output look if we uncommented out the following?
```python
    # pepperoni_pizza.add_topping('spinach')
    # pepperoni_pizza.remove_topping('spinach')
```

Pizza Store
===========

You may have noticed that our PizzaStore class has some unfinished methods.
We are going to fill in these methods and use them.
Before we do, let's talk about `if __name__ == "__main__":`
This line makes sure that the following code is run if and only if we run this .py file.
```python
    p1 = Pizza()
    p1.choose_crust('thin crust')
    p1.choose_size('large')
    p1.add_topping('pepperoni', 'yes')

    p2 = Pizza()
    p2.choose_crust('thick crust')
    p2.choose_size('medium')
    p2.add_topping('sausage')
    p2.add_topping('pepperoni')
    p2.add_topping('canadian bacon')
    p2.add_topping('ham')

    order1 = PizzaStore()
    order1.add_pizza(p1)
    order1.add_pizza(p2)
    try:
        order1.add_pizza('p3')
    except AttributeError:
        print('Zach says {} was not a Pizza'.format('p3'))
    order1.get_cost()
```
When we run Pizza_store.py, we don't want the following code to be run.
```python
    test_pizza = Pizza()
    test_pizza.list_crusts()
    test_pizza.list_sizes()
    test_pizza.list_toppings()

    pepperoni_pizza = Pizza()
    pepperoni_pizza.choose_crust('thin crust')
    pepperoni_pizza.choose_size('large')
    pepperoni_pizza.add_topping('pepperoni', 'yes')

    # pepperoni_pizza.add_topping('spinach')
    # pepperoni_pizza.remove_topping('spinach')

    print('\nThe pepperoni pizza is ${0:.2f}'.format(pepperoni_pizza.price))
```
If we had not placed that block of code  after `if __name__ == "__main__":` in Pizza.py then it would have been run.
This is because of the line `from Pizza import Pizza`

Notice that because we imported the class Pizza from Pizza.py, we now have access to it and all of its members.
This allows us to do the following:
```python
    p1 = Pizza()
    p1.choose_crust('thin crust')
    p1.choose_size('large')
    p1.add_topping('pepperoni', 'yes')

    p2 = Pizza()
    p2.choose_crust('thick crust')
    p2.choose_size('medium')
    p2.add_topping('sausage')
    p2.add_topping('pepperoni')
    p2.add_topping('canadian bacon')
    p2.add_topping('ham')
```
The ability to create tools to organize, store, and manipulate information, and import these tools to any other code is rather useful.
This is one of the main reasons why object oriented programming has been so impactful.


Now, let's fill in those empty methods!

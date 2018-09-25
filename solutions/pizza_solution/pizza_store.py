from Pizza import Pizza


class PizzaStore:

    def __init__(self):
        self.pizza_order = []
        self.cost = 0.00
        self._pn = None

    def add_pizza(self, pizza_name):
        if isinstance(pizza_name, Pizza):
            self.pizza_order.append(pizza_name)
        else:
            raise AttributeError()

    def get_cost(self):
        self.cost = 0.0
        for pizza in self.pizza_order:
            self.cost += pizza.price
        print('That will be ${0:.2f}'.format(self.cost))

    def order(self):
        if self._question("Would you like to order a pizza? (yes/no)") is False:
            print('Have a good day!')
            return
        self._pn = len(self.pizza_order)
        pizza = Pizza()
        self.add_pizza(pizza)
        self._make_pizza()
        while True:
            self._pn = len(self.pizza_order)
            if self._question("Would you like another pizza? (yes/no)") is False:
                self.get_cost()
                break
            else:
                pizza = Pizza()
                self.add_pizza(pizza)
                self._make_pizza()

    def _make_pizza(self):
        self._size()
        self._crust()
        self._toppings()
        while True:
            if self._changes() is False:
                break

    def _size(self):
        if self._question("Would you like to choose a size? (yes/no)") is False:
            self.pizza_order[self._pn].choose_size('medium')
            print('Medium is the default')
        else:
            size = input('What size would you like?')
            while True:
                try:
                    self.pizza_order[self._pn].choose_size(size)
                    break
                except AttributeError:
                    size = input('What size would you like?')

    def _crust(self):
        if self._question("Would you like to choose a crust? (yes/no)") is False:
            self.pizza_order[self._pn].choose_crust('hand tossed')
            print('Hand tossed is the default')
        else:
            crust = input('What crust would you like?')
            while True:
                try:
                    self.pizza_order[self._pn].choose_crust(crust)
                    break
                except AttributeError:
                    crust = input('What crust would you like?')

    def _toppings(self):
        if self._question("Would you like to choose a topping? (yes/no)") is False:
            print('Cheese is the default')
        else:
            self._topping()

    def _topping(self):
        topping = input('What topping would you like?')
        while True:
            try:
                self.pizza_order[self._pn].add_topping(topping)
                if self._question('Would you like another topping? (yes/no)') is False:
                    break
                else:
                    self._topping()
            except AttributeError:
                topping = input('What topping would you like?')

    def _changes(self):
        if self._question("Would you like to make any changes? (yes/no)") is False:
            return False
        else:
            change = input('Would you like to change the size, crust, or toppings?')
            while True:
                try:
                    self._check_change(change)
                    break
                except AttributeError:
                    change = input('Would you like to change the size, crust, or toppings?')
            if change == 'size':
                self._change_size()
                return True
            if change == 'crust':
                self._change_crust()
                return True
            if change == 'toppings':
                self._change_topping()
                return True

    def _check_change(self, change):
        if change != 'size' and change != 'crust' and change != 'toppings':
            raise AttributeError('You must select size, crust, or toppings to change')

    def _change_size(self):
        size = input('What size would you like?')
        while True:
            try:
                self.pizza_order[self._pn].change_size(size)
                break
            except AttributeError:
                size = input('What size would you like?')

    def _change_crust(self):
        crust = input('What crust would you like?')
        while True:
            try:
                self.pizza_order[self._pn].change_crust(crust)
                break
            except AttributeError:
                crust = input('What crust would you like?')

    def _change_topping(self):
        topping = input('What topping would you like to remove?')
        while True:
            try:
                self.pizza_order[self._pn].remove_topping(topping)
                break
            except AttributeError:
                topping = input('What topping would you like to remove?')
        if self._question("Would you like to add a topping? (yes/no)") is False:
            return
        else:
            self._topping()

    def _question(self, input_question, boolean=None):
        if boolean is None:
            boolean = input(input_question)
        else:
            boolean = input("Please type yes or no")
        if boolean == 'yes' or boolean == 'Yes':
            return True
        elif boolean == 'no' or boolean == 'No':
            return False
        else:
            return self._question(boolean)


if __name__ == "__main__":

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

    order2 = PizzaStore()
    order2.order()

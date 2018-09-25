class Pizza:

    def __init__(self):
        self.size = None
        self.crust = None
        self.servings = None
        self.price = 0.00
        self._crusts = ['hand tossed', 'stuffed crust', 'thin crust', 'thick crust']
        self._sizes = {'large': 13.00, 'medium': 10.00, 'small': 7.00}
        self.toppings = dict()
        self._toppings_list = {'sauce': 0.00, 'cheese': 0.00, 'pepperoni': 0.50, 'canadian bacon': 0.50,
                               'ham': 0.50, 'anchovies': 0.50, 'olive': 0.50, 'pineapple': 0.50, 'onions': 0.50,
                               'garlic': 0.50, 'sausage': 0.50, 'mushrooms': 0.50, 'spinach': 0.50, 'basil': 0.25}
        # defaults
        self.add_topping('sauce')
        self.add_topping('cheese')

    def list_sizes(self):
        print('\nSizes:')
        for size in self._sizes:
            print('{}'.format(size), 'for ${0:.2f}'.format(self._sizes[size]))

    def choose_size(self, size):
        if size == 'large':
            self.size = 'large'
            self.price += 13.00
            self.servings = 7
        elif size == 'medium':
            self.size = size
            self.price += 10.00
            self.servings = 5
        elif size == 'small':
            self.size = size
            self.price += 7.00
            self.servings = 3
        else:
            print('Pizza sizes are')
            for size_type in self._sizes:
                print(size_type)
            raise AttributeError('Zach says {} was Not Found'.format(size))

    def change_size(self, size):
        if self.size is None:
            raise AttributeError('Zach says size has not been chosen')
        if self.size in self._sizes:
            self.price -= self._sizes[self.size]
        self.choose_size(size)

    def list_crusts(self):
        print('\nCrusts:')
        for crust in self._crusts:
            if crust == 'stuffed crust':
                print('stuffed crust for $2.00')
            else:
                print('{}'.format(crust))

    def choose_crust(self, crust):
        if crust in self._crusts:
            self.crust = crust
        else:
            print('Crust types are:')
            for crust_type in self._crusts:
                print(crust_type)
            raise AttributeError('Zach says {} was Not Found'.format(crust))
        if self.crust == 'stuffed crust':
            self.price += 2.00

    def change_crust(self, crust):
        if self.crust is None:
            raise AttributeError('Zach says crust has not been chosen')
        if self.crust == 'stuffed crust':
            self.price -= 2.00
        self.choose_crust(crust)

    def list_toppings(self):
        print('\nToppings:')
        for topping in self._toppings_list:
            print('{}'.format(topping), 'for ${0:.2f}'.format(self._toppings_list[topping]))
        print('extra is double the price')

    def current_toppings(self):
        if len(self.toppings) == 0:
            print('No toppings selected')
        print('Toppings are:')
        for topping in self.toppings:
            print(topping)

    def add_topping(self, topping, extra='no'):
        if extra != 'yes' and extra != 'no':
            raise ValueError('Extra must be yes or no')
        if topping in self.toppings:
            if self.toppings[topping] == 'yes':
                print('extra {} has already been set'.format(topping))
            else:
                self.toppings[topping] = 'yes'
                self.price += self._toppings_list[topping]
        elif topping in self._toppings_list:
            self.toppings[topping] = extra
            if extra == 'yes':
                self.price += self._toppings_list[topping]*2
            else:
                self.price += self._toppings_list[topping]
        else:
            self.list_toppings()
            raise AttributeError('Zach says {} was Not Found'.format(topping))

    def remove_topping(self, topping, extra='no'):
        if extra != 'yes' and extra != 'no':
            raise AttributeError('Extra must be yes or no')
        if topping in self.toppings:
            if self.toppings[topping] == 'yes':
                if extra == 'yes':
                    self.price -= self._toppings_list[topping] * 2
                    self.toppings.pop(topping, None)
                else:
                    self.price -= self._toppings_list[topping]
                    self.toppings[topping] = 'no'
            else:
                if extra == 'no':
                    self.price -= self._toppings_list[topping]
                    self.toppings.pop(topping, None)
                else:
                    print('Extra {} was not set, but was still removed'.format(topping))
                    self.price -= self._toppings_list[topping]
                    self.toppings.pop(topping, None)
        else:
            raise AttributeError('That was not a topping!')

    def what_toppings(self):
        for topping in self.toppings:
            print(topping)

if __name__ == "__main__":

    test_pizza = Pizza()
    test_pizza.list_crusts()
    test_pizza.list_sizes()
    test_pizza.list_toppings()

    pepperoni_pizza = Pizza()
    pepperoni_pizza.choose_crust('thin crust')
    pepperoni_pizza.choose_size('large')
    pepperoni_pizza.add_topping('pepperoni', 'yes')

    pepperoni_pizza.add_topping('spinach')
    pepperoni_pizza.remove_topping('spinach')

    print('\nThe pepperoni pizza is ${0:.2f}'.format(pepperoni_pizza.price))

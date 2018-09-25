from Pizza import Pizza


class PizzaStore:

    def __init__(self):
        self.pizza_list = []

    def add_pizza(self, pizza_name):
        if isinstance(pizza_name, Pizza):
            self.pizza_list.append(pizza_name)
        else:
            raise AttributeError()

    def get_cost(self):
        self.cost = 0.00
        for pizza in self.pizza_list:
            self.cost += pizza.price
        print('That will be ${0:.2f}'.format(self.cost))


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
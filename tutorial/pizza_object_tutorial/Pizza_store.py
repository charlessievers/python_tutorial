from Pizza import Pizza


class PizzaStore:

    def __init__(self):
        return

    def add_pizza(self, pizza_name):
        return

    def get_cost(self):
        return

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
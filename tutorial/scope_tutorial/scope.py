
def hello(a):
    b = 5
    a += b
    return a


class Scope:
    def __init__(self):
        self.scope = 'initialized'

    def local_change(self):
        scope = 'local_scope'

    def change_scope(self):
        self.scope = 'changed'

    def print_scope(self):
        print(self.scope)

if __name__ == "__main__":

    number = 1
    print(number)
    new_number = hello(number)
    print(number, new_number)

    new_scope = Scope()
    new_scope.print_scope()

    new_scope.local_change()
    new_scope.print_scope()

    new_scope.change_scope()
    new_scope.print_scope()



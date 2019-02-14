class Product(object):
    products_count = 0

    def __init__(self, price):
        self._price = price
        self._code = Product.products_count
        Product.products_count += 1

    def get_code(self):
        return self._code

    def get_price(self):
        return self._price

    def get_total_price(self):
        return self._price + 0.07 * self._price

    def __str__(self):
        return str(self._code) + ' ' + str(self.get_total_price()) + ' CHF'


class OnlineStore(object):
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        self._products[product.get_code()] = product

    def sell_product(self, code):
        if not code in self._products:
            raise Exception('Product with code ' + str(code) + ' does not exist!')
        del self._products[code]

    def print_products(self):
        total = 0
        for product in self._products.values():
            print(product)
            total += product.get_total_price()
        print('Total price: %.2f' % total)


class SpecialProduct(Product):

    def __init__(self, price, name):
        Product.__init__(self, price)
        self._name = name

    def get_total_price(self):
        tax = 0.05 * self.get_price()
        if tax > 10:
            tax = 10

        return self.get_price() + tax

    def __str__(self):
        return self._name + ' ' + super(SpecialProduct, self).__str__()


store = OnlineStore()
p1 = Product(50)
p2 = Product(100)
print(p1)  # prints 0 53.5 CHF
print(p2)  # prints 1 107.0 CHF

store.add_product(p1)
store.add_product(p2)

sp1 = SpecialProduct(200, "sp1")
sp2 = SpecialProduct(100, "sp2")

store.print_products()
# prints the following lines:
# 0 53.5 CHF
# 1 107.0 CHF
# sp1 2 210.0
# sp2 3 105.0
# Total price: 475.50
store.sell_product(sp1.get_code())
store.print_products()
# prints the following lines:
# 0 53.5 CHF
# 1 107.0 CHF
# sp2 3 105.0
# Total price: 265.50
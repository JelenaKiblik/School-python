"""Store imitation."""


class ProductCannotBeSold(Exception):
    """Exception."""

    def __init__(self, message):
        """Exception, which is raised when a full stack is attempted to put an element."""
        super().__init__(message)


class Product:
    """Represents product model."""

    def __init__(self, name: str, price: int) -> None:
        """
        Class constructor. Each product has name and price.

        :param name: product name
        :param price: product price
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Product object representation in string format.

        :return: string
        """
        return f"Product: {self.name}, price: {self.price}"

    def __repr__(self) -> str:
        """
        Product object representation in object format.

        :return: string
        """
        return f"{self.name}"


class Customer:
    """Represents customer model."""

    def __init__(self, name: str, age: int, money: int) -> None:
        """
        Class constructor. Each customer has name, age and money when being created.

        Customer also has storage for bought items.
        :param name: customer's name
        :param age: customer's age
        :param money: customer's money
        """
        self.name = name
        self.age = age
        self.money = money
        self.products = []

    def add_item(self, product: Product, amount: int) -> None:
        """
        Add bought items to customer's items.

        :param product: product
        :param amount: amount
        """
        self.products.append(product, amount)

    def pay(self, money_to_pay: int) -> None:
        """
        Check if customer has enough money to pay for the product.

        Returns nothing, but raises exception if customer has not enough money to pay.
        In other case reduces amount of customer's money.
        :param money_to_pay: money amount needed to be paid
        """
        money_to_pay = self.amount
        if money_to_pay < self.money:
            raise ProductCannotBeSold("You do not have enough money to pay for chosen product!")
        else:
            self.money -= money_to_pay

    def __str__(self) -> str:
        """
        Customer object representation in string format.

        :return: string
        """
        return f" {self.name}'s items: {Customer[product]}; money: {money}"


class Store:
    """Represents store model."""

    def __init__(self) -> None:
        """Class constructor."""
        self.products = []
        self.money = 0

    def buy(self, product: Product, amount: int, customer: Customer) -> str:
        """
        Represent how customer buys product.

        :param product: product the customer wants
        :param amount: pieces of product
        :param customer: customer who wants to buy
        :return: message
        """
        pass

    def allowed_to_buy(self, product: Product, customer: Customer):
        """
        Check if customer is allowed to buy some particular products.

        Permission depends on customer's age

        Customers under 18 are not allowed to buy beer and tobacco.
        Must raise exception if customer has no permission to buy chosen product.
        :param product: product to buy
        :param customer: customer who makes the purchase
        """
        pass

    def check_product_availability(self, product: Product, amount: int):
        """
        Check if chosen amount of product is present in stock.

        Must raise exception if no product found or not enough in stock.
        :param product: product to be bought
        :param amount: amount of product
        """
        pass

    def add_product(self, product: Product) -> None:
        """
        Adding product to store.

        :param product:  product name
        """
        self.product = product

    def __str__(self) -> str:
        """
        Store object representation in string format.

        :return: string
        """
        return f"Store items: {self.add_product()}; store money: {self.money}."


if __name__ == "__main__":
    # print(Product("Toy", 10))  # Product: Toy, price: 10
    # print([Product("Toy", 10), Product("Adult Toy", 20)])  # [Toy, Adult Toy]
    john = Customer("John", 20, 300)
    bobby = Customer("Bobby", 17, 150)
    sandy = Customer("Sandy", 12, 100)

    store = Store()

    beer = Product("beer", 50)
    water = Product("water", 30)
    choco = Product("chocolate", 45)
    pretzel = Product("pretzel", 35)

    # store.add_product(beer)
    # store.add_product(water)
    # for _ in range(3):
    #     store.add_product(choco)
    #     store.add_product(pretzel)
    #
    # print(store.buy(beer, 1, john))  # -> Thank you for the purchase!
    # print(beer not in store.products)  # -> True
    # print(john)  # -> John's items: beer; money: 250.
    #
    # tobacco = Product("tobacco", 55)
    # store.add_product(tobacco)
    # print(store.buy(tobacco, 1, bobby))  # -> You are too young to buy Product: tobacco, price: 55!
    #
    # print(store.buy(water, 2, sandy))  # -> Item is not available in chosen amount!
    #
    # candy = Product("candy", 25)
    # print(store.buy(candy, 1, bobby))  # -> Item not found!
    #
    # store.buy(choco, 2, bobby)
    # print(bobby.money)  # -> 60
    # store.buy(water, 1, bobby)
    # print(bobby)  # -> Bobby's items: chocolate(2), water; money: 30

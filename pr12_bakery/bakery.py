"""PR12 Bakery."""


class Baker:
    def __init__(self, name: str, experience_level: int, money: int):
        self.name = name
        self.experience_level = experience_level
        self.money = money


class Pastry:
    def __init__(self, name: str, complexity_level: int):
        self.name = name
        self.complexity_level = complexity_level


class Bakery:
    def __init__(self, name: str, min_experience_level: int, budget: int):
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.bakers = []

    def add_baker(self, baker: Baker) -> Baker:
        if isinstance(baker, Baker) and baker.experience_level >= self.min_experience_level:
            self.bakers.append(baker)
            set(self.bakers)
            return baker
        return None

    def remove_baker(self, baker: Baker):
        self.baker = baker
        for baker in self.bakers:
            self.bakers.remove(baker)

    def add_recipe(self, name: str):
        #calculate cost
        #1) enough money?
        #2) recipe not in bakery yet
        #3) enough bakers?
        #remove money
        #calculate complexity
        #add recipe to dict where key is name value is complexity
        pass

    def make_order(self, name: str) -> Pastry:
        # 1)check if recipe exist
        # 2) find baker
        # loop over bakers
        # if given baker xp is enough:
        #       add baker to list
        #   find the baker with the lower xp in the list

        # loop over bakers:
        #   if baker.xp < enough
        #       if baker.xp < current_lowest:
        #           memorize this baker

        # baker.xp += len(name)
        # calculate profit => bakery, baker
        # store Pastry
        # return Pastry
        pass

    def get_recipes(self) -> dict:
        return self.recipes

    def get_pastries(self) -> list:
        # sorted()
        # order by pastry.complexity_level
        pass

    def get_bakers(self) -> list:
        # order by baker.experience level, descending
        pass


if __name__ == '__main__':

    bakery1 = Bakery("Pagariposid", 10, 100)
    print(bakery1)  # Bakery Pagariposid: 0 baker(s)

    # bakery1.add_baker(Baker("Ago", 9, 0))
    # print(bakery1)  # Bakery Pagariposid: 0 baker(s) => Baker Ago was not added because of low experience level (Sorry Ago)
    #
    # print(bakery1.make_order("cake"))  # None => No such recipe nor baker in bakery
    #
    # ########################################################################

    polly = Baker("Polly", 10, 5)
    sam = Baker("Sam", 11, 0)
    emma = Baker("Emma", 12, 6)

    bakery1.add_baker(polly)
    bakery1.add_baker(sam)
    bakery1.add_baker(emma)
    #
    # # Trying to make order when no recipes are in bakery
    #
    # print(bakery1.make_order("cake"))  # None
    #
    # bakery1.add_recipe("cake")
    # print(bakery1.budget)  # 96 (100 - len('cake') = 96 => price for recipe)
    # print(bakery1.get_recipes())  # {'cake': 2}
    #
    # print(bakery1.make_order("cake"))  # cake
    # print(
    #     bakery1.get_bakers())  # [Baker: Polly(14), Baker: Emma(12), Baker: Sam(11)] =>
    # # Polly was chosen to be the baker because 'cake' complexity and Polly experience lever were the closest
    # # Polly experience level was increased by len('cake') => 10 + 4 = 14
    #
    # print(bakery1.budget)  # 104 (used to be 96: 96 + len('cake') * 2 = 104)
    # print(polly.money)  # 13 (5 she had + len('cake') * 2 = 13)
    #
    # print(bakery1.get_pastries())  # [cake] ("NB! cake is instance of class Pastry, not a string)
    #
    # ########################################################################
    #
    # bakery2 = Bakery("Pihlaka", 11, 100)
    #
    # john = Baker("John", 11, 5)
    # megane = Baker("Megane", 17, 4)
    # kate = Baker("Megane", 18, 8)
    #
    # bakery2.add_baker(john)
    # bakery2.add_baker(megane)
    # bakery2.add_baker(kate)
    #
    # bakery2.add_recipe("muffin")
    # bakery2.add_recipe("cupcake")
    # bakery2.add_recipe("biscuits")
    #
    # print(bakery2.get_recipes())  # {'muffin': 7, 'cupcake': 10, 'biscuits': 13}
    #
    # print(
    #     bakery2.get_bakers())  # [Baker: Megane(18), Baker: Megane(17), Baker: John(11)]
    # bakery2.make_order("biscuits")
    # print(
    #     bakery2.get_bakers())  # [Baker: Megane(25), Baker: Megane(18), Baker: John(11)]
    # # Magane was chosen to be the baker as the most closest experience (which is also greater than complexity) was 17.

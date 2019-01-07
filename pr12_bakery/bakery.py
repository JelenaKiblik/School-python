"""PR12 Bakery."""


class Baker:
    """Class Baker."""

    def __init__(self, name: str, experience_level: int, money: int):
        """Constructor."""
        self.name = name
        self.experience_level = experience_level
        self.money = money

    def __repr__(self) -> str:
        """
        Baker object representation in string format.

        :return: string
        """
        return f"Baker: {self.name}({self.experience_level})"


class Pastry:
    """Class Pastry."""

    def __init__(self, name: str, complexity_level: int):
        """Constructor."""
        self.name = name
        self.complexity_level = complexity_level

    def __repr__(self) -> str:
        """
        Pastry object representation in string format.

        :return: string
        """
        return f"{self.name}"


class Recipe:
    """Class Recipe."""

    def __init__(self, name: str, complexity_level: int):
        """Constructor."""
        self.name = name
        self.complexity_level = complexity_level


class Bakery:
    """Class Bakery."""

    def __init__(self, name: str, min_experience_level: int, budget: int):
        """Constructor."""
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.bakers = {}
        self.pastries = []
        self.recipes = {}

    def add_baker(self, baker: Baker) -> Baker:
        """Add baker."""
        if baker.experience_level >= self.min_experience_level:
            self.bakers[baker] = baker.experience_level
            return baker

    def remove_baker(self, baker: Baker):
        """Remove baker."""
        if baker in self.bakers:
            del self.bakers[baker]

    def add_recipe(self, name: str):
        """Add recipe."""
        price = len(name)
        if len(self.bakers) == 0:
            return None
        if self.budget - price < 0:
            return None
        if name in self.recipes:
            return None
        self.budget -= price
        complexity_level = abs(price * len(self.bakers) - min(self.bakers.values()))
        self.recipes[name] = complexity_level
        return complexity_level

    def make_order(self, name: str) -> Pastry:
        """Make order."""
        if name not in self.recipes:
            return
        if self.recipes[name] >= max(self.bakers.values()):
            return
        required_exp = self.recipes[name]
        closest_exp = max(self.bakers.values())
        baker = list(self.bakers.keys())[list(self.bakers.values()).index(closest_exp)]
        for cook, exp in self.bakers.items():
            if required_exp == exp:
                baker = cook
                break
            if exp - required_exp > 0 and (closest_exp - required_exp) > (exp - required_exp):
                closest_exp = exp
                baker = cook
        baker.experience_level += len(name)
        self.bakers[baker] += len(name)
        income = len(name) * 4
        baker.money += int(0.5 * income)
        self.budget += int(0.5 * income)
        self.min_experience_level += 1
        self.pastries.append(Pastry(name, required_exp))
        return Pastry(name, required_exp)

    def get_recipes(self) -> dict:
        """Get recipes."""
        return self.recipes

    def get_pastries(self) -> list:
        """Get pastries."""
        return sorted(self.pastries, key=lambda k: k.complexity_level, reverse=True)

    def get_bakers(self) -> list:
        """Get bakers."""
        return sorted(self.bakers, key=lambda k: k.experience_level, reverse=True)

    def __repr__(self) -> str:
        """
        Bakery object representation in string format.

        :return: string
        """
        return f"Bakery {self.name}: {len(self.bakers)} baker(s)"


if __name__ == '__main__':

    bakery1 = Bakery("Pagariposid", 10, 100)
    bakery1.add_baker(Baker("Ago", 9, 0))
    print(bakery1)  # Bakery Pagariposid: 0 baker(s) => Baker Ago was not added because of low experience level (Sorry Ago)

    print(bakery1.make_order("cake"))  # None => No such recipe nor baker in bakery

    ########################################################################

    polly = Baker("Polly", 10, 5)
    sam = Baker("Sam", 11, 0)
    emma = Baker("Emma", 12, 6)

    bakery1.add_baker(polly)
    bakery1.add_baker(sam)
    bakery1.add_baker(emma)

    # Trying to make order when no recipes are in bakery

    print(bakery1.make_order("cake"))  # None

    bakery1.add_recipe("cake")
    print(bakery1.budget)  # 96 (100 - len('cake') = 96 => price for recipe)
    print(bakery1.get_recipes())  # {'cake': 2}

    print(bakery1.make_order("cake"))  # cake
    print(
        bakery1.get_bakers())  # [Baker: Polly(14), Baker: Emma(12), Baker: Sam(11)] =>
    # Polly was chosen to be the baker because 'cake' complexity and Polly experience lever were the closest
    # Polly experience level was increased by len('cake') => 10 + 4 = 14

    print(bakery1.budget)  # 104 (used to be 96: 96 + len('cake') * 2 = 104)
    print(polly.money)  # 13 (5 she had + len('cake') * 2 = 13)

    print(bakery1.get_pastries())  # [cake] ("NB! cake is instance of class Pastry, not a string)

    ########################################################################

    bakery2 = Bakery("Pihlaka", 11, 100)

    john = Baker("John", 11, 5)
    megane = Baker("Megane", 17, 4)
    kate = Baker("Megane", 18, 8)

    bakery2.add_baker(john)
    bakery2.add_baker(megane)
    bakery2.add_baker(kate)

    bakery2.add_recipe("muffin")
    bakery2.add_recipe("cupcake")
    bakery2.add_recipe("biscuits")

    print(bakery2.get_recipes())  # {'muffin': 7, 'cupcake': 10, 'biscuits': 13}

    print(
        bakery2.get_bakers())  # [Baker: Megane(18), Baker: Megane(17), Baker: John(11)]
    bakery2.make_order("biscuits")
    print(
        bakery2.get_bakers())  # [Baker: Megane(25), Baker: Megane(18), Baker: John(11)]
    # Magane was chosen to be the baker as the most closest experience (which is also greater than complexity) was 17.

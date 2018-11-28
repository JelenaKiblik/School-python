"""EX12 - Gym."""


class Gym:
    """Class Gym."""

    def __init__(self, name: str, max_members_number: int):
        """Constructor."""
        self.name = name
        self.max_members_number = max_members_number
        self.members = []

    def add_member(self, member: Member) -> Member:
        """Add member."""
        if isinstance(member, Member) and (self.can_add_member(member) is True):
            self.members.append(member)
            return member
        return None

    def can_add_member(self, member: Member) -> bool:
        """Can add member."""
        if isinstance(member, Member) and member not in self.members and len(self.members) <= self.max_members_number:
            return True
        else:
            return False

    def remove_member(self, member: Member):
        """Remove member."""
        if isinstance(member, Member):
            self.members.remove(member)

    def get_total_stamina(self) -> int:
        """Get total stamina."""
        pass

    def get_members_number(self) -> int:
        """Get members number."""
        pass

    def get_all_members(self) -> list:
        """Get all members."""
        pass

    def get_average_age(self) -> float:
        """Get average age."""
        pass

    def __repr__(self) -> str:
        """
        Gym object representation in string format.

        :return: string
        """
        return f"Gym {self.name} : {len(self.members)} member(s)"


class Member:
    """Class Member."""

    def __init__(self, name: str, age: int, trainers: Trainers):
        """Constructor."""
        self.name = name
        self.age = age
        self.trainers = trainers

    def get_all_gyms(self) -> list:
        """Get all gyms."""
        pass

    def get_gyms(self) -> list:
        """Get gyms."""
        pass

    # NB! LISADA TULEB JUURDE HÄSTI  LIHTNE   FUNKTSIOON ^ _ ^

    def __repr__(self) -> str:
        """
        Member object representation in string format.

        :return: string
        """
        return f"{self.name}, {self.age}: {self.trainers}"


class Trainers:
    """Class Trainers."""

    def __init__(self, stamina: int, color: str):
        """Constructor."""
        self.staminа = stamina
        self.color = color

    def __repr__(self) -> str:
        """
        Trainers object representation in string format.

        :return: string
        """
        return f" Trainers: [{self.stamina}, {self.color}]"


class City:
    """Class City."""

    def __init__(self, max_gym_number: int):
        """Constructor."""
        self.max_gym_number = max_gym_number

    def build_gym(self, gym: Gym) -> Gym:
        """Build gym."""
        if isinstance(gym, Gym):
            return gym

    def can_build_gym(self) -> bool:
        """Can build gym."""
        pass

    def destroy_gym(self):
        """Destroy gym."""
        pass

    def get_max_members_gym(self) -> list:
        """Get max members gym."""
        pass

    def get_max_stamina_gyms(self) -> list:
        """Get max stamina gyms."""
        pass

    def get_max_average_ages(self) -> list:
        """Get max average ages."""
        pass

    def get_min_average_ages(self) -> list:
        """Get min average ages."""
        pass

    def get_gyms_by_trainers_color(self, color: str) -> list:
        """Get gyms by trainers color."""
        pass

    def get_gyms_by_name(self, name: str) -> list:
        """Get gyms by name."""
        pass

    def get_all_gyms(self) -> list:
        """Get all gyms."""
        pass


if __name__ == "__main__":
    city1 = City(100)
    gym = Gym("TTÜ Sport", 50)
    city1.build_gym(gym)

    trainers1 = Trainers(50, "blue")
    trainers2 = Trainers(50, "grey")

    member = Member("Ago Luberg", 35, trainers1)
    member2 = Member("Ahti Lohk", 35, trainers2)

    gym.add_member(member)
    gym.add_member(member2)

    print(gym.get_members_number())  # 2

    print(gym.get_all_members())  # [Ago Luberg, 35: Trainers: [50, blue], Ahti Lohk, 35: Trainers: [50, grey]]

    gym.add_member(member)  # Trying to add Ago again
    print(gym.get_members_number())  # 2 //We can't...

    for i in range(48):
        gym.add_member(Member("Tudeng Tudeng", 20, Trainers(49, "blue")))

    print(gym.get_members_number())  # 50

    trainers3 = Trainers(60, "blue")
    member_new = Member("Megane", 19, trainers3)
    gym.add_member(member_new)

    print(
        gym.get_members_number())  # 3 -> Ago, Ahti and Megan, all others were removed because of the lowest trainers' stamina

    city2 = City(10)
    city2.build_gym(Gym("MyFitness", 100))
    city2.destroy_gym()

    for i in range(9):
        city2.build_gym(Gym("Super Gym", 10))

    print(city2.can_build_gym())  # False -> Cannot build gym, city is full of them

    #######################################################################################

    city3 = City(100)

    gym4 = Gym("Sparta", 50)
    gym5 = Gym("People Fitness", 30)
    gym6 = Gym("Gym Eesti", 100)

    city3.build_gym(gym4)
    city3.build_gym(gym5)
    city3.build_gym(gym6)

    gym4.add_member(Member("Bob", 18, Trainers(50, "black")))
    gym4.add_member(Member("Emma", 20, Trainers(70, "red")))
    gym4.add_member(Member("Ken", 25, Trainers(40, "grey")))

    gym5.add_member(Member("Merili", 18, Trainers(100, "pink")))
    gym5.add_member(Member("Richard", 20, Trainers(70, "green")))

    gym6.add_member(Member("Bella", 40, Trainers(15, "green")))
    gym6.add_member(Member("Bob", 50, Trainers(70, "green")))
    gym6.add_member(Member("Sandra", 25, Trainers(30, "pink")))
    gym6.add_member(Member("Bob", 35, Trainers(50, "black")))

    city3.get_max_members_gym()  # [Gym Gym Eesti : 4 member(s)]
    city3.get_max_stamina_clubs()  # [Gym People Fitness : 2 member(s)]
    city3.get_max_average_ages()  # [Gym Gym Eesti : 4 member(s)] => average age 37,5
    city3.get_min_average_ages()  # [Gym People Fitness : 2 member(s)] => average age 19
    city3.get_gyms_by_trainers_color(
        "green")  # [Gym Gym Eesti : 4 member(s), Gym People Fitness : 2 member(s)] => Gym Eesti has 2 members with green trainers, People Fitness has 1.
    city3.get_gyms_by_name(
        "Bob")  # [Gym Gym Eesti : 4 member(s), Gym Sparta : 2 member(s)] => Gym Eesti has 2 members with name Bob, Sparta has 1.

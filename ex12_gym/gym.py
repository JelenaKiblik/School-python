"""EX12 - Gym."""


class Trainers:
    """Class Trainers."""

    def __init__(self, stamina: int, color: str):
        """Constructor."""
        self.stamina = stamina
        self.color = color

    def __repr__(self) -> str:
        """
        Trainer object representation in string format.

        :return: string
        """
        return f"Trainers: [{self.stamina}, {self.color}]"


class Member:
    """Class Member."""

    def __init__(self, name: str, age: int, trainers: Trainers):
        """Constructor."""
        self.name = name
        self.age = age
        self.trainers = trainers
        self.gyms = []

    def get_all_gyms(self) -> list:
        """Get all gyms."""
        return self.gyms

    def get_gyms(self) -> list:
        """Get gyms."""
        return self.gyms

    def __repr__(self) -> str:
        """
        Member object representation in string format.

        :return: string
        """
        return f"{self.name}, {self.age}: {self.trainers}"


class Gym:
    """Class Gym."""

    def __init__(self, name: str, max_members_number: int):
        """Constructor."""
        self.name = name
        self.max_members_number = max_members_number
        self.members = []

    def add_member(self, member: Member) -> Member:
        """Add member."""
        if self.can_add_member(member):
            if len(self.members) < self.max_members_number:
                self.members.append(member)
                return member
            else:
                lowest_stamina = 100
                weakest = []
                for x in self.members:
                    if x.trainers.stamina < lowest_stamina:
                        lowest_stamina = x.trainers.stamina
                for x in self.members:
                    if x.trainers.stamina == lowest_stamina:
                        weakest.append(x)
                for weak_member in weakest:
                    self.remove_member(weak_member)
                self.members.append(member)
                member.gyms.append(self)
                return member

    def can_add_member(self, member: Member) -> bool:
        """Can add member."""
        if isinstance(member, Member):
            if member not in self.members and isinstance(member.trainers, Trainers):
                if member.trainers.stamina > 0 and member.trainers.color is not None and member.trainers.color != "":
                    return True

    def remove_member(self, member: Member):
        """Remove member."""
        self.members.remove(member)

    def get_total_stamina(self) -> int:
        """Get total stamina."""
        total_stamina = 0
        for x in self.members:
            total_stamina += x.trainers.stamina
        return total_stamina

    def get_members_number(self) -> int:
        """Get members number."""
        return len(self.members)

    def get_all_members(self) -> list:
        """Get all members."""
        return self.members

    def get_average_age(self) -> float:
        """Get average age."""
        age = 0
        for x in self.members:
            age += x.age
        return float(age / len(self.members))

    def get_count_of_trainers(self, color: str) -> int:
        """Get the count colored trainers."""
        count = 0
        for x in self.members:
            if x.trainers.color == color:
                count += 1
        return count

    def get_name_count(self, name: str) -> int:
        """Get the count of gym members with given name."""
        count = 0
        for x in self.members:
            if x.name == name:
                count += 1
        return count

    def __repr__(self) -> str:
        """
        Gym object representation in string format.

        :return: string
        """
        return f"Gym {self.name} : {len(self.members)} member(s)"


class City:
    """Class City."""

    def __init__(self, max_gym_number: int):
        """Constructor."""
        self.max_gym_number = max_gym_number
        self.gyms = []

    def build_gym(self, gym: Gym) -> Gym:
        """Build gym."""
        if self.can_build_gym() is True:
            self.gyms.append(gym)
            return gym
        else:
            return None

    def can_build_gym(self) -> bool:
        """Can build gym."""
        return len(self.gyms) < self.max_gym_number

    def destroy_gym(self):
        """Destroy gym."""
        lowest_member_count = 2000
        for x in self.gyms:
            if x.get_members_number() < lowest_member_count:
                lowest_member_count = x.get_members_number()
        for x in self.gyms:
            if x.get_members_number() == lowest_member_count:
                self.gyms.remove(x)

    def get_max_members_gym(self) -> list:
        """Get max members gym."""
        max_members_gyms = []
        max_members = 0
        for x in self.gyms:
            members_number = x.get_members_number()
            if members_number > max_members:
                max_members = members_number
        for x in self.gyms:
            if x.get_members_number() == max_members:
                max_members_gyms.append(x)
        return max_members_gyms

    def get_max_stamina_gyms(self) -> list:
        """Get max stamina gyms."""
        max_stamina_gyms = []
        max_stamina = 0
        for x in self.gyms:
            total_stamina = x.get_total_stamina()
            if int(total_stamina) > int(max_stamina):
                max_stamina = total_stamina
        for x in self.gyms:
            if x.get_total_stamina() == max_stamina:
                max_stamina_gyms.append(x)
        return max_stamina_gyms

    def get_max_average_ages(self) -> list:
        """Get max average ages."""
        max_average_ages = []
        max_average_age = 0
        for x in self.gyms:
            average_age = x.get_average_age()
            if average_age > max_average_age:
                max_average_age = average_age
        for x in self.gyms:
            if x.get_average_age() == max_average_age:
                max_average_ages.append(x)
        return max_average_ages

    def get_min_average_ages(self) -> list:
        """Get min average ages."""
        min_average_ages = []
        min_average_age = 100
        for x in self.gyms:
            average_age = x.get_average_age()
            if average_age < min_average_age:
                min_average_age = average_age
        for x in self.gyms:
            if x.get_average_age() == min_average_age:
                min_average_ages.append(x)
        return min_average_ages

    def get_gyms_by_trainers_color(self, color: str) -> list:
        """Get gyms by trainers color."""
        trainers_count = {}
        for x in self.gyms:
            if x.get_count_of_trainers(color) > 0:
                trainers_count[x] = x.get_count_of_trainers(color)
        return sorted(trainers_count.keys(), key=trainers_count.get, reverse=True)

    def get_gyms_by_name(self, name: str) -> list:
        """Get gyms by name."""
        name_count = {}
        for x in self.gyms:
            if x.get_name_count(name) > 0:
                name_count[x] = x.get_name_count(name)
        return sorted(name_count.keys(), key=name_count.get, reverse=True)

    def get_all_gyms(self) -> list:
        """Get all gyms."""
        return self.gyms


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

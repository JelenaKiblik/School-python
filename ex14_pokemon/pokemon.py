"""Pokemin."""
import requests


class CannotAddPokemonException(Exception):
    """Custom exception."""
    pass


class NoAvailablePokemonsInWorldException(Exception):
    """Custom exception."""
    pass


class Person:
    """Simple Person class."""

    def __init__(self, name, age):
        """
        Person constructor.

        :param name: Name of the Person.
        :param age:  Age of the Person.
        """
        pass

    def add_pokemon(self, pokemon):
        """
        Add pokemon to Person.

        :param pokemon: Pokemon to add.
        :return:
        """
        pass

    def get_pokemon(self):
        """
        Get Person's Pokemon.

        :return: Pokemon or None.
        """
        pass

    def remove_pokemon(self):
        """Remove Person's Pokemon."""
        pass

    def __repr__(self):
        """
        Representation of object.

        :return: Person's name, Person's age, Pokemon: Person's pokemon.
        """
        pass


class Data:
    """Class for getting data from API."""

    @staticmethod
    def get_all_pokemons_data(url):
        """
        Make request to API.

        :param endpoint: Address where to make the GET request.
        :return: Response data.
        """
        pass

    @staticmethod
    def get_additional_data(url):
        """
        Make request to API to get additional data for each Pokemon.

        :param endpoint: Address where to make the GET request.
        :return: Response data.
        """
        pass


class Pokemon:
    """Class for Pokemon."""

    def __init__(self, name, experience, attack, defence, types):
        """
        Class constructor.

        :param name: Pokemon's name.
        :param experience: Pokemon's experience
        :param attack: Pokemon's attack level
        :param defence: Pokemon's defence level.
        :param types: Pokemon's types.
        """
        pass

    def get_power(self):
        """
        Calculate power of Pokemon.

        :return: Power.
        """
        pass

    def __str__(self):
        """
        String representation of object.

        :return: Pokemon's name, experience: Pokemon's experience, att: Pokemon's attack level, def: Pokemon's defence level, types: Pokemon's types.
        """
        pass

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name
        """
        pass


class World:
    """World class."""

    def __init__(self, name):
        """
        Class constructor.

        :param name:
        """
        pass

    def add_pokemons(self, no_of_pokemons):
        """
        Add Pokemons to world, GET data from the API.
        """
        pass

    def get_pokemons_by_type(self):
        """
        Get Pokemons by type.

        :return: Dict of Pokemons, grouped by types.
        """
        pass

    def hike(self, person: Person):
        """
        Person goes to a hike to find a Pokemon.

        :param person: Person who goes to hike.
        """
        pass

    def remove_available_pokemon(self, pokemon: Pokemon):
        """
        Remove Pokemon from available Pokemons, which means that the Pokemon got a owner.

        :param pokemon: Pokemon to be removed.
        """
        pass

    def remove_pokemon_from_world(self, pokemon: Pokemon):
        """
        Remove Pokemon from the world, which means that the Pokemon died.

        :param pokemon: Pokemon to be removed.
        """
        pass

    def fight(self, person1: Person, person2: Person):
        """
        Two people fight with their Pokemons.

        :param person1:
        :param person2:
        :return: Pokemon which wins.
        """
        pass

    def group_pokemons(self):
        """
        Group Pokemons by given format.

        :return: Dictionary of grouped Pokemons.
        """
        pass

    def sort_by_type_experience(self):
        """
        Sort Pokemons by type adn experience. The first Pokemons should be Fire type and experience level of under 100.

        :return: List of sorted Pokemons.
        """
        pass

    def get_most_experienced_pokemon(self):
        """
        Get the Pokemon(s) which has the maximum experience level.
        """
        pass

    def get_min_experience_pokemon(self):
        """
        Get the Pokemon(s) which has the minimum experience level.
        """


class Main:
    if __name__ == '__main__':
        world = World("Poke land")
        world.add_pokemons(128)
        print(len(world.pokemons))  # -> 128
        print(len(world.get_pokemons_by_type().keys()))  # -> 16
        ago = Person("Ago", 10)
        peeter = Person("Peeter", 11)
        print(len(world.available_pokemons))  # -> 128
        world.hike(ago)
        world.hike(peeter)
        print(len(world.available_pokemons))  # -> 126
        print(world.get_most_experienced_pokemon())  # -> [CHANSEY]
        print(world.get_min_experience_pokemon())  # -> [CATERPIE, WEEDLE]
        print(world.fight(ago, peeter))  # String that says who battled with who and who won.

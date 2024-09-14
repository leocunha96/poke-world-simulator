import pytest
from coding.npc import NPC

class TestClass:
    def test_create_npc_with_all_informations_and_pokemons(self):
        #given
        name = 'Ash'
        gender = 'Male'
        age = 20
        category = 'Trainer'
        pokemons = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle']
        level = 12

        #expected
        expected_name = 'Ash'
        expected_gender = 'Male'
        expected_age = 20
        expected_category = 'Trainer'
        expected_pokemons = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle']
        expected_level = 12

        #when
        npc = NPC(name = name, gender = gender, age = age, category = category, pokemons = pokemons, level = level) #npc instance

        #then
        result_name = npc.name
        result_gender = npc.gender
        result_age = npc.age
        result_category = npc.category
        result_pokemons = npc.pokemons
        result_level = npc.level

        #assert
        assert result_name == expected_name
        assert result_gender == expected_gender
        assert result_age == expected_age
        assert result_category == expected_category
        assert result_pokemons == expected_pokemons
        assert result_level == expected_level

    
    def test_create_npc_with_firts_letter_of_name_capitalized(self):
        ...
    
    def test_create_npc_witht_name_being_a_string(self):
        ...
    
    def test_create_npc_with_valid_gender_male_or_female(self):
        ...
    
    def test_create_npc_with_valid_category(self):
        ...

    def test_create_npc_with_age_between_5_and_100(self):
        ...
    
    def test_create_npc_with_level_between_0_and_100(self):
        ...
    
    def test_create_npc_with_pokemons_between_0_and_6(self):
        ...
import pytest

class TestClass:
    def test_create_npc_with_all_informations_and_pokemons(self):
        pokemons = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle']
        npc = NPC(name = 'Ash', gender = 'Male', age = '20', category = 'Trainer', pokemons = pokemons, level = 12)
    
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
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
        #given
        name_npc1 = 'Ash'
        gender_npc1 = 'Male'
        age_npc1 = 20
        category_npc1 = 'Trainer'
        pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        level_npc1 = 12

        #given
        name_npc2 = 'misty'
        gender_npc2 = 'Female'
        age_npc2 = 18
        category_npc2 = 'Gym Leader'
        pokemons_npc2 = ['Staryu', 'Psyduck', 'Goldeen', 'Starmie']
        level_npc2 = 15

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        #expected
        expected_name_npc2 = 'Misty'
        expected_gender_npc2 = 'Female'
        expected_age_npc2 = 18
        expected_category_npc2 = 'Gym Leader'
        expected_pokemons_npc2 = ['Staryu', 'Psyduck', 'Goldeen', 'Starmie']
        expected_level_npc2 = 15

        #when
        npc1 = NPC(name = name_npc1, gender = gender_npc1, age = age_npc1, category = category_npc1, pokemons = pokemons_npc1, level = level_npc1) #npc instance
        npc2 = NPC(name = name_npc2, gender = gender_npc2, age = age_npc2, category = category_npc2, pokemons = pokemons_npc2, level = level_npc2) #npc instance

        #then
        result_name_npc1 = npc1.name
        result_gender_npc1 = npc1.gender
        result_age_npc1 = npc1.age
        result_category_npc1 = npc1.category
        result_pokemons_npc1 = npc1.pokemons
        result_level_npc1 = npc1.level

        result_name_npc2 = npc2.name
        result_gender_npc2 = npc2.gender
        result_age_npc2 = npc2.age
        result_category_npc2 = npc2.category
        result_pokemons_npc2 = npc2.pokemons
        result_level_npc2 = npc2.level

        #assert
        assert result_name_npc1 == expected_name_npc1
        assert result_gender_npc1 == expected_gender_npc1
        assert result_age_npc1 == expected_age_npc1
        assert result_category_npc1 == expected_category_npc1
        assert result_pokemons_npc1 == expected_pokemons_npc1
        assert result_level_npc1 == expected_level_npc1

        assert result_name_npc2 == expected_name_npc2
        assert result_gender_npc2 == expected_gender_npc2
        assert result_age_npc2 == expected_age_npc2
        assert result_category_npc2 == expected_category_npc2
        assert result_pokemons_npc2 == expected_pokemons_npc2
        assert result_level_npc2 == expected_level_npc2

    def test_create_npc_with_firts_letter_of_gender_capitalized(self):

        #given
        name_npc1 = 'Ash'
        gender_npc1 = 'Male'
        age_npc1 = 20
        category_npc1 = 'Trainer'
        pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        level_npc1 = 12

        name_npc2 = 'misty'
        gender_npc2 = 'female'
        age_npc2 = 18
        category_npc2 = 'Gym Leader'
        pokemons_npc2 = ['Staryu', 'Goldeen', 'Psyduck', 'Starmie']
        level_npc2 = 15

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        expected_name_npc2 = 'Misty'
        expected_gender_npc2 = 'Female'
        expected_age_npc2 = 18
        expected_category_npc2 = 'Gym Leader'
        expected_pokemons_npc2 = ['Staryu', 'Goldeen', 'Psyduck', 'Starmie']
        expected_level_npc2 = 15

        #when
        npc1 = NPC(name = name_npc1, gender = gender_npc1, age = age_npc1, category = category_npc1, pokemons = pokemons_npc1, level = level_npc1)
        npc2 = NPC(name = name_npc2, gender = gender_npc2, age = age_npc2, category = category_npc2, pokemons = pokemons_npc2, level = level_npc2)

        #them
        result_name_npc1 = npc1.name
        result_gender_npc1 = npc1.gender
        result_age_npc1 = npc1.age
        result_category_npc1 = npc1.category
        result_pokemons_npc1 = npc1.pokemons
        result_level_npc1 = npc1.level

        result_name_npc2 = npc2.name
        result_gender_npc2 = npc2.gender
        result_age_npc2 = npc2.age
        result_category_npc2 = npc2.category
        result_pokemons_npc2 = npc2.pokemons
        result_level_npc2 = npc2.level

        #assert
        assert result_name_npc1 == expected_name_npc1
        assert result_gender_npc1 == expected_gender_npc1
        assert result_age_npc1 == expected_age_npc1
        assert result_category_npc1 == expected_category_npc1
        assert result_pokemons_npc1 == expected_pokemons_npc1
        assert result_level_npc1 == expected_level_npc1

        assert result_name_npc2 == expected_name_npc2
        assert result_gender_npc2 == expected_gender_npc2
        assert result_age_npc2 == expected_age_npc2
        assert result_category_npc2 == expected_category_npc2
        assert result_pokemons_npc2 == expected_pokemons_npc2
        assert result_level_npc2 == expected_level_npc2

    def test_create_npc_with_firts_letter_of_category_capitalized(self):
            #given
        name_npc1 = 'Ash'
        gender_npc1 = 'Male'
        age_npc1 = 20
        category_npc1 = 'Trainer'
        pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        level_npc1 = 12

        name_npc2 = 'misty'
        gender_npc2 = 'female'
        age_npc2 = 18
        category_npc2 = 'gym leader'
        pokemons_npc2 = ['Staryu', 'Goldeen', 'Psyduck', 'Starmie']
        level_npc2 = 15

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        expected_name_npc2 = 'Misty'
        expected_gender_npc2 = 'Female'
        expected_age_npc2 = 18
        expected_category_npc2 = 'Gym Leader'
        expected_pokemons_npc2 = ['Staryu', 'Goldeen', 'Psyduck', 'Starmie']
        expected_level_npc2 = 15

        #when
        npc1 = NPC(name = name_npc1, gender = gender_npc1, age = age_npc1, category = category_npc1, pokemons = pokemons_npc1, level = level_npc1)
        npc2 = NPC(name = name_npc2, gender = gender_npc2, age = age_npc2, category = category_npc2, pokemons = pokemons_npc2, level = level_npc2)

        #them
        result_name_npc1 = npc1.name
        result_gender_npc1 = npc1.gender
        result_age_npc1 = npc1.age
        result_category_npc1 = npc1.category
        result_pokemons_npc1 = npc1.pokemons
        result_level_npc1 = npc1.level

        result_name_npc2 = npc2.name
        result_gender_npc2 = npc2.gender
        result_age_npc2 = npc2.age
        result_category_npc2 = npc2.category
        result_pokemons_npc2 = npc2.pokemons
        result_level_npc2 = npc2.level

        #assert
        assert result_name_npc1 == expected_name_npc1
        assert result_gender_npc1 == expected_gender_npc1
        assert result_age_npc1 == expected_age_npc1
        assert result_category_npc1 == expected_category_npc1
        assert result_pokemons_npc1 == expected_pokemons_npc1
        assert result_level_npc1 == expected_level_npc1

        assert result_name_npc2 == expected_name_npc2
        assert result_gender_npc2 == expected_gender_npc2
        assert result_age_npc2 == expected_age_npc2
        assert result_category_npc2 == expected_category_npc2
        assert result_pokemons_npc2 == expected_pokemons_npc2
        assert result_level_npc2 == expected_level_npc2
    
    def test_create_npc_with_name_being_a_string(self):
        #given
        name_npc1 = 123
        gender_npc1 = 'Male'
        age_npc1 = 20
        category_npc1 = 'Trainer'
        pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        level_npc1 = 12

        #expected
        expected_name_npc1 = '123'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        #when
        npc1 = NPC(name = name_npc1, gender = gender_npc1, age = age_npc1, category = category_npc1, pokemons = pokemons_npc1, level = level_npc1)

        #them
        result_name_npc1 = npc1.name
        result_gender_npc1 = npc1.gender
        result_age_npc1 = npc1.age
        result_category_npc1 = npc1.category
        result_pokemons_npc1 = npc1.pokemons
        result_level_npc1 = npc1.level

        #assert
        assert result_name_npc1 == expected_name_npc1
        assert result_gender_npc1 == expected_gender_npc1
        assert result_age_npc1 == expected_age_npc1
        assert result_category_npc1 == expected_category_npc1
        assert result_pokemons_npc1 == expected_pokemons_npc1
        assert result_level_npc1 == expected_level_npc1

    def test_create_npc_with_gender_being_a_string(self):
        #given
        name_npc1 = 'Ash'
        gender_npc1 = 456
        age_npc1 = 20
        category_npc1 = 'Trainer'
        pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        level_npc1 = 12

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Invalid'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        #when
        npc1 = NPC(name = name_npc1, gender = gender_npc1, age = age_npc1, category = category_npc1, pokemons = pokemons_npc1, level = level_npc1)

        #them
        result_name_npc1 = npc1.name
        result_gender_npc1 = npc1.gender
        result_age_npc1 = npc1.age
        result_category_npc1 = npc1.category
        result_pokemons_npc1 = npc1.pokemons
        result_level_npc1 = npc1.level

        #assert
        assert result_name_npc1 == expected_name_npc1
        assert result_gender_npc1 == expected_gender_npc1
        assert result_age_npc1 == expected_age_npc1
        assert result_category_npc1 == expected_category_npc1
        assert result_pokemons_npc1 == expected_pokemons_npc1
        assert result_level_npc1 == expected_level_npc1

    def test_create_npc_with_category_being_a_string(self):
        #given
        name_npc1 = 'Ash'
        gender_npc1 = 'Male'
        age_npc1 = 20
        category_npc1 = 3
        pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        level_npc1 = 12

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = '3'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        #when
        npc1 = NPC(name = name_npc1, gender = gender_npc1, age = age_npc1, category = category_npc1, pokemons = pokemons_npc1, level = level_npc1)

        #them
        result_name_npc1 = npc1.name
        result_gender_npc1 = npc1.gender
        result_age_npc1 = npc1.age
        result_category_npc1 = npc1.category
        result_pokemons_npc1 = npc1.pokemons
        result_level_npc1 = npc1.level

        #assert
        assert result_name_npc1 == expected_name_npc1
        assert result_gender_npc1 == expected_gender_npc1
        assert result_age_npc1 == expected_age_npc1
        assert result_category_npc1 == expected_category_npc1
        assert result_pokemons_npc1 == expected_pokemons_npc1
        assert result_level_npc1 == expected_level_npc1

    def test_create_npc_with_valid_gender_male_or_female(self):
        #given
        name_npc1 = 'Ash'
        gender_npc1 = 'jose'
        age_npc1 = 20
        category_npc1 = 'Trainer'
        pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        level_npc1 = 12

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Invalid'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        #when
        npc1 = NPC(name = name_npc1, gender = gender_npc1, age = age_npc1, category = category_npc1, pokemons = pokemons_npc1, level = level_npc1)

        #them
        result_name_npc1 = npc1.name
        result_gender_npc1 = npc1.gender
        result_age_npc1 = npc1.age
        result_category_npc1 = npc1.category
        result_pokemons_npc1 = npc1.pokemons
        result_level_npc1 = npc1.level

        #assert
        assert result_name_npc1 == expected_name_npc1
        assert result_gender_npc1 == expected_gender_npc1
        assert result_age_npc1 == expected_age_npc1
        assert result_category_npc1 == expected_category_npc1
        assert result_pokemons_npc1 == expected_pokemons_npc1
        assert result_level_npc1 == expected_level_npc1
    
    def test_create_npc_with_valid_category(self):
        ...

    def test_create_npc_with_age_between_5_and_100(self):
        ...
    
    def test_create_npc_with_level_between_0_and_100(self):
        ...
    
    def test_create_npc_with_pokemons_between_0_and_6(self):
        ...
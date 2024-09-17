import pytest
from coding.npc import NPC

class TestNpc:
    def setup_method(self):
        #common data for tests
        #given

        self.name_npc1 = 'Ash'
        self.gender_npc1 = 'Male'
        self.age_npc1 = 20
        self.category_npc1 = 'Trainer'
        self.pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        self.level_npc1 = 12

        self.name_npc2 = 'misty'
        self.gender_npc2 = 'female'
        self.age_npc2 = 18
        self.category_npc2 = 'gym Leader'
        self.pokemons_npc2 = ['Staryu', 'Goldeen', 'Psyduck', 'Starmie']
        self.level_npc2 = 15


    def test_create_npc_with_all_informations_and_pokemons(self):

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, pokemons = self.pokemons_npc1, level = self.level_npc1) #npc instance

        #then
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.category == expected_category_npc1
        assert npc1.pokemons == expected_pokemons_npc1
        assert npc1.level == expected_level_npc1

    def test_create_npc_with_firts_letter_of_name_capitalized(self):
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
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, pokemons = self.pokemons_npc1, level = self.level_npc1) #npc instance
        npc2 = NPC(name = self.name_npc2, gender = self.gender_npc2, age = self.age_npc2, category = self.category_npc2, pokemons = self.pokemons_npc2, level = self.level_npc2) #npc instance

        #then
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.category == expected_category_npc1
        assert npc1.pokemons == expected_pokemons_npc1
        assert npc1.level == expected_level_npc1

        assert npc2.name == expected_name_npc2
        assert npc2.gender == expected_gender_npc2
        assert npc2.age == expected_age_npc2
        assert npc2.category == expected_category_npc2
        assert npc2.pokemons == expected_pokemons_npc2
        assert npc2.level == expected_level_npc2
        

    def test_create_npc_with_firts_letter_of_gender_capitalized(self):
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
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, pokemons = self.pokemons_npc1, level = self.level_npc1) #npc instance
        npc2 = NPC(name = self.name_npc2, gender = self.gender_npc2, age = self.age_npc2, category = self.category_npc2, pokemons = self.pokemons_npc2, level = self.level_npc2) #npc instance

        #them
        assert npc1.name == expected_name_npc1
        assert  npc1.gender == expected_gender_npc1
        assert  npc1.age == expected_age_npc1
        assert  npc1.category == expected_category_npc1
        assert  npc1.pokemons == expected_pokemons_npc1
        assert  npc1.level == expected_level_npc1

        assert npc2.name == expected_name_npc2
        assert  npc2.gender == expected_gender_npc2
        assert  npc2.age == expected_age_npc2
        assert  npc2.category == expected_category_npc2
        assert  npc2.pokemons == expected_pokemons_npc2
        assert  npc2.level == expected_level_npc2

    def test_create_npc_with_firts_letter_of_category_capitalized(self):
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
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, pokemons = self.pokemons_npc1, level = self.level_npc1) #npc instance
        npc2 = NPC(name = self.name_npc2, gender = self.gender_npc2, age = self.age_npc2, category = self.category_npc2, pokemons = self.pokemons_npc2, level = self.level_npc2) #npc instance

        #them
        assert npc1.name == expected_name_npc1
        assert  npc1.gender == expected_gender_npc1
        assert  npc1.age == expected_age_npc1
        assert  npc1.category == expected_category_npc1
        assert  npc1.pokemons == expected_pokemons_npc1
        assert  npc1.level == expected_level_npc1

        assert npc2.name == expected_name_npc2
        assert  npc2.gender == expected_gender_npc2
        assert  npc2.age == expected_age_npc2
        assert  npc2.category == expected_category_npc2
        assert  npc2.pokemons == expected_pokemons_npc2
        assert  npc2.level == expected_level_npc2
    
    def test_create_npc_with_name_being_a_string(self):
        #given
        self.name_npc1 = 123

        #expected
        expected_name_npc1 = '123'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert  npc1.gender == expected_gender_npc1
        assert  npc1.age == expected_age_npc1
        assert  npc1.category == expected_category_npc1

    def test_create_npc_with_gender_being_a_string(self):
        #given
        self.gender_npc1 = 456
    
        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Invalid'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        
        #when
        npc1 = NPC(name = self.name_npc1 ,gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.category == expected_category_npc1

    def test_create_npc_with_category_being_a_string(self):
        #given
        self.category_npc1 = 3
       
        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Invalid'

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.category == expected_category_npc1

    def test_create_npc_with_a_valid_gender(self):

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'

        expected_name_npc2 = 'Misty'
        expected_gender_npc2 = 'Female'
        expected_age_npc2 = 18
        expected_category_npc2 = 'Gym Leader'

        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, pokemons = self.pokemons_npc1, level = self.level_npc1) #npc instance
        npc2 = NPC(name = self.name_npc2, gender = self.gender_npc2, age = self.age_npc2, category = self.category_npc2, pokemons = self.pokemons_npc2, level = self.level_npc2) #npc instance

        #then
        assert npc1.name == expected_name_npc1
        assert npc1.checking_valid_genders(self.gender_npc1) == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.category == expected_category_npc1

        assert npc2.name == expected_name_npc2
        assert npc2.checking_valid_genders(self.gender_npc2) == expected_gender_npc2
        assert npc2.age == expected_age_npc2
        assert npc2.category == expected_category_npc2

    def test_create_npc_with_a_invalid_gender(self):
        #given
        gender_npc1 = 'jose'

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Invalid'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'

        #when
        npc1 = NPC(name = self.name_npc1, gender = gender_npc1, age = self.age_npc1, category = self.category_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.checking_valid_genders(gender_npc1) == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.category == expected_category_npc1
    
    def test_create_npc_with_valid_category(self):
        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.checking_valid_categories(self.category_npc1) == expected_category_npc1

    def test_create_npc_with_invalid_category(self):
        #given
        category_npc1 = 'Fazendeiro'

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Invalid'

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = category_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.checking_valid_categories(category_npc1) == expected_category_npc1

    def test_create_npc_with_age_between_5_and_100(self):
        #given

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.checking_valid_age(self.age_npc1) == expected_age_npc1
        assert npc1.category == expected_category_npc1
    
    def test_create_npc_with_invalid_age(self):
        #given
        age_npc1 = 3

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 'Invalid'
        expected_category_npc1 = 'Trainer'

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = age_npc1, category = self.category_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.checking_valid_age(age_npc1) == expected_age_npc1
        assert npc1.category == expected_category_npc1
    
    def test_create_npc_with_level_between_0_and_100(self):
        #given
        name_npc1 = 'Ash'
        gender_npc1 = 'Male'
        age_npc1 = 101
        category_npc1 = 'Trainer'
        pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        level_npc1 = 105

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 'Invalid'
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 'Invalid'

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
    
    def test_create_npc_with_pokemons_between_0_and_6(self):
        #given
        name_npc1 = 'Ash'
        gender_npc1 = 'Male'
        age_npc1 = 20
        category_npc1 = 'Trainer'
        pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree', 'Taurus']
        level_npc1 = -5

        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = 'Invalid'
        expected_level_npc1 = 'Invalid'

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

    def test_create_npc_with_all_information_except_pokemons(self):
        #given
        name = 'Ash'
        gender = 'Male'
        age = 20
        category = 'Trainer'
        level = 12

        #expected
        expected_name = 'Ash'
        expected_gender = 'Male'
        expected_age = 20
        expected_category = 'Trainer'
        expected_pokemons = []
        expected_level = 12

        #when
        npc = NPC(name = name, gender = gender, age = age, category = category, level = level) #npc instance

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
        
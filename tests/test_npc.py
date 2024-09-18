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
        with pytest.raises(Exception):
            self.gender_npc1 = 456
        
            #expected
            expected_name_npc1 = 'Ash'
            expected_age_npc1 = 20
            expected_category_npc1 = 'Trainer'
            
            #when
            npc1 = NPC(name = self.name_npc1 ,gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1)

            #them
            assert npc1.name == expected_name_npc1
            assert npc1.gender
            assert npc1.age == expected_age_npc1
            assert npc1.category == expected_category_npc1

    def test_create_npc_with_category_being_a_string(self):
        #given
        with pytest.raises(Exception):
            self.category_npc1 = 3
        
            #expected
            expected_name_npc1 = 'Ash'
            expected_gender_npc1 = 'Male'
            expected_age_npc1 = 20
            

            #when
            npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1)

            #them
            assert npc1.name == expected_name_npc1
            assert npc1.gender == expected_gender_npc1
            assert npc1.age == expected_age_npc1
            assert npc1.category 

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
        with pytest.raises(Exception):
            #given
            gender_npc1 = 'jose'

            #expected
            expected_name_npc1 = 'Ash'
            expected_age_npc1 = 20
            expected_category_npc1 = 'Trainer'

            #when
            npc1 = NPC(name = self.name_npc1, gender = gender_npc1, age = self.age_npc1, category = self.category_npc1)

            #them
            assert npc1.name == expected_name_npc1
            assert npc1.checking_valid_genders(gender_npc1)
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
        with pytest.raises(Exception):
            category_npc1 = 'Fazendeiro'

            #expected
            expected_name_npc1 = 'Ash'
            expected_gender_npc1 = 'Male'
            expected_age_npc1 = 20

            #when
            npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = category_npc1)

            #them
            assert npc1.name == expected_name_npc1
            assert npc1.gender == expected_gender_npc1
            assert npc1.age == expected_age_npc1
            assert npc1.checking_valid_categories(category_npc1) 

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
        with pytest.raises(Exception):
            age_npc1 = 3

            #expected
            expected_name_npc1 = 'Ash'
            expected_gender_npc1 = 'Male'
            expected_category_npc1 = 'Trainer'

            #when
            npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = age_npc1, category = self.category_npc1)

            #them
            assert npc1.name == expected_name_npc1
            assert npc1.gender == expected_gender_npc1
            assert npc1.checking_valid_age(age_npc1)
            assert npc1.category == expected_category_npc1
    
    def test_create_npc_with_level_between_0_and_100(self):
        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, pokemons = self.pokemons_npc1, level = self.level_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.category == expected_category_npc1
        assert npc1.pokemons == expected_pokemons_npc1
        assert npc1.checking_valid_level(self.level_npc1) == expected_level_npc1

    def test_create_npc_with_invalid_level(self):
        #given
        with pytest.raises(Exception):
            level_npc1 = 105

            #expected
            expected_name_npc1 = 'Ash'
            expected_gender_npc1 = 'Male'
            expected_age_npc1 = 20
            expected_category_npc1 = 'Trainer'
            expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']

            #when
            npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, pokemons = self.pokemons_npc1, level = level_npc1)

            #them
            assert npc1.name == expected_name_npc1
            assert npc1.gender == expected_gender_npc1
            assert npc1.age == expected_age_npc1
            assert npc1.category == expected_category_npc1
            assert npc1.pokemons == expected_pokemons_npc1
            assert npc1.checking_valid_level(level_npc1)
    
    def test_create_npc_with_pokemons_between_0_and_6(self):
       #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree']
        expected_level_npc1 = 12

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, pokemons = self.pokemons_npc1, level = self.level_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.category == expected_category_npc1
        assert npc1.checking_number_valid_pokemons(self.pokemons_npc1) == expected_pokemons_npc1
        assert npc1.level == expected_level_npc1

    def test_create_npc_with_invalid_pokemons_numbers(self):
        #given
        with pytest.raises(Exception):
            pokemons_npc1 = ['Pikachu', 'Bulbassaur', 'Charmander', 'Squirtle', 'Pidgeot', 'Butterfree', 'Taurus']

            #expected
            expected_name_npc1 = 'Ash'
            expected_gender_npc1 = 'Male'
            expected_age_npc1 = 20
            expected_category_npc1 = 'Trainer'
            expected_level_npc1 = 12

            #when
            npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, pokemons = pokemons_npc1, level = self.level_npc1)

            #them
            assert npc1.name == expected_name_npc1
            assert npc1.gender == expected_gender_npc1
            assert npc1.age == expected_age_npc1
            assert npc1.category == expected_category_npc1
            assert npc1.checking_number_valid_pokemons(pokemons_npc1)
            assert npc1.level == expected_level_npc1

    def test_create_npc_with_all_information_except_pokemons(self):
        #expected
        expected_name_npc1 = 'Ash'
        expected_gender_npc1 = 'Male'
        expected_age_npc1 = 20
        expected_category_npc1 = 'Trainer'
        expected_pokemons_npc1 = []
        expected_level_npc1 = 12

        #when
        npc1 = NPC(name = self.name_npc1, gender = self.gender_npc1, age = self.age_npc1, category = self.category_npc1, level = self.level_npc1)

        #them
        assert npc1.name == expected_name_npc1
        assert npc1.gender == expected_gender_npc1
        assert npc1.age == expected_age_npc1
        assert npc1.category == expected_category_npc1
        assert npc1.pokemons == expected_pokemons_npc1
        assert npc1.level == expected_level_npc1
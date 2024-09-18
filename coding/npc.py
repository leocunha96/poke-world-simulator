class NPC():
    MAX_POKEMONS = 6
    def __init__(self, name, gender, age, category, pokemons = None, level = 0):
        self._name = str(name).title()
        self._gender = self.checking_valid_genders(gender)
        self._age = self.checking_valid_age(age)
        self._category = self.checking_valid_categories(category)
        self._pokemons = self.checking_number_valid_pokemons(pokemons)
        self._level = self.checking_valid_level(level)

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, value):
        self._gender = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        self._category = value

    @property
    def pokemons(self):
        return self._pokemons
    
    @pokemons.setter
    def pokemons(self, value):
        self._pokemons = value

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        self._level = value

    def checking_valid_genders(self, gender):
        valid_genders = ('Male', 'Female')
        formated_gender = str(gender).title()
        if formated_gender in valid_genders:
                return formated_gender
        else:
            raise Exception ('Invalid Gender')
            

    def checking_valid_categories(self, category):
        valid_categories = ('Bandit', 'Common', 'Guide', 'Gym Leader', 'Healer', 'Player', 'Professor', 'Rival', 'Seller', 'Specialist', 'Storyteller', 'Trader', 'Trainer')
        formated_category = str(category).title()
        if formated_category in valid_categories:
                return formated_category
        else:
            raise Exception ('Invalid Category')
    
    def checking_valid_age(self, age):
        max_age = 100
        minimum_age = 5
        if age >= minimum_age and age <= max_age:
                return age
        else:
            raise Exception ('Invalid Age')
        
    def checking_valid_level(self, level):
        max_level = 100
        minimum_level = 0
        if level >= minimum_level and level <= max_level:
                return level
        else:
            return 'Invalid'

    def checking_number_valid_pokemons(self, pokemons):
        if pokemons is None:
             return []
        if len(pokemons) > self.MAX_POKEMONS:
                return 'Invalid'
        else:
            return pokemons
        

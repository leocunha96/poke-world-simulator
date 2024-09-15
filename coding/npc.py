class NPC():
    
    def __init__(self, name, gender, age, category, pokemons = None, level = 0):
        self._name = str(name).title()
        self._gender = self.checking_valid_genders(gender)
        self._age = age
        self._category = str(category).title()
        self._pokemons = pokemons if pokemons is not None else []
        self._level = level

    
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
            return 'Invalid'
        

    
class NPC():
    
    def __init__(self, name, gender, age, category, pokemons = None, level = 0):
        self._name = name.title()
        self._gender = gender.title()
        self._age = age
        self._category = category.title()
        self._pokemons = pokemons if pokemons is not None else []
        self.level = level

    
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

    
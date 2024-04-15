class Pokemon: 
    def _int_(self):
        """Constructor: contains all properties of a pokemon
        """
        self.name = " "
        self.id = 0
        self.weight = 0 
        self.height = 0 
        self.type = "Normal"
    pass

def main():
    pokemon_one = Pokemon()
    pokemon_one.name = "Pikachu"
    pokemon_one.type = "Electric"
    pokemon_one.id = 25
    print(pokemon_one.name)
    print(pokemon_one.id)
    print(pokemon_one.type)

    pokemon_two = Pokemon()
    pokemon_two.name = "Squirtle"
    pokemon_two.id = 4
    pokemon_two.type = "Water"
    print(pokemon_two.name)
if __name__ == "__main__":
    main()


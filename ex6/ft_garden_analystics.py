# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analystics.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 13:31:18 by klucchin        #+#    #+#               #
#  Updated: 2026/02/06 16:14:20 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(self.name, "grew 1cm")

    def describe(self):
        return "- " + self.name + ": " + str(self.height) + "cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def describe(self):
        state = "blooming" if self.blooming else "not blooming"
        return (
            "- " + self.name + ": " + str(self.height) + "cm, "
            + self.color + " flowers (" + state + ")"
        )


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def describe(self):
        return (
            super().describe()
            + ", Prize points: "
            + str(self.prize_points)
        )


class GardenManager:
    gardens = {}

    class GardenStats:
        def __init__(self, plants):
            self.plants = plants

        def count_plants(self):
            count = 0
            for _ in self.plants:
                count += 1
            return count

        def total_growth(self):
            growth = 0
            for _ in self.plants:
                growth += 1
            return growth

        def plant_types(self):
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.gardens[owner] = self

    def add_plant(self, plant):
        self.plants.append(plant)
        print("Added", plant.name, "to", self.owner + "'s garden")

    def grow_all(self):
        print("\n", self.owner, "is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print("\n===", self.owner + "'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.describe())

        stats = GardenManager.GardenStats(self.plants)
        count = stats.count_plants()
        growth = stats.total_growth()
        r, f, p = stats.plant_types()

        print("\nPlants added:", count, ", Total growth:", growth, "cm")
        print(
            "Plant types:", r, "regular,", f, "flowering,", p, "prize flowers"
            "\n"
        )

    @staticmethod
    def validate_height(plant):
        return plant.height > 0

    @classmethod
    def create_garden_network(cls):
        scores = {}
        for owner in cls.gardens:
            score = 0
            for plant in cls.gardens[owner].plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points
            scores[owner] = score
        return scores

    @classmethod
    def total_gardens(cls):
        count = 0
        for _ in cls.gardens:
            count += 1
        return count


def main():
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    bob.add_plant(Plant("Cactus", 90))
    bob.add_plant(FloweringPlant("Tulip", 22, "purple"))

    alice.grow_all()
    alice.report()
    print("\nHeight validation test:",
          GardenManager.validate_height(alice.plants[0]), "\n")
    bob.grow_all()
    bob.report()

    print("\nHeight validation test:",
          GardenManager.validate_height(bob.plants[0]))

    scores = GardenManager.create_garden_network()
    print("Garden scores - Alice:", scores["Alice"],
          ", Bob:", scores["Bob"])

    print("Total gardens managed:", GardenManager.total_gardens())


if __name__ == "__main__":
    main()

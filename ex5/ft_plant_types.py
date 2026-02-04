# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 17:16:19 by klucchin        #+#    #+#               #
#  Updated: 2026/02/04 18:03:27 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self):
        shade_area = self.diameter * 1.56
        print(
            f"{self.name} provides {round(shade_area)}"
            " square meters of shade\n"
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season

    def nutritional_info(self):
        print(f"{self.name} is rich in vitamin C\n")


# === Create all plants ===
print("=== Garden Plant Types ===")

plants = [
    Flower("Rose", 25, 30, "red"),
    Flower("Sunflower", 80, 45, "yellow"),
    Tree("Oak", 500, 1825, 50),
    Tree("Sitka_spruce", 960, 3500, 100),
    Vegetable("Tomato", 80, 90, "summer harvest"),
    Vegetable("Potato", 100, 90, "spring harvest"),
]

# === Display all plants ===
for plant in plants:
    if isinstance(plant, Flower):
        print(
            f"{plant.name} (Flower): {plant.height}cm, {plant.age} days, "
            f"{plant.color} color"
        )
        plant.bloom()
    elif isinstance(plant, Tree):
        print(
            f"{plant.name} (Tree): {plant.height}cm, {plant.age} days, "
            f"{plant.diameter}cm diameter"
        )
        plant.produce_shade()
    elif isinstance(plant, Vegetable):
        print(
            f"{plant.name} (Vegetable): {plant.height}cm, {plant.age} days, "
            f"{plant.harvest_season}"
        )
        plant.nutritional_info()

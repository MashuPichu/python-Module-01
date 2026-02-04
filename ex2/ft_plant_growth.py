# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 15:15:45 by klucchin        #+#    #+#               #
#  Updated: 2026/02/04 16:13:23 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_one_day(self):
        self.age += 1

    def get_info(self):
        print(
            self.name + ": "
            + str(self.height) + "cm, "
            + str(self.age) + " days old"
        )


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

plants = [rose, sunflower, cactus]

print("=== Day 1 ===")
for i in range(len(plants)):
    plants[i].get_info()

start_heights = []
for i in range(len(plants)):
    start_heights.append(plants[i].height)

for day in range(6):
    for i in range(len(plants)):
        plants[i].grow()
        plants[i].age_one_day()
        if i == 2:
            plants[2].grow()

print("=== Day 7 ===")
for i in range(len(plants)):
    plants[i].get_info()
    growth = plants[i].height - start_heights[i]
    print("Growth this week: +" + str(growth) + "cm")

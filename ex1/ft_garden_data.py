# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 14:52:54 by klucchin        #+#    #+#               #
#  Updated: 2026/02/04 15:49:57 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

plants = [rose, sunflower, cactus]

print("=== Garden Plant Registry ===")

for i in range(len(plants)):
    plant = plants[i]
    print(
        plant.name + ": "
        + str(plant.height) + "cm, "
        + str(plant.age) + " days old"
    )

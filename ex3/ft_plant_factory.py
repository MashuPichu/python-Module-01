# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 16:14:14 by klucchin        #+#    #+#               #
#  Updated: 2026/02/04 16:29:31 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

plant_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
]

print("=== Plant Factory Output ===")

plants = []

for i in range(len(plant_data)):
    name = plant_data[i][0]
    height = plant_data[i][1]
    age = plant_data[i][2]
    print(f"Created: {name}, ({height}cm, {age} days)")

plants_number = len(plant_data)
print(f"\nTotal plants created: {plants_number}")

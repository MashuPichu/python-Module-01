# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 16:30:04 by klucchin        #+#    #+#               #
#  Updated: 2026/02/04 17:15:53 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = 0
        self.age = 0
        print("=== Garden Security System ===")
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = value
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, value):
        if value < 0:
            print(f"Invalid operation attempted: age {value} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = value
            print(f"Age updated: {self.age} days [OK]")

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    def get_info(self):
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")


rose = SecurePlant("Rose", 25, 30)
rose.set_height(-5)
rose.get_info()

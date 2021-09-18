# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:39:13 2020

@author: alex
"""

from assignment1 import *

if __name__ == '__main__':

    orc1 = Orc('Gary', 3.1, True)
    orc2 = Orc('Mark', 2.8, True)

    print('Changing attribute values (no errors) \n')
    print(orc1, ' : ', orc2)
    # orc1.name = 'Jack'
    # orc2.name = 'Luke'
    # orc1.name
    # orc2.name
    # orc1.strength
    # orc1.strength = 5.0
    # orc2.strength = 4.0
    # orc1.strength
    # orc2.strength
    # orc1.weapon = True
    # orc2.weapon = False
    # orc1.weapon
    # orc2.weapon
    # Orc.fight(orc1, orc2)
    # Orc.fight(orc2, orc1)
    knight1 = Knight('Jeremy', 5, 'Gondor', [])
    # a1 = Archer('John', 5.2, 'Gondor')
    # a2 = Archer('James', 2.0, 'Gondor')
    # print(orc1>orc2, 'h')
    # print(a1, 'archer')
    # print(a2, 'archer')
    # knight1.archers_list = [a1, a2]
    print(knight1, 'knight')
    # print(knight1.archers_list)
    # a1.fight(a2)
    # a1.fight(orc1)
    
    # print('\nError testing \n')
    # print(orc1, ' : ', orc2)
    # orc1.name = 1655
    # orc2.name = False
    # orc1.name
    # orc2.name
    # orc1.strength = 'hey'
    # orc2.strength = -0.01
    # orc1.strength
    # orc2.strength
    # orc1.weapon = 'True'
    # orc2.weapon = 3
    # orc1.weapon
    # orc2.weapon
    # Orc.fight(orc1, orc2)
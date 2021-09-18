# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:23:57 2020

@author: 119442536 Alex O'Meara'
"""

class Characters:
    
    def __init__(self, name, strength):
            self.name = name
            self.strength = strength
    
    def __str__(self):
        return '%s %s' % (self._name, self._strength)
    
    def __gt__(self, other): 
        if self._strength > other._strength:
            return True
        else:
            return False
        
    def fight(self, other):#
        if self > other:
            if self._strength != 5.0:
                self._strength += 1
            print(self)
        elif self == other:
            if self._strength != 0.0:
                self._strength -= 0.5
            elif other._strength != 0.0:
                other._strength -= 0.5
        else:
            if other._strength != 5.0:
                other._strength += 1
            print(other)

    @property
    def name(self): # Getter for _name
        return self._name
    
    @name.setter
    def name(self, name): # Setter for _name
        if type(name) == str:
            self._name = name
        else:
            print('type ERROR')
        
    @property
    def strength(self): # Getter for _strength
        return self._strength
    
    @strength.setter
    def strength(self, strength): # Setter for _strength
        if type(strength) == float:
            if strength < 0:
                strength = 0.0
            elif strength > 5:
                strength = 5.0 
            self._strength = strength
        else:
            print('type ERROR')    

class Orc(Characters):
    
    def __init__(self, name, strength, weapon):
        Characters.__init__(self, name, strength)
        self.weapon = weapon
        
    def __str__(self):
        return super().__str__() + " %s" % (self._weapon)
    
    def __gt__(self, other):
        if isinstance(self, Orc) and isinstance(other, Orc):
            if self._weapon == other._weapon:
                return super().__gt__(other)
            elif self.weapon == True:
                return True
            else:
                return False
            
         
    @property
    def weapon(self):
        return self._weapon
    
    @weapon.setter
    def weapon(self, weapon):
        if type(weapon) == bool:
            self._weapon = weapon
            
        else:
            print('type ERROR')    
        
class People(Characters):
    
    def __init__(self, name, strength, kingdom):
        Characters.__init__(self, name, strength)
        self.kingdom = kingdom
        
    def __str__(self):
        return '%s %s %s' % (self._name, self._strength, self._kingdom)
    
    def fight(self, other):
        if isinstance(self, People) and isinstance(other, People):
            print('fight ERROR')
        elif isinstance(self, Orc) and not self._weapon:
            print(other)
        elif isinstance(other, Orc) and not other._weapon:
            print(self)
        else:
            return super().fight(other)
            
        
    @property
    def kingdom(self): # Getter for kingdom
        return self._kingdom
    
    @kingdom.setter
    def kingdom(self, kingdom): # Setter for kingdom
        if type(kingdom) == str:
            self._kingdom = kingdom
        else:
            print('type ERROR')
        
class Archer(People):
    
    def __init__(self, name, strength, kingdom):
        People.__init__(self, name, strength, kingdom)
        
    
        

class Knight(People):
        
    def __init__(self, name, strength, kingdom, archers_list):
        People.__init__(self, name, strength, kingdom) 
        self.archers_list = archers_list
    
    def __str__(self):
        archer_list_str = ', ['
        for x in self._archers_list:
            archer_list_str += x.__str__()
            if self._archers_list.index(x) != len(self._archers_list) - 1:
                archer_list_str += ' '
        archer_list_str += ']'
        return super().__str__() + archer_list_str
            
    
    @property
    def archers_list(self):
        return self._archers_list
        
    @archers_list.setter
    def archers_list(self, archer):
        self._archers_list = []
        for x in archer:
            if x.kingdom != self._kingdom and not isinstance(x, Archer):
                print('archers list ERROR')
            elif x.kingdom == self._kingdom:
                self._archers_list.append(x)
             
            
            
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
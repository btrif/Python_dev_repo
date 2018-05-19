#!/usr/bin/python3
# One of the most common use of decorators is to  CREATE ACCESSOR METHODS FOR VARIABLES
# 2014-09-14 20:45

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)
    
#    what turns it into an accessor is @property 
    @property 
    def color(self):
        return self.properties.get('color', None)
    
    @color.setter
    def color(self, c):
        self.properties['color'] = c
        
    @color.deleter
    def color(self):
        del self.properties['color']

def main():
    donald = Duck()
    donald.color = 'blue'
    print(donald.color)
    

if __name__ == "__main__": main()

#  Created by Bogdan Trif on 24-07-2018 , 1:21 PM.
print('-----------------------      Public- Protected- and Private Attributes   ----------------------------')

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

a = A()
print('semi-private, protected : ' ,a._prot )
print(' public :  ',a.pub)
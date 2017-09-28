class Student:
    def __init__(self, name):
        self.name = name
        self.attend = 0
        self.grades = []
        print('Hi! My name is {0}'.format(self.name))
    
    def addGrade(self, grade):
        self.grades.append(grade)
    
    def attendDay(self):
        self.attend += 1
    
    def getAverage(self):
        return sum(self.grades) / len(self.grades)
        
        
def main(): 


    student1 = Student('Bogdan')
    print('Days to school:',student1.attend)    
    student2 =Student('Valeriu')
    student1.attendDay()
    print('Days to school:',student1.attend)

    for x in range(11):
        student2.attendDay()

    print('Days to school:',student2.attend)

    student1.addGrade(90)
    student1.addGrade(50)
    student1.addGrade(92)
    student1.addGrade(81)
    student1.addGrade(73)
    print('Notele studentului 1 sunt:',student1.grades)
    print('Media notelor studentului 1 este:',student1.getAverage())
        
    
    
    
if __name__ == "__main__": main()


#  Created by Bogdan Trif on 10-07-2018 , 11:00 AM.
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html

'''
3.12. Implementing a Queue in Python
It is again appropriate to create a new class for the implementation of the abstract data type queue.
As before, we will use the power and simplicity of the list collection to build the internal representation of the queue.

We need to decide which end of the list to use as the rear and which to use as the front.
The implementation shown in Listing 1 assumes that the rear is at position 0 in the list.
This allows us to use the insert function on lists to add new elements to the rear of the queue.
The pop operation can be used to remove the front element (the last element of the list).
Recall that this also means that enqueue will be O(n) and dequeue will be O(1).
'''

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

'''
3.13. Simulation: Hot Potato
One of the typical applications for showing a queue in action is to simulate a real situation that requires data 
to be managed in a FIFO manner. To begin, let’s consider the children’s game Hot Potato.
In this game (see Figure 2) children line up in a circle and pass an item from neighbor to neighbor as fast as they can. 

At a certain point in the game, the action is stopped and the child who has the item (the potato) is removed from the circle. 
Play continues until only one child is left.

This game is a modern-day equivalent of the famous Josephus problem. 
Based on a legend about the famous first-century historian Flavius Josephus, the story is told that in the Jewish revolt against Rome, 
Josephus and 39 of his comrades held out against the Romans in a cave. 
With defeat imminent, they decided that they would rather die than be slaves to the Romans. 
They arranged themselves in a circle. One man was designated as number one, and proceeding clockwise they killed every seventh man. 
Josephus, according to the legend, was among other things an accomplished mathematician. 
He instantly figured out where he ought to sit in order to be the last to go. 
When the time came, instead of killing himself, he joined the Roman side. 

You can find many different versions of this story. 
Some count every third man and some allow the last man to escape on a horse. In any case, the idea is the same.

We will implement a general simulation of Hot Potato. 
Our program will input a list of names and a constant, call it “num,” to be used for counting. 
It will return the name of the last person remaining after repetitive counting by num. 
What happens at that point is up to you.

To simulate the circle, we will use a queue (see Figure 3). 
Assume that the child holding the potato will be at the front of the queue. 
Upon passing the potato, the simulation will simply dequeue and then immediately enqueue that child, 
putting her at the end of the line. 
She will then wait until all the others have been at the front before it will be her turn again. 
After num dequeue/enqueue operations, the child at the front will be removed permanently and another cycle will begin. 
This process will continue until only one name remains (the size of the queue is 1).
'''

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))


print('\n---------  3.14. Simulation: Printing Tasks    - ---------------------------')
# http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationPrintingTasks.html

'''
3.14. Simulation: Printing Tasks

A more interesting simulation allows us to study the behavior of the printing queue described earlier in this section. 
Recall that as students send printing tasks to the shared printer, 
the tasks are placed in a queue to be processed in a first-come first-served manner. 
Many questions arise with this configuration. 
The most important of these might be whether the printer is capable of handling a certain amount of work. 
If it cannot, students will be waiting too long for printing and may miss their next class.

Consider the following situation in a computer science laboratory. 
On any average day about 10 students are working in the lab at any given hour. 
These students typically print up to twice during that time, and the length of these tasks ranges from 1 to 20 pages. 
The printer in the lab is older, capable of processing 10 pages per minute of draft quality. 
The printer could be switched to give better quality, but then it would produce only five pages per minute. 
The slower printing speed could make students wait too long. What page rate should be used?

We could decide by building a simulation that models the laboratory. 
We will need to construct representations for students, printing tasks, and the printer (Figure 4). 
As students submit printing tasks, we will add them to a waiting list, a queue of print tasks attached to the printer. 
When the printer completes a task, it will look at the queue to see if there are any remaining tasks to process. 
Of interest for us is the average amount of time students will wait for their papers to be printed. 
This is equal to the average amount of time a task waits in the queue.

To model this situation we need to use some probabilities. 
For example, students may print a paper from 1 to 20 pages in length. 
If each length from 1 to 20 is equally likely, the actual length for a print task can be simulated 
by using a random number between 1 and 20 inclusive. 
This means that there is equal chance of any length from 1 to 20 appearing.

If there are 10 students in the lab and each prints twice, then there are 20 print tasks per hour on average. 
What is the chance that at any given second, a print task is going to be created? 
The way to answer this is to consider the ratio of tasks to time. 
Twenty tasks per hour means that on average there will be one task every 180 seconds:

20 tasks / 1 hour × 1 hour/ 60 minutes × 1 minute / 60 seconds = 1 task / 180 seconds

For every second we can simulate the chance that a print task occurs by generating a random number between 1 and 180 inclusive. 
If the number is 180, we say a task has been created. 
Note that it is possible that many tasks could be created in a row or we may wait quite a while for a task to appear.
That is the nature of simulation. 
You want to simulate the real situation as closely as possible given that you know general parameters.
'''

'''
3.14.1. Main Simulation Steps
Here is the main simulation.

1.  Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
2.  For each second (currentSecond):
        -   Does a new print task get created? If so, add it to the queue with the currentSecond as the timestamp.
        -   If the printer is not busy and if a task is waiting,
            --  Remove the next task from the print queue and assign it to the printer.
            --  Subtract the timestamp from the currentSecond to compute the waiting time for that task.
            --  Append the waiting time for that task to a list for later processing.
            --  Based on the number of pages in the print task, figure out how much time will be required.
        -   The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.
        -   If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.
3.  After the simulation is complete, compute the average waiting time from the list of waiting times generated.



3.14.2. Python Implementation
To design this simulation we will create classes for the three real-world objects described above: Printer, Task, and PrintQueue.

The Printer class (Listing 2) will need to track whether it has a current task. 
If it does, then it is busy (lines 13–17) and the amount of time needed can be computed from the number of pages in the task. 
The constructor will also allow the pages-per-minute setting to be initialized. 
The tick method decrements the internal timer and sets the printer to idle (line 11) if the task is completed.
'''

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

'''
The Task class (Listing 3) will represent a single printing task. 
When the task is created, a random number generator will provide a length from 1 to 20 pages. 
We have chosen to use the randrange function from the random module.

Each task will also need to keep a timestamp to be used for computing waiting time. 
This timestamp will represent the time that the task was created and placed in the printer queue. 
The waitTime method can then be used to retrieve the amount of time spent in the queue before printing begins.
'''

import random

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


'''
The main simulation (Listing 4) implements the algorithm described above. 
The printQueue object is an instance of our existing queue ADT. 
A boolean helper function, newPrintTask, decides whether a new printing task has been created. 
We have again chosen to use the randrange function from the random module to return a random integer between 1 and 180. 
Print tasks arrive once every 180 seconds. 
By arbitrarily choosing 180 from the range of random integers (line 32), we can simulate this random event. 
The simulation function allows us to set the total time and the pages per minute for the printer.
'''



import random

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))
    return averageWait

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

'''
When we run the simulation, we should not be concerned that the results are different each time. 
This is due to the probabilistic nature of the random numbers.
We are interested in the trends that may be occurring as the parameters to the simulation are adjusted. 
Here are some results.

First, we will run the simulation for a period of 60 minutes (3,600 seconds) using a page rate of five pages per minute. 
In addition, we will run 10 independent trials. 
Remember that because the simulation works with random numbers each run will return different results.
'''

'''
After running our 10 trials we can see that the mean average wait time is 122.09 seconds. 
You can also see that there is a large variation in the average weight time with a minimum average of 17.27 seconds 
and a maximum of 376.05 seconds. 
You may also notice that in only two of the cases were all the tasks completed.

Now, we will adjust the page rate to 10 pages per minute, and run the 10 trials again, 
with a faster page rate our hope would be that more tasks would be completed in the one hour time frame.
'''

W = 0
for i in range(10):
    W += simulation(3600,5)
print('Total Average Wait = ',  W/ 10 )

print('------ 10 ppm -----')
W = 0
for i in range(10):
      W += simulation(3600,10)
print('Total Average Wait = ', W/10  )

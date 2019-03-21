from queue import Queue
import random

class Printer:
    def __init__(self, pagesperminute):
        self.page_rate = pagesperminute
        self.current_task = None
        self.time_remaining = 0


    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    
    def busy(self):
        return self.current_task == None


    def startNext(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.getPages() * 60 / self.page_rate

    
class Task:
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)


    def getStamp(self):
        return self.time_stamp


    def getPages(self):
        return self.pages


    def waitTime(self, current_time):
        return current_time - self.time_stamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        
        if newPrintTask():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.waitTime(current_second))
            lab_printer.startNext(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


def newPrintTask():
    num = random.randrange(1,181) # between 1 and 180 inclusive
    return num == 180


for i in range(10):
    simulation(3600, 5) # 1 hr, 5 pages per minute

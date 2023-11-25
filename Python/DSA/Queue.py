# Queue : it is a linear data structure that stores items in First-In/First-out manner.
# i.e the first added element will be removed first

class Queue:
    def __init__(self):
        self.queue = []
    
    def Enqueue(self, data):
        self.queue.append(data)

    def Dequeue(self):
        if(self.queue):
            self.queue.pop(0)
        else:
            print("empty Queue!.. nothing to pop")

    def Front(self):
        if(self.queue):
            print(self.queue[0])
        else:
            print("empty Queue!.. nothing to show")

    def Rear(self):
        if(self.queue):
            print(self.queue[-1])
        else:
            print("empty Queue!.. nothing to show")
    
    def Display(self):
        print(self.queue)

if __name__ == '__main__':

    Q = Queue()
    Q.Enqueue(10)
    Q.Enqueue(20)
    Q.Enqueue(30)

    Q.Display()
    Q.Front()
    Q.Rear()

    Q.Dequeue()
    Q.Dequeue()

    Q.Display()
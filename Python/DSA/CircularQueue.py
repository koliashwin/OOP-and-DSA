
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
    
    def Enqueue(self, data):
        if((self.rear + 1) % self.size == self.front):
            print("Queue is full !... cann't add anymore")
        elif(self.front == -1):
            self.front, self.rear = 0, 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    
    def Dequeue(self):
        if(self.front == -1):
            print("Empty Queue!... nothing to delete")
        elif(self.front == self.rear):
            temp = self.queue[self.front]
            self.front = self.rear = -1
            print("deleted : ",temp)
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print("deleted : ",temp)

    def Display(self):
        if(self.front == -1):
            print('empty Queue!...')
        elif(self.front <= self.rear):
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear+1):
                print(self.queue[i], end=" ")
            print()
    
if __name__=='__main__':
    cq = CircularQueue(3)

    cq.Enqueue(10)
    cq.Enqueue(20)
    cq.Enqueue(30)
    cq.Display()
    cq.Dequeue()
    cq.Dequeue()
    cq.Display()
    cq.Enqueue(40)
    cq.Enqueue(50)
    cq.Enqueue(60)
    cq.Display()
    cq.Dequeue()
    cq.Dequeue()
    cq.Display()
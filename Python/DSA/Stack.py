# Stack : it is a linear data structure that stores items in Last-In/First-Out(LIFO) or First-In/Last-Out(FILO) approch.
# i.e the last added element will be removed first

class Stack:

    def __init__(self):
        self.stack = []
    
    def Push(self, data):
        self.stack.append(data)
    
    def Pop(self):
        if(self.stack):
            self.stack.pop()
        else:
            print("empty stack!... nothing to pop there")
    
    def Display(self):
        print(self.stack)


if __name__ == '__main__':
    S = Stack()

    S.Pop()

    S.Push(10)
    S.Push(20)
    S.Push(30)

    S.Display()

    S.Pop()
    S.Display()
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queueList= []
    def put(self, elem):
        self.__queueList.insert(0, elem)
    def get(self):
        if self.__queueList == []:
            raise QueueError
        else:
            elem = self.__queueList[-1]
            del self.__queueList[-1]
            return elem

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.__count = 0
        
    def isempty(self):
        if self.__count < 1:
            return True
    def put(self, elem):
        Queue.put(self, elem)
        self.__count +=1
    def get(self):
            elem = Queue.get(self)
            self.__count -=1
            return elem
    #
    # Write new code here.
    #


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

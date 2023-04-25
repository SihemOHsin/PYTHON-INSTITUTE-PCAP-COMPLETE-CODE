class QueueError:  # Choose base class for the new exception.
    def __init__(self):
        self.__raise= "error :list vide"


class Queue:
    def __init__(self):
        QueueError.__init__(self)
        self.__queueList = []
        # Write code here
        #

    def put(self, elem):
        self.__queueList.insert(0,elem)
        # Write code here
        #

    def get(self):
        if self.__queueList == 0:
            return QueueError.__raise
        else:
            elem = self.__queueList[-1]
            del self.__queueList[-1]
            return elem
        # Write code here
        #


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

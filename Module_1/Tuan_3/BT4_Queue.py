class MyQueue():
    def __init__(self, capacity):
        self.__data = []
        self.__capacity = capacity

    def getData(self):
        return self.__data

    def isEmpty(self):
        return len(self.__data) == 0

    def isFull(self):
        return len(self.__data) == self.__capacity

    def dequeueFirstElement(self):
        if self.isEmpty():
            print('Empty')
            return
        return self.__data.pop(0)

    def addElement(self, value):
        if self.isFull():
            print('Full')
            return
        return self.__data.append(value)

    def getFirstElement(self):
        if self.isEmpty():
            print('Empty')
            return
        return self.__data[0]


queue1 = MyQueue(capacity=5)
print('Queue ban đầu: ', queue1.getData())
queue1.addElement(1)
queue1.addElement(2)
print('Queue sau khi thêm giá trị: ', queue1.getData())
print('Queue đã đủ giá trị chưa? ', queue1.isFull())
print('Lấy giá trị vị trí đầu tiên trong Queue: ', queue1.getFirstElement())
print('Xóa giá trị vị trí đầu tiên trong Queue: ', queue1.dequeueFirstElement())
print('Lấy giá trị vị trí đầu tiên trong Queue: ', queue1.getFirstElement())
print('Xóa giá trị vị trí đầu tiên trong Queue: ', queue1.dequeueFirstElement())
print('Queue có rỗng không? ', queue1.isEmpty())

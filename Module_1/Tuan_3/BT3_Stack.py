class MyStack():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__data = []

    def getData(self):
        return self.__data

    def isEmpty(self):
        return len(self.__data) == 0

    def isFull(self):
        return len(self.__data) == self.__capacity

    def popFirstElement(self):
        if self.isEmpty():
            print("Empty")
            return
        return self.__data.pop()

    def pushElement(self, value):
        if self.isFull():
            print("Full")
            return
        return self.__data.append(value)

    def getFirstElement(self):
        if self.isEmpty():
            print("Empty")
            return
        return self.__data[-1]


stack1 = MyStack(capacity=5)
print('Stack ban đầu: ', stack1.getData())
stack1.pushElement(1)
stack1.pushElement(2)
print('Stack sau khi thêm giá trị: ', stack1.getData())
print('Stack đã đủ giá trị chưa? ', stack1.isFull())
print('Lấy giá trị vừa thêm vào: ', stack1.getFirstElement())
print('Giá trị vừa xóa: ', stack1.popFirstElement())
print('Lấy giá trị tiếp theo: ', stack1.getFirstElement())
print('Giá trị vừa xóa: ', stack1.popFirstElement())
print('Stack có rỗng không? ', stack1.isEmpty())

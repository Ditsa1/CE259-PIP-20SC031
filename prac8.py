# 20CS031 - DITSA MANDANI
# Repo. Link - https://github.com/Ditsa1/CE259-PIP-20SC031

# implement stack like structure
class Stack:

    # initializing
    def __init__(self):
        self.stack = []

    # push operation
    def push(self, value):
        self.stack.append(value)

    # pop operation
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!!\n")
        else:
            self.stack.pop()

    # to check if stack is empty or not
    def isEmpty(self):
        return self.stack == []

    # stack traversal
    def traversal(self):
        print(f' stack =  {self.stack[::-1]}')


s = Stack()

print("Enter from below option: \n")
while True:
    print("1. Push to stack.")
    print("2. Pop from stack.")
    print("3. Traverse the stack.")
    print("4. Is the stack empty?")
    print("5. End program.")

    choice = int(input())

    if choice == 1:
        print("Enter element: ")
        element = int(input())
        s.push(element)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.traversal()
    elif choice == 4:
        status = s.isEmpty()
        print(f'Empty Status : {status}\n')
    elif choice == 5:
        break
    else:
        print("Enter proper choice!!\n")
        continue

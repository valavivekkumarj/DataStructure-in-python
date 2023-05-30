queue = []


def isEmpty():
    if not queue:
        return True


def display():
    print(queue)


def enqueue(data):
    queue.append(data)
    display()


def dequeue():
    if isEmpty():
        print("queue is empty")
    else:
        a = queue.pop(0)
        print(a)


def front():
    if isEmpty():
        print("queue is empty")
    else:
        print(queue[0])


def rear():
    if isEmpty():
        print("queue is empty")
    else:
        print(queue[-1])


print("stack is 'lifo' type data structure :")
print("operation performed on stack:1.push  2.pop  3.peek  4.displaystack")

while True:
    choice = int(
        input(
            """enter choice : 
                                        1.enqueue
                                        2.dequeue 
                                        3.front
                                        4.rear  
                                        5.displaystack 
                                        6.exit"""
        )
    )

    if choice == 1:
        data = int(input("enter data to push"))
        enqueue(data)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        front()
    elif choice == 4:
        rear()
    elif choice == 5:
        display()
    elif choice == 6:
        print("EXIT")
        break
    else:
        print("enter valid choice")

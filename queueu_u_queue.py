import queue

q = queue.Queue()


def isEmpty():
    if not q:
        return True


def display():
    if isEmpty():
        print("queue is empty")
    else:
        print(q)


def enqueue(data):
    q.put(data)
    display()


def dequeue():
    if isEmpty():
        print("quueue is empty")

    else:
        print(q.get())


def front():
    if isEmpty():
        print("quueue is empty")

    else:
        print(q[0])


def rear():
    if isEmpty():
        print("quueue is empty")

    else:
        print(q[-1])


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

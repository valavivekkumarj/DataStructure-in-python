import collections

queue = collections.deque()

"""here we use deque() from collection class to implement queue 
 deque()  have several method like 
 append("add data to end ) ,pop(delete data from end) ,appendleft(add data to front) 
 ,popleft(delete data from front)"""


def isEmpty():
    if not queue:
        return True


def display():
    if not queue:
        print("queue is empty")
    else:
        print(queue)


def enqueue(data):
    queue.append(data)
    display()


def dequeue():
    if isEmpty():
        print("queue is empty")
    else:
        a = queue.popleft()
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


# user interface with code logic
while True:
    choice = int(
        input(
            """enter choice : 
                                1.enqueue
                                2.dequeue  
                                3.front  
                                4.rear
                                5.dispaly 
                                6.exit"""
        )
    )

    if choice == 1:
        a = int(input("enter data to enqueu"))
        enqueue(a)

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

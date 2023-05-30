import queue

stack = queue.LifoQueue()

print("stack is 'lifo' type data structure :")
print("operation performed on stack:1.push  2.pop  3.peek  4.displaystack")

while True:
    choice = int(
        input(
            """enter choice : 
                                        1.push
                                        2.pop  
                                        3.peek  
                                        4.displaystack 
                                        5.exit"""
        )
    )

    if choice == 1:
        a = int(input("enter data to push"))
        stack.put(a)
        print(stack)

    elif choice == 2:
        if not stack:
            print("stack is underflow")
        else:
            o = stack.get()
            print(o)
            print(stack)
    elif choice == 3:
        if not stack:
            print("stack is underflow")
        else:
            print(stack[-1])
    elif choice == 4:
        if not stack:
            print("stack is underflow")
        else:
            print(stack)
    elif choice == 5:
        print("EXIT")
        break
    else:
        print("enter valid choice")

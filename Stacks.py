stack = [None for index in range(0,10)]
basePointer = 0
topPointer = -1
stackFull = 10
item = None

def pop():
    global topPointer, basePointer, item 
    
    if topPointer == basePointer -1:
        print("Stack is empty,cannot pop")
        
    else:
        item = stack[topPointer]
        topPointer = topPointer -1

def push(item):
    global topPointer 
    
    if topPointer < stackFull - 1:
        topPointer = topPointer + 1
        stack[topPointer] = item
        
    else:
        print("Stack is full, cannot push")


push(7)
push(10)
push(27)

pop()

push(5)

print(*stack)
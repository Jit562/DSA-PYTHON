def create_stack():
    '''
    stack ( LIFO ) last input and first output ,
    create the stack
    '''
    stack = []
    return stack

def check_empty(stack):
    '''
    Check the stack data
    '''
    return len(stack) == 0

def push_stack(stack, item):
    '''
    push the data in stack
    '''
    stack.append(item)

    print("Push item: " + item)

def pop(stack):
    '''
     remove the data in stack
    '''  
    if check_empty(stack):
        return "stack is empty"
    
    return stack.pop()

stack = create_stack()

push_stack(stack, str(1))
push_stack(stack, str(2))
push_stack(stack, str(3))
push_stack(stack, str(4))
push_stack(stack, str(5))
push_stack(stack, str(6))

print("pop item: " + pop(stack))

print("After pop item: " + str(stack))







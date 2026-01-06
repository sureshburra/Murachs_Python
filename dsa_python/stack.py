def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"
    return stack.pop()

:wq


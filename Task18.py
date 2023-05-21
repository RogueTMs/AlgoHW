PRIORITY = {1: ['||'], 2: ['&'], 3: ['<<', '>>'], 4: ['+', '-'], 5: ['*', '/', '%'], 6: ['^']}
RIGHT = '^'


def priority(first, second):
    prior1, prior2 = 0, 0
    for key, val in PRIORITY.items():
        if first in val:
            prior1 = key
        if second in val:
            prior2 = key

    if prior1 > prior2:
        return 1
    elif prior1 < prior2:
        return -1
    else:
        return 0


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            val = self.head.val
            self.head = self.head.next
            return val

    def peek(self):
        if self.head is None:
            return None
        return self.head.val

    def is_empty(self):
        if self.head:
            return True
        else:
            return False


def pol_notation(data):
    res = ''
    stack = Stack()
    data = data.replace(' ', '')

    for elem in data:
        if elem == '(':
            stack.push('(')

        elif elem == ')':
            check = stack.pop()
            while check != '(':
                res += check
                check = stack.pop()

        elif elem.isdigit():
            res += elem

        else:
            check = priority(elem, stack.peek())
            if check == 1:
                stack.push(elem)
            else:
                if elem in RIGHT:
                    check = 0
                else:
                    check = 1
                oper = stack.peek()
                while priority(elem, oper) < check:

                    oper = stack.pop()
                    if oper is None:
                        break
                    res += oper
                stack.push(elem)

    while stack.head:
        res += stack.pop()
    return res


test = '8 + ((9 * 4) + 5) ^ 2 + 1 / 2'
print(pol_notation(test))

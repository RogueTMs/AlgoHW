PRIORITY = {1: ['+', '-'], 2: ['*', '/']}


def priority(value: str) -> int:
    for k, v in PRIORITY.items():
        if value in v:
            return k
    return -1


def pol_notation(expr: str) -> str:
    result = []
    stack = []
    for element in expr:
        if element not in '+-*/':
            result.append(element)
        else:
            last = None if not stack else stack[-1]
            while priority(last) >= priority(element):
                result.append(stack.pop())
                last = None if not stack else stack[-1]
            stack.append(element)
    for e in reversed(stack):
        result.append(e)
    return ''.join(result)
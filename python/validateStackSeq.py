def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    stack = []
    for val in pushed:
        stack.append(val)
        while stack and popped and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
    return False if stack else True

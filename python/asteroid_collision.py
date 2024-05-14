def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for val in asteroids:
        if val < 0 and len(stack) > 0 and stack[len(stack) - 1] > 0:
            while (
                len(stack)
                and stack[len(stack) - 1] > 0
                and stack[len(stack) - 1] <= abs(val)
            ):
                if stack[len(stack) - 1] == abs(val):
                    stack.pop()
                    break
                stack.pop()
            else:
                if (len(stack) and stack[len(stack) - 1] < 0) or not len(stack):
                    stack.append(val)
        else:
            stack.append(val)
    return stack


print(asteroidCollision([5, 10, -5]))

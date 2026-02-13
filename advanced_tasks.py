def reverse_string(text_to_invert: str) -> str:
    text  = list(text_to_invert)
    stack = []
    for _ in range(len(text)):
        stack.append(text.pop())
    return ''.join(stack)

#print(reverse_string(input()))

def matching_parentheses(algebraic_expression:str) -> list:
    stack = []
    parentheses_indexes = []
    for i in range (len(algebraic_expression)):
        if algebraic_expression[i] == "(":
            parentheses_indexes.append(i)
        elif algebraic_expression[i] == ")":
            if parentheses_indexes:
                start_index = parentheses_indexes.pop()
                close_index = i + 1
                phrase = algebraic_expression[start_index:close_index]
                stack.append(phrase)
    return stack
# res = matching_parentheses(input())
# for item in res:
#     print(item)

def supermarket():
    from collections import deque

    supermarket_queue = deque()
    while True:
        person = input()
        if person == "End":
            break
        elif person == "Paid":
            while   supermarket_queue:
                 print(supermarket_queue.popleft())
            continue
        supermarket_queue.append(person)

    print(f"{len(supermarket_queue)} people remaining.")

def supermarket_deque():
    from collections import deque

    supermarket_queue = deque()
    while True:
        person = input()
        if person == "End":
            break
        elif person == "Paid":
            while   supermarket_queue:
                 supermarket_queue.popleft()
            continue
        supermarket_queue.append(person)

    print(f"{len(supermarket_queue)} people remaining.")
#supermarket()

def supermarket_pop():
    supermarket_queue = []
    while True:
        person = input()
        if person == "End":
            break
        elif person == "Paid":
            while   supermarket_queue:
                 supermarket_queue.pop(0)
            continue
        supermarket_queue.append(person)

    print(f"{len(supermarket_queue)} people remaining.")


if __name__ == '__main__':
     supermarket()
     supermarket_pop()
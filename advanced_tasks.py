def reverse_string(text_to_invert: str) -> str:
    text = list(text_to_invert)
    stack = []
    for _ in range(len(text)):
        stack.append(text.pop())
    return ''.join(stack)


# print(reverse_string(input()))

def matching_parentheses(algebraic_expression: str) -> list:
    stack = []
    parentheses_indexes = []
    for i in range(len(algebraic_expression)):
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
            while supermarket_queue:
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
            while supermarket_queue:
                supermarket_queue.popleft()

            continue
        supermarket_queue.append(person)

    print(f"{len(supermarket_queue)} people remaining.")


def supermarket_list_pop():
    supermarket_queue = []
    while True:
        person = input()
        if person == "End":
            break
        elif person == "Paid":
            while supermarket_queue:
                supermarket_queue.pop(0)
            continue
        supermarket_queue.append(person)

    print(f"{len(supermarket_queue)} people remaining.")


def water_dispenser():
    from collections import deque
    litres = int(input())
    people_queue = deque()

    while True:
        person = input()

        if person == "Start":
            break
        people_queue.append(person)

    while True:
        received_command = input()
        if received_command == "End":
            break
        command = received_command.split()
        if "refill" not in command:

            litres_need = int(command[0])
            if people_queue:
                person_s_name = people_queue.popleft()
                if litres >= litres_need:
                    litres -= litres_need
                    print(f"{person_s_name} got water")

                else:
                    print(f"{person_s_name} must wait")
            else:
                print(f"We have no people in the queue")

        else:
            litres_for_adding = int(command[1])
            litres += litres_for_adding

    print(f"{litres} liters left")


def hot_potato():
    from collections import deque

    names = deque(input().split())
    number = int(input())
    while len(names) > 1:
        names.rotate(-(number - 1))
        print(f"Removed {names.popleft()}")

    print(f"Last is {names[0]}")


def reverse_numbers():
    line_of_numbers = input().split()
    stack = []
    while line_of_numbers:
        stack.append(line_of_numbers.pop())
    print(" ".join(stack))


def stacked_queries():
    n = int(input())
    stack = []
    for _ in range(n):
        command = input()
        if command == "2":
            if stack:
                stack.pop()
        elif command == "3":
            if stack:
                print(max(stack))
        elif command == "4":
            if stack:
                print(min(stack))
        else:
            # command = 1
            number = int(command.split()[1])
            stack.append(number)

    print(", ".join(map(str, reversed(stack))))


def fast_food():
    from collections import deque
    food_quantity = int(input())
    food_purchases = deque(map(int, input().split()))

    if food_purchases:
        print(max(food_purchases))
    while food_purchases and food_purchases[0] <= food_quantity:
        food_quantity -= food_purchases.popleft()

    if food_purchases:
        print("Orders left:", *food_purchases)
    else:
        print("Orders complete")


def fashion_boutique():
    delivered_close = list(map(int, input().split()))
    capacity = int(input())
    current_box_capacity = capacity
    count_of_boxes = 1

    while delivered_close:
        current_close = delivered_close.pop()
        if current_close <= current_box_capacity:
            current_box_capacity -= current_close
        else:
            count_of_boxes += 1
            current_box_capacity = capacity - current_close

    print(f"{count_of_boxes}")


def truck_tour():
    from collections import deque
    petrol_stations = int(input())
    total_track = deque()
    for petrol_number in range(petrol_stations):
        amount_of_petrol, distance = input().split()
        total_track.append({"petrol_number": petrol_number, "fuel": int(amount_of_petrol), "distance": int(distance)})

    stops = 0
    while stops < petrol_stations:

        current_fuel = 0
        for track in total_track:
            if (current_fuel + track["fuel"]) >= track["distance"]:
                current_fuel += track["fuel"]
                current_fuel -= track["distance"]
                stops += 1
            else:
                total_track.rotate(-1)
                stops = 0
                break

    print(total_track[0]["petrol_number"])


def balanced_parentheses():

    phrase = input()
    open_parentheses = []
    parentheses_dic = {"{": "}", "[": "]", "(": ")"}
    for char in phrase:
        if char in parentheses_dic.keys():
            open_parentheses.append(char)
        else:
                if len(open_parentheses) == 0 or char != parentheses_dic[open_parentheses.pop()] :
                    print("NO")
                    return


    if not open_parentheses:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    balanced_parentheses()

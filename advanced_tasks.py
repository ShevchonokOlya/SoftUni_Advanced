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
            if len(open_parentheses) == 0 or char != parentheses_dic[open_parentheses.pop()]:
                print("NO")
                return

    if not open_parentheses:
        print("YES")
    else:
        print("NO")


def convert(seconds: int) -> str:
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d:%02d" % (hour, minutes, seconds)


def robotics():
    from collections import deque
    robots = [val.split("-") for val in input().split(";")]

    robot_dict = {}
    for robot in robots:
        robot_dict[robot[0]] = [int(robot[1]), 0]

    hours, minutes, seconds = map(int, input().split(":"))
    time_in_seconds = (hours * 3600 + minutes * 60 + seconds)

    products = deque()

    while True:
        product = input()
        if product == "End":
            break
        else:
            products.append(product)

    while products:
        time_in_seconds += 1

        for robot_n, [working_time, freedom_timer] in robot_dict.items():
            if freedom_timer <= time_in_seconds:
                final_time = time_in_seconds + working_time
                robot_dict[robot_n] = [working_time, final_time]
                time_result = convert(time_in_seconds)
                product_identification = products.popleft()
                print(f"{robot_n} - {product_identification} [{time_result}]")
                break
        else:
            products.rotate(-1)


def key_revolver():
    from collections import deque
    bullets_price = int(input())  # 0-100
    gun_barrel_size = int(input())  # 1-5000
    bullets = list(map(int, input().split()))  # [1-100]

    locks = deque(map(int, input().split()))  # [1-100]
    intelligence_value = int(input())  # [1-100000]

    current_burrel = 0
    amount_of_shoot = 0

    while locks and bullets:
        lock_to_soot = locks[0]
        bullet = bullets.pop()
        current_burrel += 1

        amount_of_shoot += 1
        if lock_to_soot >= bullet:
            print("Bang!")
            locks.popleft()
        else:
            print("Ping!")

        if current_burrel == gun_barrel_size and bullets:
            print("Reloading!")
            current_burrel = 0

    if not locks:
        money_earned = intelligence_value - bullets_price * amount_of_shoot
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")


def crossroads():
    from collections import deque
    duration_green_light = int(input())
    free_window_seconds = int(input())
    cars_in_traffic = deque()
    success = 0

    while True:
        car_or_color = input()
        if car_or_color == "END":
            break
        elif car_or_color == "green":
            current_green = duration_green_light

            while cars_in_traffic and current_green > 0:
                new_car = cars_in_traffic.popleft()
                current_car_lenght = len(new_car)

                if current_car_lenght <= current_green:
                    # car passed safely throw green light
                    success += 1
                    current_green -= current_car_lenght

                elif current_green < current_car_lenght <= current_green + free_window_seconds:
                    success += 1
                    current_green = 0
                    break

                elif current_car_lenght > current_green + free_window_seconds:
                    index = current_green + free_window_seconds
                    print(f"A crash happened!\n{new_car} was hit at {new_car[index]}.")
                    return

        else:
            car = car_or_color
            cars_in_traffic.append(car)

    print(f"Everyone is safe.\n{success} total cars passed the crossroads.")


def cups_and_bottles():
    from collections import deque
    cups = deque(int(cup) for cup in input().split())  # litres - starts from first
    bottles = [int(bottle) for bottle in input().split()]  # litres - starts from last
    waisted_water = 0

    while cups and bottles:

        current_cup = cups[0]

        while current_cup > 0 and bottles:
            current_bottle = bottles.pop()

            if current_bottle > current_cup:
                waisted_water += current_bottle - current_cup

            current_cup -= current_bottle
            if current_cup <= 0:
                cups.popleft()

    if not cups:
        print("Bottles:", " ".join(map(str, bottles)))

    if cups and not bottles:
        print("Cups:", " ".join(map(str, cups)))

    print(f"Wasted litters of water: {waisted_water}")




def count_same_values():
    numbers = tuple(map(str, input().split()))
    set_of_numbers = set(numbers)
    for number in numbers:
        if number in set_of_numbers:
            print(f"{float(number):.1f} - {numbers.count(number)} times")
            set_of_numbers.remove(number)


def students_grades():
    n = int(input())
    student_grades = {}

    for _ in range(n):
        student = tuple(input().split())
        student_grades[student[0]] = student_grades.get(student[0], []) + [float(student[1])]

    for student_name, marks in student_grades.items():
        average_grade = sum(marks) / len(marks)
        marks = [mark for mark in marks]
        print(f"{student_name} -> {' '.join([f'{el:.2f}' for el in marks])} (avg: {average_grade:.2f})")


def record_unique_names():
    number_of_unique_names = int(input())
    names: set = set()
    for _ in range(number_of_unique_names):
        names.add(input())
    [print(name) for name in names]


def parking_lot():
    car_number = int(input())
    car_registration_numbers = set()

    for _ in range(car_number):
        car = tuple(input().split(","))
        if car[0] == "IN":
            car_registration_numbers.add(car[1])
        else:
            if car[1] in car_registration_numbers:
                car_registration_numbers.remove(car[1])

    if len(car_registration_numbers) == 0:
        print("Parking Lot is Empty")
    else:
        print("\n".join(car_registration_numbers))


def soft_uni_party():
    number_of_guests = int(input())
    reservation_numbers = set()
    for _ in range(number_of_guests):
        reservation = input()
        if len(reservation) == 8:
            reservation_numbers.add(reservation)

    while True:
        entered_guest = input()
        if entered_guest == "END":
            break
        if entered_guest in reservation_numbers:
            reservation_numbers.remove(entered_guest)

    print(len(reservation_numbers))
    sorted_guests = sorted([guest for guest in reservation_numbers])
    print("\n".join(sorted_guests))


def summation_pairs():
    import time
    unique_integers = set([int(number) for number in input().split()])
    target_number = int(input())

    start = time.perf_counter()

    result = set()

    while unique_integers:
        number = unique_integers.pop()
        pair_number = target_number - int(number)

        if pair_number in unique_integers:
            unique_integers.remove(pair_number)
            result.add((number, pair_number))

    for pair_of_numbers in result:
        print(f"{pair_of_numbers[0]} + {pair_of_numbers[1]} = {target_number}")


# print(time.perf_counter() - start)


def sum_pairs():
    import time
    numbers = list(map(int, input().split()))
    target = int(input())

    start = time.perf_counter()
    targets = set()
    values_map = {}
    for value in numbers:

        if value in targets:
            targets.remove(value)
            pair = values_map[value]
            del values_map[value]
            print(f'{pair} + {value} = {target}')

        else:
            resulting_number = target - value
            targets.add(resulting_number)
            values_map[resulting_number] = value

    # print(time.perf_counter() - start)


def unique_usernames():
    names = set()
    for _ in range(int(input())):
        names.add(input())
    print(*names, sep="\n")


def sets_of_elements():
    set1_length, set2_length = (int(num) for num in input().split())

    set1 = set()
    set2 = set()
    for _ in range(set1_length):
        set1.add(input())
    for _ in range(set2_length):
        set2.add(input())
    print(*(set1 & set2), sep="\n")


def periodic_table():
    elements = set()
    for _ in range(int(input())):
        elements = elements.union(input().split())
    print(*elements, sep="\n")


def count_symbols():
    txt = input()
    symbols = set(txt)
    for ch in sorted(symbols):
        print(f"{ch}: {txt.count(ch)} time/s")


def get_elements(interval_string: str) -> list:
    section1, section2 = interval_string.split("-")
    start_1, end_1 = map(int, section1.split(","))
    start_2, end_2 = map(int, section2.split(","))

    section1 = set(int(num) for num in range(start_1, end_1 + 1))
    section2 = set(int(num) for num in range(start_2, end_2 + 1))
    return list(section1 & section2)


def longest_intersection():
    result_interval = []
    max_list_len = -1
    for _ in range(int(input())):
        intersection = get_elements(input())
        if len(intersection) > max_list_len:
            max_list_len = len(intersection)
            result_interval = intersection.copy()
    print(f"Longest intersection is {result_interval} with length {max_list_len}")


def battle_of_names():
    even = set()
    odd = set()
    for counter in range(0, int(input())):
        counter += 1
        name_price = sum([ord(ch) for ch in input()])
        name_price //= counter
        even.add(name_price) if name_price % 2 == 0 else odd.add(name_price)


    odd_sum = sum(odd)
    even_sum = sum(even)

    if odd_sum == even_sum:
        print(*(odd.union(even)), sep=", ")
    elif odd_sum > even_sum:
        print(*(odd.difference(even)), sep=", ")
    else:
        print(*(even.symmetric_difference(odd)), sep=", ")

if __name__ == '__main__':
    pass

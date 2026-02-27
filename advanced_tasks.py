from dataclasses import field


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
                current_car_length = len(new_car)

                if current_car_length <= current_green:
                    # car passed safely throw green light
                    success += 1
                    current_green -= current_car_length

                elif current_green < current_car_length <= current_green + free_window_seconds:
                    success += 1
                    break

                elif current_car_length > current_green + free_window_seconds:
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
    # import time
    unique_integers = set([int(number) for number in input().split()])
    target_number = int(input())

    # start = time.perf_counter()

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
    # import time
    numbers = list(map(int, input().split()))
    target = int(input())

    # start = time.perf_counter()
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


def numbers_sequence():
    sequence_of_numbers_1 = set(map(int, input().split()))
    sequence_of_numbers_2 = set(map(int, input().split()))
    for _ in range(int(input())):
        command = input().split()

        if command[0] == "Add":
            numbers_to_add = set(map(int, command[2:]))

            if command[1] == "First":
                sequence_of_numbers_1 = sequence_of_numbers_1.union(numbers_to_add)
            else:
                sequence_of_numbers_2 = sequence_of_numbers_2.union(numbers_to_add)

        elif command[0] == "Remove":
            numbers_to_remove = set(map(int, command[2:]))
            if command[1] == "First":
                sequence_of_numbers_1 -= numbers_to_remove
            else:
                sequence_of_numbers_2 -= numbers_to_remove

        elif command[0] == "Check":
            if sequence_of_numbers_2 <= sequence_of_numbers_1 or sequence_of_numbers_1 <= sequence_of_numbers_2:

                print("True")
            else:
                print("False")
    print(*sorted(sequence_of_numbers_1), sep=", ")
    print(*sorted(sequence_of_numbers_2), sep=", ")


def expression_evaluator():
    from collections import deque
    numbers = deque()
    input_expression = input().split()
    current_num = 0
    for expr in input_expression:
        if expr.lstrip('-').isdigit():
            numbers.append(int(expr))
        else:

            if expr == "+":
                current_num = numbers.popleft()

                while numbers:
                    current_num += numbers.popleft()

            elif expr == "-":
                current_num = numbers.popleft()
                while numbers:
                    current_num -= numbers.popleft()

            elif expr == "*":
                current_num = numbers.popleft()
                while numbers:
                    current_num *= numbers.popleft()

            elif expr == "/":
                current_num = numbers.popleft()
                while numbers:
                    current_num = current_num // numbers.popleft()

            numbers.appendleft(current_num)
    print(current_num)


def milkshakes():
    from collections import deque
    chocolate = list(map(int, input().split(", ")))
    milk_cups = deque(map(int, input().split(', ')))
    milkshake_count = 0

    while milk_cups and chocolate:

        current_chocolate = chocolate[-1]
        current_milk = milk_cups[0]

        if current_chocolate <= 0 or current_milk <= 0:
            if current_chocolate <= 0:
                chocolate.pop()
            if current_milk <= 0:
                milk_cups.popleft()
            continue

        if current_chocolate == current_milk:
            chocolate.pop()
            milk_cups.popleft()
            milkshake_count += 1
        else:
            milk_cups.rotate(-1)
            chocolate[-1] -= 5

        if milkshake_count >= 5:
            break
    if milkshake_count < 5:
        print("Not enough milkshakes.")
    else:
        print("Great! You made all the chocolate milkshakes needed!")

    if chocolate:
        print("Chocolate:", ", ".join(map(str, chocolate)))
    else:
        print("Chocolate: empty")
    if milk_cups:
        print("Milk:", ", ".join(map(str, milk_cups)))
    else:
        print("Milk: empty")


def honey():
    from collections import deque

    bees = deque(map(int, input().split()))
    nectar = list(map(int, input().split()))
    symbols = deque(input().split())
    total_honey = 0

    while bees and nectar:
        current_bee = bees[0]
        current_nectar = nectar[-1]

        if current_bee <= current_nectar:

            symbol = symbols.popleft()

            if symbol == "+":
                total_honey += current_bee + current_nectar
            elif symbol == "-":
                total_honey += abs(current_bee - current_nectar)
            elif symbol == "*":
                total_honey += current_bee * current_nectar
            elif symbol == "/":
                if current_nectar != 0:
                    total_honey += current_bee / current_nectar

            bees.popleft()
            nectar.pop()
        else:
            nectar.pop()
            continue

    print(f"Total honey made: {total_honey}")
    if bees:
        print(f"Bees left: {', '.join(map(str, bees))}")
    if nectar:
        print(f"Nectar left: {', '.join(map(str, nectar))}")


def santa_present_factory():
    from collections import deque
    boxes_with_materials = list(map(int, input().split()))
    magic_values = deque(map(int, input().split()))
    presents = {}

    toys = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}

    while boxes_with_materials and magic_values:
        material = boxes_with_materials[-1]
        magic = magic_values[0]
        total_magic = material * magic
        if total_magic < 0:
            current_magic = boxes_with_materials.pop() + magic_values.popleft()
            boxes_with_materials.append(current_magic)
            continue
        elif total_magic == 0:
            if material == 0:
                boxes_with_materials.pop()
            if magic == 0:
                magic_values.popleft()
        else:
            if total_magic in toys.values():
                toy = [key for key, val in toys.items() if val == total_magic][0]
                presents[toy] = presents.get(toy, 0) + 1
                boxes_with_materials.pop()
                magic_values.popleft()
            else:
                magic_values.popleft()
                boxes_with_materials[-1] += 15

    if ("Doll" in presents.keys() and "Wooden train" in presents.keys()) or (
            "Teddy bear" in presents.keys() and "Bicycle" in presents.keys()):

        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")

    if boxes_with_materials:
        print(f"Materials left: {', '.join(map(str, (boxes_with_materials[::-1])))}")
    if magic_values:
        print(f"Magic left: {', '.join(map(str, magic_values))}")
    for present, amount in sorted(presents.items()):
        print(f"{present}: {amount}")


def paint_colors():
    colors = input().split()
    main_colors = {"red", "yellow", "blue"}
    secondary_colors = {
        "orange": ["red", "yellow"],
        "purple": ["red", "blue"],
        "green": ["yellow", "blue"]}

    found_colors = []

    while colors:
        first_color = colors.pop(0)
        second_color = colors.pop(-1) if colors else ""

        one = str(first_color + second_color)
        second = str(second_color + first_color)

        if one in main_colors or one in secondary_colors.keys():
            found_colors.append(one)
        elif str(second) in main_colors or second in secondary_colors.keys():
            found_colors.append(second)
        else:
            first_color = first_color[:-1]
            second_color = second_color[:-1]
            if first_color:
                colors.insert(len(colors) // 2, first_color)
            if second_color:
                colors.insert(len(colors) // 2, second_color)

    for color in found_colors:
        if color in secondary_colors.keys():
            needed_colors = set(secondary_colors[color])
            all_colors = set(found_colors)
            if not needed_colors.issubset(all_colors):
                found_colors.remove(color)

    print(found_colors)


def sum_matrix_elements():
    row, column = map(int, input().split(", "))
    sum_of_numbers = 0
    matrix = []
    for _ in range(row):
        list_of_numbers = list(map(int, input().split(", ")))
        matrix.append(list_of_numbers)
        sum_of_numbers += sum(list_of_numbers)
    print(sum_of_numbers)
    print(matrix)


def even_matrix():
    matrix = []
    for _ in range(int(input())):
        matrix.append([int(num) for num in input().split(", ") if int(num) % 2 == 0])
    print(matrix)


def flattening_matrix():
    matrix = []
    for _ in range(int(input())):
        matrix.append([int(num) for num in input().split(", ")])
    print([num for row in matrix for num in row])


def sum_matrix_columns():
    matrix = []
    rows, column = map(int, input().split(", "))

    for _ in range(rows):
        matrix.append([int(num) for num in input().split()])

    for col in range(column):
        sum_of_col = 0
        for row in range(rows):
            sum_of_col += matrix[row][col]
        print(sum_of_col)


def primary_diagonal():
    matrix = []
    n = int(input())
    for _ in range(n):
        matrix.append([int(num) for num in input().split()])
    print(sum([matrix[i][i] for i in range(n)]))


def symbol_in_matrix():
    matrix = []
    for _ in range(int(input())):
        matrix.append(input())
    symbol = input()
    row = [i for i in range(len(matrix)) if symbol in matrix[i]]
    if row:
        col = matrix[row[0]].index(symbol)
        print(f"({row[0]}, {col})")
    else:
        print(f"{symbol} does not occur in the matrix")


def square_with_maximum_sum():
    row, column = map(int, input().split(", "))
    matrix = []
    for _ in range(row):
        list_of_numbers = list(map(int, input().split(", ")))
        matrix.append(list_of_numbers)

    sum_of_square = 0
    best_square = []
    for i in range(0, row - 1):
        for j in range(0, column - 1):
            current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
            if current_sum > sum_of_square:
                sum_of_square = current_sum
                best_square = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]

    num = len(best_square)
    for i in range(num):
        print(" ".join(map(str, best_square[i])))

    print(sum_of_square)


def diagonals():
    matrix = [[int(num) for num in input().split(", ")] for _ in range(int(input()))]
    primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
    secondary_diagonal = [matrix[i][-i - 1] for i in range(len(matrix))]

    print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
    print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")


def diagonal_difference():
    matrix = []
    for _ in range(int(input())):
        matrix.append([int(num) for num in input().split()])

    primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
    secondary_diagonal = [matrix[i][-i - 1] for i in range(len(matrix))]
    difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
    print(difference)


def squares_in_matrix():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(input().split())

    count = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
                count += 1
    print(count)


def maximal_sum():
    row, column = map(int, input().split())
    matrix = []
    for _ in range(row):
        list_of_numbers = list(map(int, input().split()))
        matrix.append(list_of_numbers)

    best_square = []
    sum_of_square = float('-inf')

    for i in range(0, row - 2):
        for j in range(0, column - 2):
            current_sum = (matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] +
                           matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] +
                           matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2])

            if current_sum > sum_of_square:
                sum_of_square = current_sum
                best_square = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                               [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                               [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]

    print(f"Sum = {sum_of_square}")
    if best_square:
        for i in range(0, 3):
            print(" ".join(map(str, best_square[i])))


def matrix_of_palindromes():
    row, column = map(int, input().split())
    matrix = []
    for i in range(row):
        matrix.append([""] * column)
        for j in range(column):
            matrix[i][j] = f"{chr(97 + i)}{chr(97 + i + j)}{chr(97 + i)}"

        print(*matrix[i])


def matrix_shuffling():
    r, c = map(int, input().split())
    matrix = [[num for num in input().split()] for _ in range(r)]
    while True:
        command = input().split()
        if command[0] == "END":
            break
        elif command[0] == "swap" and len(command) == 5:
            first_row, first_column, second_row, second_col = map(int, command[1:])
            if 0 <= first_row < r and 0 <= first_column < c and 0 <= second_row < r and 0 <= second_col < c:
                matrix[first_row][first_column], matrix[second_row][second_col] = matrix[second_row][second_col], \
                    matrix[first_row][first_column]
                print(*[" ".join(line) for line in matrix], sep="\n")

            else:
                print("Invalid input!")
        else:
            print("Invalid input!")


def snake_moves():
    from collections import deque
    row, col = map(int, input().split())
    snake = deque(input())
    matrix = []

    for row_number in range(row):
        multiplier = (col // len(snake)) + 1
        cur_snake = (list(snake) * multiplier)[:col]

        matrix.append([""] * col)
        if row_number % 2 == 0:
            matrix[row_number] = list(cur_snake)[:col]
        else:
            matrix[row_number] = list(cur_snake)[:col][::-1]

        snake.rotate(-col)

    for mat_row in matrix:
        print(*mat_row, sep="")


def flatten_lists():
    matrix = [[int(num) for num in line.split()] for line in input().split("|") if line]
    final_output = []

    for i in range(len(matrix) - 1, -1, -1):
        final_output.extend(matrix[i])

    print(*final_output)


def validate_coordinates(row_num, col_num, matrix):
    return 0 <= row_num < len(matrix) and 0 <= col_num < len(matrix[0])


def matrix_modification():
    matrix = [list(map(int, input().split())) for _ in range(int(input()))]

    while True:
        command = input().split()
        if command[0] == "END":
            break

        if validate_coordinates(int(command[1]), int(command[2]), matrix):
            if command[0] == "Add" and len(command) == 4:
                matrix[int(command[1])][int(command[2])] += int(command[3])
            elif command[0] == "Subtract" and len(command) == 4:
                matrix[int(command[1])][int(command[2])] -= int(command[3])
        else:
            print("Invalid coordinates")

    for row in matrix:
        print(*row)


def validate_matr_coordinates(row_num, col_num, matrix):
    return 0 <= row_num < len(matrix) and 0 <= col_num < len(matrix[0])


def bombs():
    matrix = []
    for _ in range(int(input())):
        matrix.append(list(map(int, input().split())))
    coordinates = [[int(coord[0]), int(coord[1])] for coord in [coord.split(",") for coord in input().split()]]

    for coord in coordinates:
        row, col = map(int, coord)
        if matrix[row][col] > 0:
            bomb_cel_value = matrix[row][col]
            for mat_row in range(row - 1, row + 2):
                for mat_col in range(col - 1, col + 2):
                    if validate_matr_coordinates(mat_row, mat_col, matrix) and matrix[mat_row][mat_col] > 0:
                        matrix[mat_row][mat_col] -= bomb_cel_value
            matrix[row][col] = 0

    alive_list = [num for row in matrix for num in row if num > 0]
    print(f"Alive cells: {len(alive_list)}")
    print(f"Sum: {sum(alive_list)}")

    for mat_row in matrix:
        print(*mat_row, sep=" ")


def miner():
    field_size = int(input())
    movement_commands = input().split()
    s_coord = []
    coal = []
    the_field = []

    for index_row in range(field_size):
        line = input().split()
        the_field.append(line)
        if "s" in line:
            s_coord = [index_row, line.index("s")]
        c_indexes = [i for i, char in enumerate(line) if char == 'c']
        for c_index in c_indexes:
            coal.append([index_row, c_index])

    movements = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "left": lambda x, y: (x, y - 1),
        "right": lambda x, y: (x, y + 1),
    }

    for move in movement_commands:
        new_row, new_col = movements[move](s_coord[0], s_coord[1])
        if 0 <= new_col < field_size and 0 <= new_row < field_size:
            s_coord = [new_row, new_col]
            if the_field[new_row][new_col] == "e":
                print(f"Game over! ({new_row}, {new_col})")
                return
            elif the_field[new_row][new_col] == "c":
                the_field[new_row][new_col] = "*"
                coal.remove([new_row, new_col])

    if not coal:
        print(f"You collected all coal! ({s_coord[0]}, {s_coord[1]})")
    else:
        print(f"{len(coal)} pieces of coal left. ({s_coord[0]}, {s_coord[1]})")

def bunnies_spred(field, current_bunnies_coordinates):

    new_bunnies = set()
    person_dead = False

    spreading_bunnies = [ (-1, 0), (1, 0), (0, -1), (0, 1)  ]
    for bunny in current_bunnies_coordinates:
        for row, col in spreading_bunnies:
            if 0 <= bunny[0]+row < len(field) and 0 <= bunny[1] + col < len(field[0]):
                new_bunnies.add((bunny[0]+row, bunny[1]+col))
                if field[bunny[0]+row][bunny[1]+col] == "P":
                    person_dead = True
                field[bunny[0] + row][bunny[1] + col] = "B"

    return field, current_bunnies_coordinates.union(new_bunnies), person_dead

def radioactive_mutate_vampire_bunnies():
    row, col = map(int, input().split())
    the_field = []
    person_row, person_col = float("inf"), -100
    bunnies_coordinates = set()

    person_won = False
    person_dead = False
    person_dead_under_bunnies = False

    for index_row in range(row):
        line = list(input())
        the_field.append(line)
        for index_col, char in enumerate(line):
            if char == "P":
                person_row, person_col = index_row, index_col
            elif char == "B":
                bunnies_coordinates.add((index_row, index_col))

    movements = {
        "U": lambda x, y: (x - 1, y),
        "D": lambda x, y: (x + 1, y),
        "L": lambda x, y: (x, y - 1),
        "R": lambda x, y: (x, y + 1),
    }
    commands = list(input())

    for command in commands:
        new_row, new_col = movements[command](person_row, person_col)
        the_field[person_row][person_col] = "."

        if 0 <= new_col < col and 0 <= new_row < row:
            if the_field[new_row][new_col] == "B":
                person_dead = True
            else:
                the_field[new_row][new_col] = "P"
            person_row, person_col = new_row, new_col
        else:
            person_won = True

        the_field, bunnies_coordinates, person_dead_under_bunnies = bunnies_spred(the_field, bunnies_coordinates)

        if person_dead or person_won or person_dead_under_bunnies:
                break

    for line in the_field:
        print(*line, sep="")

    if person_won:
        print(f"won: {person_row} {person_col}")
    if person_dead or person_dead_under_bunnies:
        print(f"dead: {person_row} {person_col}")



radioactive_mutate_vampire_bunnies()


def knight_game():
    matrix = [list(input()) for _ in range(int(input()))]
    print(*matrix)


# knight_game()

if __name__ == '__main__':
    pass

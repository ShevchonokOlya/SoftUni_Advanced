def ball_game():
    from collections import deque

    strength = [int(num) for num in input().split()]
    accuracy = deque(int(number) for number in input().split())
    scored_goals = 0

    while accuracy and strength:
        current_strength = strength[-1]
        current_accuracy = accuracy[0]
        current_kick = current_accuracy + current_strength

        if current_kick == 100:
            strength.pop()
            accuracy.popleft()
            scored_goals += 1

        elif current_kick < 100:
            if current_strength < current_accuracy:
                strength.pop()
            elif current_strength > current_accuracy:
                accuracy.popleft()
            else:
                accuracy.popleft()
                strength[-1] = current_kick

        elif current_kick > 100:
            strength[-1] -= 10
            accuracy.append(accuracy.popleft())

    if scored_goals == 3:
        print("Paul scored a hat-trick!")
    elif scored_goals == 0:
        print("Paul failed to score a single goal.")
    elif scored_goals > 3:
        print("Paul performed remarkably well!")
    elif 0 < scored_goals < 3:
        print("Paul failed to make a hat-trick.")

    if scored_goals:
        print(f"Goals scored: {scored_goals}")

    if strength:
        print("Strength values left:", ", ".join(map(str, strength)))
    if accuracy:
        print("Accuracy values left:", ", ".join(map(str, accuracy)))


def bomb_has_been_planted():
    rows, columns = map(int, input().split(", "))
    counter_row, counter_col = (float("-inf"), float("-inf"))

    start_row, start_col = 0, 0

    movements_amount = 16
    person_dead = False
    person_won = False

    matrix = []

    for row in range(rows):
        line = input()
        matrix.append(list(line))
        if "C" in line:  # counter
            counter_row, counter_col = (row, line.index("C"))
            start_row, start_col = counter_row, counter_col

    movements = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "left": lambda x, y: (x, y - 1),
        "right": lambda x, y: (x, y + 1),
        "defuse": lambda x, y: (x, y),
    }

    while True:
        command = input()
        new_row, new_col = movements[command](counter_row, counter_col)

        if 0 <= new_col < columns and 0 <= new_row < rows:
            if matrix[new_row][new_col] == "T":

                movements_amount -= 1
                matrix[new_row][new_col] = "*"
                person_dead = True
                break

            elif matrix[new_row][new_col] == "B":
                if command == "defuse":
                    movements_amount -= 4
                    if movements_amount >= 0:
                        matrix[new_row][new_col] = "D"
                        person_won = True
                        break
                    else:
                        matrix[new_row][new_col] = "X"
                        person_dead = True
                        break
                else:
                    movements_amount -= 1

            elif matrix[new_row][new_col] == "*" or matrix[new_row][new_col] == "C":
                if command == "defuse":
                    movements_amount -= 2
                else:
                    movements_amount -= 1

            counter_row, counter_col = new_row, new_col

            if movements_amount <= 0:
                break
            if person_dead or person_won:
                break
        else:
            movements_amount -= 1

    matrix[start_row][start_col] = "C"

    if person_won:
        print(f"Counter-terrorist wins!\nBomb has been defused: {movements_amount} second/s remaining.")

    elif person_dead and command == "defuse":
        print(f"Terrorists win!\nBomb was not defused successfully!\nTime needed: {abs(movements_amount)} second/s.")

    elif person_dead:
        print("Terrorists win!")

    else:
        print("Terrorists win!\nBomb was not defused successfully!\nTime needed: 0 second/s.")

    for line in matrix:
        print(*line, sep="")


def list_roman_emperors(*args, **emperors) -> str:
    result_string = f'Total number of emperors: {len(args)}\n'
    unsuccess_imp = {}
    success_imp = {}
    for imp, success in args:
        if success:
            success_imp[imp] = emperors[imp]

        else:
            unsuccess_imp[imp] = emperors[imp]

    success_imp = dict(sorted(success_imp.items(), key=lambda x: (-x[1], x[0])))
    unsuccess_imp = dict(sorted(unsuccess_imp.items(), key=lambda x: (x[1], x[0])))

    if success_imp:
        result_string += f'Successful emperors:\n'
        for emperor_name, number_of_years in success_imp.items():
            result_string += f"****{emperor_name}: {number_of_years}\n"

    if unsuccess_imp:
        result_string += "Unsuccessful emperors:\n"
        for emperor_name, number_of_years in unsuccess_imp.items():
            result_string += f"****{emperor_name}: {number_of_years}\n"

    return result_string.strip()


#
# print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
# print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinacity", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinacity=4, Vespasian=19,))
# print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))

def rapid_courier():
    from collections import deque
    total_weight = 0

    packages_left = list(map(int, input().split()))
    couriers_available = deque(map(int, input().split()))

    while packages_left and couriers_available:
        current_package = packages_left.pop()
        current_courier = couriers_available.popleft()

        if current_courier >= current_package:
            total_weight += current_package
            current_courier -= current_package * 2
            if current_courier > 0:
                couriers_available.append(current_courier)
        else:
            current_package -= current_courier
            packages_left.append(current_package)
            total_weight += current_courier

    print(f"Total weight: {total_weight} kg")

    if not packages_left and not couriers_available:
        print("Congratulations, all packages were delivered successfully by the couriers today.")

    elif packages_left and not couriers_available:
        print(
            f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages_left))}")

    elif couriers_available and not packages_left:
        print(
            f"Couriers are still on duty: {', '.join(map(str, couriers_available))} but there are no more packages to deliver.")


def boarding_passengers(capacity_of_the_ship: int, *passengers):
    total_number_of_guests = {}
    boarded = 0
    current_capacity_of_the_ship = capacity_of_the_ship
    total_guests = sum(p[0] for p in passengers)
    for number_of_passenger, benefit_program in passengers:
        if current_capacity_of_the_ship >= number_of_passenger and current_capacity_of_the_ship > 0:
            total_number_of_guests[benefit_program] = total_number_of_guests.get(benefit_program , 0) + number_of_passenger
            current_capacity_of_the_ship -= number_of_passenger
            boarded += number_of_passenger


    total_number_of_guests = sorted(total_number_of_guests.items(), key=lambda x: (-x[1], x[0]))
    string_result = f"Boarding details by benefit plan:\n"

    for benefit_program, number_of_guests in total_number_of_guests:
        string_result += f'## {benefit_program}: {number_of_guests} guests\n'

    if total_guests == boarded:
        string_result += f"All passengers are successfully boarded!"
    elif total_guests > boarded and capacity_of_the_ship > boarded:
        string_result += f"Partial boarding completed. Available capacity: {current_capacity_of_the_ship}."
    else:
        string_result += f"Boarding unsuccessful. Cruise ship at full capacity."


    return string_result


# print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
# print("\n")
# print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'),
#                           (10, 'Gold')))
# print("\n")
# print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'),
#                           (20, 'Diamond')))

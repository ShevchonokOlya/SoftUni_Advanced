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
            total_number_of_guests[benefit_program] = total_number_of_guests.get(benefit_program,
                                                                                 0) + number_of_passenger
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

def bees():
    field = []

    bee_row, bee_col = float("-inf"), float("-inf")
    initial_energy = 15
    size = int(input())
    collected_nectar = 0
    restoration = False
    reached_hive = False

    for row in range(size):
        line_of_field = list(input())
        field.append(line_of_field)

        for position in line_of_field:
            if position == 'B':
                bee_row = row
                bee_col = line_of_field.index(position)

    command_map = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "left": lambda x, y: (x, y - 1),
        "right": lambda x, y: (x, y + 1),

    }

    while True:
        initial_energy -= 1

        command = input()
        new_row, new_col = command_map[command](bee_row, bee_col)
        if not (0 <= new_col < size and 0 <= new_row < size):
            new_row, new_col = new_row % size, new_col % size
        field[bee_row][bee_col] = "-"
        bee_row, bee_col = new_row, new_col

        if field[new_row][new_col].isdigit():
            collected_nectar += int(field[new_row][new_col])

        elif field[new_row][new_col] == 'H':
            reached_hive = True
            break

        if initial_energy <= 0 and collected_nectar < 30:
            break

        elif initial_energy <= 0 and collected_nectar >= 30 and not restoration:
            initial_energy += collected_nectar - 30
            collected_nectar = 30
            restoration = True

            if initial_energy <= 0:
                break


        elif initial_energy <= 0 and restoration:
            break

    field[bee_row][bee_col] = "B"

    if reached_hive and collected_nectar >= 30:
        print(f"Great job, Bee! The hive is full. Energy left: {initial_energy}")
    elif reached_hive and collected_nectar < 30:
        print(f"Bee did not manage to collect enough nectar.")
    elif not reached_hive and initial_energy <= 0:
        print("This is the end! Bee ran out of energy.")

    for line in field:
        print(*line, sep="")


def cookbook(*dishes) -> str:
    cook_book = {}

    for dish in dishes:
        recipe_name, cuisine_type, ingredients = dish

        if cuisine_type not in cook_book.keys():
            cook_book[cuisine_type] = {}
        cook_book[cuisine_type][recipe_name] = ingredients

    cook_book = dict(sorted(cook_book.items(), key=lambda x: (-len(x[1]), x[0])))

    result_string = ""
    for cuisine_type, recipe_of_dish in cook_book.items():
        result_string += f"{cuisine_type} cuisine contains {len(recipe_of_dish)} recipes:\n"
        for recipe_name, ingredients in sorted(recipe_of_dish.items()):
            result_string += f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n"
    return result_string.strip()


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))
# print("\n")
#
# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
# ))
# print("\n")
# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
#     ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
#     ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
#     ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
# ))
def chicken_snack():
    from collections import deque
    money = list(map(int, input().split()))
    prices = deque(map(int, input().split()))
    henry_eaten = 0

    while money and prices:

        current_money = money.pop()
        current_price = prices.popleft()
        if current_money == current_price:
            henry_eaten += 1

        elif current_money > current_price:
            if money:
                money[-1] += current_money - current_price
            henry_eaten += 1

    if henry_eaten >= 4:
        print(f"Gluttony of the day! Henry ate {henry_eaten} foods.")
    elif henry_eaten > 0:
        extra_s = 's' if henry_eaten > 1 else ''
        print(f"Henry ate: {henry_eaten} food{extra_s}.")
    else:
        print("Henry remained hungry. He will try next weekend again.")


def clear_skies():
    skies = []

    jet_row, jet_col = float("-inf"), float("-inf")

    initial_armor = 300
    size = int(input())

    for row in range(size):
        line_of_sky = list(input())
        skies.append(line_of_sky)

        for position in line_of_sky:
            if position == 'J':
                jet_row = row
                jet_col = line_of_sky.index(position)

    command_map = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "left": lambda x, y: (x, y - 1),
        "right": lambda x, y: (x, y + 1),

    }
    amount_of_enemy = 4
    skies[jet_row][jet_col] = "-"

    while True:
        if initial_armor <= 0:
            break
        command = input().strip()
        new_row, new_col = command_map[command](jet_row, jet_col)
        if 0 <= new_row < size and 0 <= new_col < size:
            if skies[new_row][new_col] == "E":
                initial_armor -= 100
                skies[new_row][new_col] = "-"
                amount_of_enemy -= 1
            elif skies[new_row][new_col] == "R":
                initial_armor = 300
                skies[new_row][new_col] = "-"

            jet_row, jet_col = new_row, new_col

        if amount_of_enemy == 0:
            break
        if initial_armor <= 0:
            break

    if amount_of_enemy == 0:
        print("Mission accomplished, you neutralized the aerial threat!")
    if initial_armor <= 0:
        print(f"Mission failed, your jet fighter was shot down! Last coordinates [{jet_row}, {jet_col}]!")

    skies[jet_row][jet_col] = "J"

    for line in skies:
        print(*line, sep="")


def off_road_challenge():
    from collections import deque
    initial_fuel = list(map(int, input().split()))
    consumption_index = deque(map(int, input().split()))
    quantities = deque(map(int, input().split()))
    reached = 0
    n = 0

    while initial_fuel:
        current_fuel = initial_fuel[-1]
        current_index = consumption_index[0]
        current_quantity = quantities[0]
        n += 1
        if (current_fuel - current_index) >= current_quantity:
            print(f"John has reached: Altitude {n}")
            initial_fuel.pop()
            consumption_index.popleft()
            quantities.popleft()
            reached += 1
        else:
            print(f"John did not reach: Altitude {n}")
            break

    if not quantities:
        print(f"John has reached all the altitudes and managed to reach the top!")
    else:
        print(f"John failed to reach the top.")
        if reached > 0:
            print(f"Reached altitudes: {', '.join(['Altitude ' + str(n) for n in range(1, reached + 1)])}")
    if reached == 0:
        print(f"John didn't reach any altitude.")


def team_lineup(*team_players) -> str:
    players = {}
    for player_name, country in team_players:
        players[country] = players.get(country, []) + [player_name]

    players = dict(sorted(players.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''
    for country_name, players_names in players.items():
        result += f"{country_name}:\n"
        for players_name in players_names:
            result += f"  -{players_name}\n"
    return result


#
#
# print(team_lineup(("Harry Kane", "England"), ("Manuel", "Germany"), ("Sterling", "England"),
#                   ("Toni Kroos", "Germany"), ("Cristiano Ronaldo", "Portugal"), ("Thomas Muller", "Germany")))
# print("\n")
# print(team_lineup(("Lionel Messi", "Argentina"), ("Kylian", "Brazil"), ("Cristiano Ronaldo", "Portugal"),
#                   ("Harry Kane", "England"), ("Kylian", "France"), ("Sterling", "England")))
# print("\n")
# print(team_lineup(("Harry Kane", "England"), ("Manuel", "Germany"), ("Sterling", "England"),
#                   ("Toni Kroos", "Germany"), ("Cristiano Ronaldo", "Portugal"), ("Thomas Muller", "Germany"),
#                   ("Bruno", "Portugal"), ("Bernardo Silva", "Portugal"), ("Harry", "England")))


def command_mapping(command: str, row_number: int, col_number: int) -> (int, int):
    command_map = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "left": lambda x, y: (x, y - 1),
        "right": lambda x, y: (x, y + 1),
    }

    return command_map[command](int(row_number), int(col_number))


def fishing_competition():
    see_size = int(input())
    sea = []
    fisher_row, fisher_col = float("inf"), float("inf")
    for row in range(see_size):
        line = list(input())
        sea.append(line)
        if "S" in line:
            fisher_row, fisher_col = row, line.index("S")

    total_catch = 0
    got_in_whirlpool = False

    while True:
        command = input().strip()
        if command == "collect the nets":
            break

        new_row, new_col = command_mapping(command, fisher_row, fisher_col)
        if not (0 <= new_row < see_size and 0 <= new_col < see_size):
            new_row, new_col = new_row % see_size, new_col % see_size

        sea[fisher_row][fisher_col] = "-"
        fisher_row, fisher_col = new_row, new_col


        if sea[new_row][new_col] == "W":
            got_in_whirlpool = True
            break
        elif sea[new_row][new_col].isdigit():
            total_catch += int(sea[new_row][new_col])
            sea[new_row][new_col] = "-"

    sea[fisher_row][fisher_col] = "S"

    if got_in_whirlpool:
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{fisher_row},{fisher_col}]")
        return

    if total_catch >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(
            f"You didn't catch enough fish and didn't reach the quota! You need {20 - total_catch} tons of fish more.")

    if total_catch > 0:
        print(f"Amount of fish caught: {total_catch} tons.")

    for line in sea:
        print(*line, sep="")



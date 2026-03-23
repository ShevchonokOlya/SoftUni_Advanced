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


def gather_credits(number_of_credits: int, *args):
    courses = set()
    result = ""
    total_credits = 0

    for course_name, course_credits in args:
        if total_credits >= number_of_credits:
            break
        if course_name not in courses:
            courses.add(course_name)
            total_credits += course_credits

    if total_credits >= number_of_credits:
        result += f"Enrollment finished! Maximum credits: {total_credits}.\n"
        result += f"Courses: {', '.join(sorted(courses))}\n"
    else:
        result += f"You need to enroll in more courses! You have to gather {number_of_credits - total_credits} credits more."
    return result.strip()


#
# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))
#
# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))
#
# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))

def temple_of_doom():
    from collections import deque
    tools = deque([int(number) for number in input().split()])
    substances = list(map(int, input().split()))
    challenges = list(map(int, input().split()))

    while tools and substances:
        current_tool = tools.popleft()
        current_substance = substances.pop()
        current_chance = current_tool * current_substance
        if current_chance in challenges:
            challenges.remove(current_chance)
        else:
            current_tool += 1
            tools.append(current_tool)
            current_substance -= 1
            if current_substance != 0:
                substances.append(current_substance)

    if challenges and (not tools or not substances):
        print("Harry is lost in the temple. Oblivion awaits him.")
    else:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
    if tools:
        print(f"Tools: {', '.join(map(str, tools))}")
    if substances:
        print(f"Substances: {', '.join(map(str, substances))}")
    if challenges:
        print(f"Challenges: {', '.join(map(str, challenges))}")


def movement_map(command: str, row_number: int, col_number: int) -> (int, int):
    command_map = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "left": lambda x, y: (x, y - 1),
        "right": lambda x, y: (x, y + 1),
    }

    return command_map[command](int(row_number), int(col_number))


def mouse_in_the_kitchen():
    kitchen_row_size, kitchen_col_size = map(int, input().split(","))

    kitchen = []
    cheese = []
    mouse_row, mouse_col = float("inf"), float("inf")

    for row in range(kitchen_row_size):
        line = list(input())
        kitchen.append(line)
        if "M" in line:
            mouse_row, mouse_col = row, line.index("M")
        if "C" in line:
            for index, el in enumerate(line):
                if el == "C":
                    cheese.append([row, index])

    while True:
        command = input().strip()
        if command == "danger":
            if cheese:
                print("Mouse will come back later!")
            break
        new_row, new_col = movement_map(command, mouse_row, mouse_col)
        if 0 <= new_row < kitchen_row_size and 0 <= new_col < kitchen_col_size:
            if kitchen[new_row][new_col] == "T":
                print("Mouse is trapped!")
                kitchen[mouse_row][mouse_col] = "*"
                kitchen[new_row][new_col] = "M"
                mouse_row, mouse_col = new_row, new_col
                break

            elif kitchen[new_row][new_col] == "C":
                kitchen[mouse_row][mouse_col] = "*"
                kitchen[new_row][new_col] = "M"
                mouse_row, mouse_col = new_row, new_col
                cheese.remove([new_row, new_col])
                if not cheese:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break

            elif kitchen[new_row][new_col] == "@":
                pass

            elif kitchen[new_row][new_col] == "*":
                kitchen[mouse_row][mouse_col] = "*"
                kitchen[new_row][new_col] = "M"
                mouse_row, mouse_col = new_row, new_col

        else:
            print("No more cheese for tonight!")
            break

    for line in kitchen:
        print(*line, sep="")


def click_bait():
    from collections import deque
    final_feed = []

    suggested_links = deque(map(int, input().split()))
    featured_articles = list(map(int, input().split()))
    target_engagement_value = int(input().strip())
    while suggested_links and featured_articles:
        current_link = suggested_links.popleft()
        current_article = featured_articles.pop()
        max_val, max_name = max((current_link, "link"), (current_article, "feature"))
        min_val, min_name = min((current_link, "link"), (current_article, "feature"))
        remainder = max_val % min_val

        if max_val == min_val:
            final_feed.append(0)
        elif max_name == "feature":
            final_feed.append(remainder)
            if remainder != 0:
                featured_articles.append(remainder * 2)
        else:
            final_feed.append((-1) * remainder)
            if remainder != 0:
                suggested_links.append(remainder * 2)


    print(f"Final Feed: {', '.join(map(str, final_feed))}")

    total_final_feed = sum(final_feed)

    if  total_final_feed >= target_engagement_value :
        print(f"Goal achieved! Engagement Value: {total_final_feed}")
    else:
        shortfall = target_engagement_value - total_final_feed
        print(f"Goal not achieved! Short by: {shortfall}")

def plant_garden(garden_space: float, *types_of_plants, **planting_requests):

    plants = {}
    planted_plants = {}
    result = ''
    for type_of_plant, space_require in types_of_plants:
        plants[type_of_plant] = plants.get(type_of_plant, space_require)

    planting_requests = dict(sorted((k, v) for k, v in planting_requests.items() if k in plants))

    for plant_type , quantity in planting_requests.items():

        if plant_type in plants.keys():
            possible_amount =  int(garden_space / plants[plant_type])
            can_be_planted = min(possible_amount, quantity)
            if can_be_planted > 0:
                garden_space  -= can_be_planted * plants[plant_type]
                planting_requests[plant_type] -= can_be_planted
                planted_plants[plant_type] = planted_plants.get(plant_type, 0) + can_be_planted

        if garden_space <= 0:
            break

    if sum(planting_requests.values()) == 0:
        result += f"All plants were planted! Available garden space: {garden_space:.1f} sq meters.\n"
    else:
        result += f"Not enough space to plant all requested plants!\n"

    result += f"Planted plants:\n"

    for k, v in planted_plants.items():
        result += f"{k}: {int(v)}\n"

    return result.strip()

#
# print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
# print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
# print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
# print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))


def movement_space_map(command: str, row_number: int, col_number: int) -> (int, int):
    command_map = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "left": lambda x, y: (x, y - 1),
        "right": lambda x, y: (x, y + 1),
    }

    return command_map[command](int(row_number), int(col_number))

def space_mission():

    space_size = int(input().strip())
    space = []
    current_resources = 100
    planet_row, planet_col = float("inf"), float("inf")
    spaceship_row, spaceship_col = float("inf"), float("inf")
    is_lost = False

    for row in range(space_size):
        line = list(input().split())
        space.append(line)
        if "S" in line:
            spaceship_row, spaceship_col = row, line.index("S")

        if "P" in line:
            planet_row, planet_col = row, line.index("P")


    space[spaceship_row][spaceship_col] = '.'

    while current_resources > 4:
        command = input().strip()
        new_row, new_col = movement_space_map(command, spaceship_row, spaceship_col)
        current_resources -= 5

        if 0 <= new_row < space_size and 0 <= new_col < space_size:
            if space[new_row][new_col] == "R":
                current_resources = min(100, current_resources + 10)
                spaceship_row, spaceship_col = new_row, new_col


            elif space[new_row][new_col] == "M":
                space[new_row][new_col] = '.'
                spaceship_row, spaceship_col = new_row, new_col

                current_resources -= 5

            elif space[new_row][new_col] == "P":
                spaceship_row, spaceship_col = new_row, new_col
                break

            else:
                spaceship_row, spaceship_col = new_row, new_col

        else:
            is_lost = True
            break

    if not (spaceship_row == planet_row and spaceship_col == planet_col):
        space[spaceship_row][spaceship_col] = 'S'

    if planet_row == spaceship_row and planet_col == spaceship_col and current_resources >= 0:
        print(f"Mission accomplished! The spaceship reached Planet B with {current_resources} resources left.")
    elif is_lost:
        print(f"Mission failed! The spaceship was lost in space.")
    else:
        print("Mission failed! The spaceship was stranded in space.")

    for line in space:
        print(" ".join(line))

def accommodate(*groups, **rooms):
    from collections import deque
    groups_of_guests = deque(groups)
    unaccommodated = []


    hotel = {}
    while groups_of_guests:
        current_guests = groups_of_guests.popleft()
        booking_successfully = False

        room_number_booked = float("-inf")
        for room, capacity in sorted(rooms.items(), key=lambda x: (x[1], int(x[0].split("_")[1]))):
            if capacity >= current_guests:
                number = int(room.split("_")[1])

                hotel[number] = current_guests
                room_number_booked = room
                booking_successfully = True
                break #breaking for

        if booking_successfully:
            del rooms[room_number_booked]
        else:
            unaccommodated.append(current_guests)

    rooms = dict([(item, value) for item, value in rooms.items() if value != 0])

    result = ''

    if hotel:
        result = f"A total of {len(hotel.keys())} accommodations were completed!\n"
        for hotel_room, guest_in_room in sorted(hotel.items(), key= lambda x: x[0]):
           result += f"<Room {hotel_room} accommodates {guest_in_room} guests>\n"
    else:
        result +="No accommodations were completed!\n"

    if unaccommodated:
        result += f"Guests with no accommodation: {sum(unaccommodated)}\n"
    if rooms:
        result += f"Empty rooms: {len(rooms.keys())}\n"

    return result.strip()


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print("\n")
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print("\n")
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))


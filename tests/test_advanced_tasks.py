import unittest
import advanced_tasks as tasks
from unittest.mock import patch
import io
from contextlib import redirect_stdout
import time


class AdvancedTasksTest(unittest.TestCase):
    def test_reverse_string_with_python_phrase(self):
        result = tasks.reverse_string("I Love Python")
        self.assertEqual(result, "nohtyP evoL I")

    def test_reverse_string_with_stacks_phrase(self):
        result = tasks.reverse_string("Stacks and Queues")
        self.assertEqual(result, "seueuQ dna skcatS")

    def test_reverse_string_empty(self):
        result = tasks.reverse_string("")
        self.assertEqual(result, "")

    def test_matching_parentheses_with_long_expression(self):
        result = tasks.matching_parentheses("1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5")
        self.assertEqual(result, ["(2 + 3)", "(3 + 1)", "(2 - (2 + 3) * 4 / (3 + 1))"])

    def test_matching_parentheses_with_Part_long_expression(self):
        result = tasks.matching_parentheses("(2 + 3) * 4 / (3 + 1)) * 5")
        self.assertEqual(result, ["(2 + 3)", "(3 + 1)"])

    def test_matching_parentheses_with_short_expression(self):
        result = tasks.matching_parentheses("(2 + 3) - (2 + 3)")
        self.assertEqual(result, ["(2 + 3)", "(2 + 3)"])

    def test_matching_parentheses_empty(self):
        result = tasks.matching_parentheses("")
        self.assertEqual(result, [])

    def test_matching_parentheses_extra_closing(self):
        result = tasks.matching_parentheses("1 + (2 + 3) )")
        self.assertEqual(result, ["(2 + 3)"])

    def test_matching_parentheses_extra_opening(self):
        result = tasks.matching_parentheses("( (2 + 3)")
        self.assertEqual(result, ["(2 + 3)"])

    def test_matching_parentheses_only_opening(self):
        result = tasks.matching_parentheses("(((")
        self.assertEqual(result, [])

    def test_matching_parentheses_only_closing(self):
        result = tasks.matching_parentheses(")))")
        self.assertEqual(result, [])

    @patch('builtins.input', side_effect=[
        'George', 'Peter', 'William', 'Paid',
        'Michael', 'Oscar', 'Olivia', 'Linda', 'End'
    ])
    def test_supermarket_queue_with_prints(self, mock_input):
        captured_output = io.StringIO()

        # Перенаправляем весь вывод (print) в нашу ловушку
        with redirect_stdout(captured_output):
            tasks.supermarket()

        # Забираем всё, что функция "напечатала" в виде одной большой строки
        printed_text = captured_output.getvalue().strip()

        # Проверяем, совпадает ли текст с тем, что ожидается в примере
        expected_text = "George\nPeter\nWilliam\n4 people remaining."
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        'Anna', 'Emma', 'Alexander', 'End'
    ])
    def test_supermarket_queue_second_example(self, mock_input):
        # Создаем новую чистую ловушку для второго теста
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.supermarket()

        printed_text = captured_output.getvalue().strip()
        expected_text = "3 people remaining."
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['End'
                                          ])
    def test_supermarket_queue_Empty_example(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.supermarket()

        printed_text = captured_output.getvalue().strip()
        expected_text = "0 people remaining."
        self.assertEqual(printed_text, expected_text)

    def generate_huge_input():
        my_inputs = [f"Client_{i}" for i in range(1, 20001)]
        my_inputs[19994] = "Paid"
        my_inputs.append("End")
        return my_inputs

    @patch('builtins.input', side_effect=generate_huge_input())
    def test_supermarket_1000queue_example(self, mock_input):
        captured_output = io.StringIO()
        start_time = time.perf_counter()

        with redirect_stdout(captured_output):
            tasks.supermarket_deque()  # Вызываем твою функцию
        end_time = time.perf_counter()

        printed_text = captured_output.getvalue().strip()

        # print("\nТЕСТ supermarket_deque НА 20000")
        execution_time = end_time - start_time

        # print(f"\n⏱ Время выполнения: {execution_time:.5f} секунд")

    @patch('builtins.input', side_effect=generate_huge_input())
    def test_supermarketPOP_1000queue_example(self, mock_input):
        captured_output = io.StringIO()
        start_time = time.perf_counter()

        with redirect_stdout(captured_output):
            tasks.supermarket_list_pop()
        end_time = time.perf_counter()

        printed_text = captured_output.getvalue().strip()

        # print("\nТЕСТ supermarket_pop НА 20000 ")
        execution_time = end_time - start_time

    # print(f"\n⏱ Время выполнения: {execution_time:.5f} секунд")

    @patch('builtins.input', side_effect=[
        '2', 'Peter', 'Amy', 'Start', '2', 'refill 1', '1', 'End'
    ])
    def test_water_dispenser_example(self, mock_input):
        # Создаем новую чистую ловушку для второго теста
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.water_dispenser()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Peter got water\nAmy got water\n0 liters left"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '10', 'Peter', 'George', 'Amy', 'Alice', 'Start', '2', '3', '3', '3', 'End'
    ])
    def test_water_dispenser_PeterGeorgeAmy_wait_Alice_2litres(self, mock_input):
        # Создаем новую чистую ловушку для второго теста
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.water_dispenser()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Peter got water\nGeorge got water\nAmy got water\nAlice must wait\n2 liters left"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        'Tracy Emily Daniel', '2'])
    def test_hot_potato(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.hot_potato()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Removed Emily\nRemoved Tracy\nLast is Daniel"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        'George Peter Michael William Thomas', '10'])
    def test_hot_potato10(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.hot_potato()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Removed Thomas\nRemoved Peter\nRemoved Michael\nRemoved George\nLast is William"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        'George Peter Michael William Thomas', '1'])
    def test_hot_potato1(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.hot_potato()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Removed George\nRemoved Peter\nRemoved Michael\nRemoved William\nLast is Thomas"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '1 2 3 4 5'])
    def test_reverse_numbers12345_54321(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.reverse_numbers()

        printed_text = captured_output.getvalue().strip()
        expected_text = "5 4 3 2 1"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '1'])
    def test_reverse_numbers1_1(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.reverse_numbers()

        printed_text = captured_output.getvalue().strip()
        expected_text = "1"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        ''])
    def test_reverse_numbers_empty(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.reverse_numbers()

        printed_text = captured_output.getvalue().strip()
        expected_text = ""
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '9', '1 97', '2', '1 20', '2', '1 26', '1 20', '3', '1 91', '4'])
    def test_stacked_queries_example(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.stacked_queries()

        printed_text = captured_output.getvalue().strip()
        expected_text = "26\n20\n91, 20, 26"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '10', '2', '1 47', '1 66', '1 32', '4', '3', '1 25', '1 16', '1 8', '4'])
    def test_stacked_queries_example2(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.stacked_queries()

        printed_text = captured_output.getvalue().strip()
        expected_text = "32\n66\n8\n8, 16, 25, 32, 66, 47"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '1', '2'])
    def test_stacked_queries_delete_from_empty(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.stacked_queries()

        printed_text = captured_output.getvalue().strip()
        expected_text = ""
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '1', '3'])
    def test_stacked_queries_max_from_empty(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.stacked_queries()

        printed_text = captured_output.getvalue().strip()
        expected_text = ""
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '1', '4'])
    def test_stacked_queries_min_from_empty(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.stacked_queries()

        printed_text = captured_output.getvalue().strip()
        expected_text = ""
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '348', '20 54 30 16 7 9'])
    def test_fast_food_with_Orders_complete(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.fast_food()

        printed_text = captured_output.getvalue().strip()
        expected_text = "54\nOrders complete"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '499', '57 45 62 70 33 90 88 76 100 50'])
    def test_fast_food_with_orders_left(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.fast_food()

        printed_text = captured_output.getvalue().strip()
        expected_text = "100\nOrders left: 76 100 50"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '0', '57 45 62 70 33 90 88 76 100 50'])
    def test_fast_food_with_zero_start(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.fast_food()

        printed_text = captured_output.getvalue().strip()
        expected_text = "100\nOrders left: 57 45 62 70 33 90 88 76 100 50"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '500', ''])
    def test_fast_food_with_zero_purchises(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.fast_food()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Orders complete"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '3', '1 5', '3 4', '10 3'])
    def test_truck_tour_example_2(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.truck_tour()

        printed_text = captured_output.getvalue().strip()
        expected_text = "2"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '3', '1 5', '10 3', '3 4'])
    def test_truck_tour_example_1(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.truck_tour()

        printed_text = captured_output.getvalue().strip()
        expected_text = "1"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '5', '22 5', '14 10', '52 7', '21 12', '36 9'])
    def test_truck_tour_example_0(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.truck_tour()

        printed_text = captured_output.getvalue().strip()
        expected_text = "0"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '{{[[(())]]}}'])
    def test_balanced_parentheses_YES(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.balanced_parentheses()

        printed_text = captured_output.getvalue().strip()
        expected_text = "YES"
        self.assertEqual(printed_text, expected_text)


    @patch('builtins.input', side_effect=[
        '{[()]}'])
    def test_balanced_parentheses_YES2(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.balanced_parentheses()

        printed_text = captured_output.getvalue().strip()
        expected_text = "YES"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '{[(])}'])
    def test_balanced_parentheses_NO(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.balanced_parentheses()

        printed_text = captured_output.getvalue().strip()
        expected_text = "NO"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '{['])
    def test_balanced_parentheses_2_open(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.balanced_parentheses()

        printed_text = captured_output.getvalue().strip()
        expected_text = "NO"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        ')'])
    def test_balanced_parentheses_1_close(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.balanced_parentheses()

        printed_text = captured_output.getvalue().strip()
        expected_text = "NO"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '(){}[]'])
    def test_balanced_parentheses_3_balanced(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.balanced_parentheses()

        printed_text = captured_output.getvalue().strip()
        expected_text = "YES"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '50', '2', '11 10 5 11 10 20', '15 13 16', '1500'])
    def test_key_revolver_test1(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.key_revolver()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Ping!\nBang!\nReloading!\nBang!\nBang!\nReloading!\n2 bullets left. Earned $1300"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '20', '6', '14 13 12 11 10 5', '13 3 11 10', '800'])
    def test_key_revolver_test2(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.key_revolver()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Bang!\nPing!\nPing!\nPing!\nPing!\nPing!\nCouldn't get through. Locks left: 3"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '33', '1', '12 11 10', '10 20 30', '100'])
    def test_key_revolver_test3(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.key_revolver()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Bang!\nReloading!\nBang!\nReloading!\nBang!\n0 bullets left. Earned $1"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '10','5', 'Mercedes' , 'green', 'Mercedes', 'BMW', 'Skoda' ,'green', 'END'])
    def test_crossroads_test_1(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.crossroads()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Everyone is safe.\n3 total cars passed the crossroads."
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '9','3', 'Mercedes', 'Hummer' , 'green', 'Hummer', 'Mercedes', 'green', 'END'])
    def test_crossroads_test_2(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.crossroads()

        printed_text = captured_output.getvalue().strip()
        expected_text = "A crash happened!\nHummer was hit at e."
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '10','5', 'Volkswagen', 'BMW','green', 'END'])
    def test_crossroads_test_3(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.crossroads()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Everyone is safe.\n1 total cars passed the crossroads."
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['4 2 10 5', '3 15 15 11 6'])
    def test_cups_and_bottles_bottles_win(self, mock_input):

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.cups_and_bottles()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Bottles: 3\nWasted litters of water: 26"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['10 20 30', '5 5'])
    def test_cups_and_bottles_cups_win(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.cups_and_bottles()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Cups: 20 30\nWasted litters of water: 0"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['5 6 4', '3 4 5 1 2'])
    def test_cups_and_bottles_partial_fill(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.cups_and_bottles()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Cups: 4\nWasted litters of water: 4"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'])
    def test_count_same_values(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.count_same_values()

        printed_text = captured_output.getvalue().strip()
        expected_text = "-2.5 - 3 times\n4.0 - 2 times\n3.0 - 4 times\n-5.5 - 1 times"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3'])
    def test_count_same_values2(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.count_same_values()

        printed_text = captured_output.getvalue().strip()
        expected_text = "2.0 - 3 times\n4.0 - 6 times\n5.0 - 4 times\n3.0 - 7 times"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['7', 'Peter 5.20','Mark 5.50', 'Peter 3.20', 'Mark 2.50', 'Alex 2.00', 'Mark 3.46', 'Alex 3.00'])
    def test_students_grades_3_people_7_lines(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.students_grades()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Peter -> 5.20 3.20 (avg: 4.20)\nMark -> 5.50 2.50 3.46 (avg: 3.82)\nAlex -> 2.00 3.00 (avg: 2.50)"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['4', 'Scott 4.50','Ted 3.00', 'Scott 5.00', 'Ted 3.66'])
    def test_students_grades_2people(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.students_grades()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Scott -> 4.50 5.00 (avg: 4.75)\nTed -> 3.00 3.66 (avg: 3.33)"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['5', 'Lee 6.00','Lee 5.50', 'Lee 6.00', 'Peter 4.40', 'Kenny 3.30'])
    def test_students_grades_3_people_5_lines(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.students_grades()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Lee -> 6.00 5.50 6.00 (avg: 5.83)\nPeter -> 4.40 (avg: 4.40)\nKenny -> 3.30 (avg: 3.30)"
        self.assertEqual(printed_text, expected_text)

    raw_input_parking_lot = """4
    IN, CA2844AA
    IN, CA1234TA
    OUT, CA2844AA
    OUT, CA1234TA"""

    @patch('builtins.input', side_effect=raw_input_parking_lot.split('\n'))
    def test_parking_lot(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.parking_lot()
        actual_output = set(captured_output.getvalue().strip().split('\n'))

        expected_output_raw = """Parking Lot is Empty"""
        expected_output = set(expected_output_raw.strip().split('\n'))

        missing_cars = expected_output - actual_output
        self.assertFalse(missing_cars, f"Ошибка! Потеряны машины: {missing_cars}")


        extra_cars = actual_output - expected_output
        self.assertFalse(extra_cars, f"Ошибка! Лишние машины на парковке: {extra_cars}")

    raw_input_parking_lot_4_results = """10
    IN, CA2844AA
    IN, CA1234TA
    OUT, CA2844AA
    IN, CA9999TT
    IN, CA2866HI
    OUT, CA1234TA
    IN, CA2844AA
    OUT, CA2866HI
    IN, CA9876HH
    IN, CA2822UU"""

    cleaned_input = [line.strip() for line in raw_input_parking_lot_4_results.split('\n') if line.strip()]

    # 2. Передаем этот чистый список в side_effect
    @patch('builtins.input', side_effect=cleaned_input)
    def test_parking_lot_4_results(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.parking_lot()

        raw_output = captured_output.getvalue().strip().split('\n')
        actual_output_4results = set(line.strip() for line in raw_output if line.strip())

        expected_output_raw = """CA2844AA
        CA9999TT
        CA2822UU
        CA9876HH"""
        expected_output_4_results = set(el.strip() for el in expected_output_raw.strip().split('\n'))

        missing_cars = expected_output_4_results - actual_output_4results
        self.assertFalse(missing_cars, f"Ошибка! Потеряны машины: {missing_cars}")

        extra_cars = actual_output_4results - expected_output_4_results
        self.assertFalse(extra_cars, f"Ошибка! Лишние машины на парковке: {extra_cars}")

    @patch('builtins.input', side_effect=['6', 'George', 'George', 'George', 'Peter', 'George', 'NiceGuy1234'])
    def test_unique_usernames(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.unique_usernames()

        printed_text = set((captured_output.getvalue().strip()).split('\n'))
        expected_text = {"Peter","NiceGuy1234","George"}
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['10', 'Peter', 'Maria', 'Peter', 'George', 'Steve', 'Maria', 'Alex', 'Peter', 'Steve','George'])
    def test_unique_usernames_5(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.unique_usernames()

        printed_text = set((captured_output.getvalue().strip()).split('\n'))
        expected_text = {'Peter', 'Maria', 'George', 'Steve', 'Alex' }
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['4 3', '1', '3', '5', '7', '3', '4', '5'])
    def test_sets_of_elements(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.sets_of_elements()

        printed_text = set((captured_output.getvalue().strip()).split('\n'))
        expected_text = {'3', '5' }
        self.assertEqual(printed_text, expected_text)


    @patch('builtins.input', side_effect=['2 2', '1', '3', '1', '5' ])
    def test_sets_of_elements_1(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.sets_of_elements()

        printed_text = set((captured_output.getvalue().strip()).split('\n'))
        expected_text = {'1' }
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['4', 'Ce O', 'Mo O Ce' , 'Ee', 'Mo' ])
    def test_periodic_table4_4(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.periodic_table()

        printed_text = set((captured_output.getvalue().strip()).split('\n'))
        expected_text = {'Ce', 'Ee' , 'Mo', 'O' }
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['3', 'Ge Ch O Ne', 'Nb Mo Tc', 'O Ne'])
    def test_periodic_table3_7(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.periodic_table()

        printed_text = set((captured_output.getvalue().strip()).split('\n'))
        expected_text = {'Ch','Ge','Mo','Nb','Ne','O','Tc'}
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['SoftUni rocks'])
    def test_count_symbols_softuni_rocks(self, mock_input):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            tasks.count_symbols()
        printed_text = set(line for line in captured_output.getvalue().split('\n') if line)
        expected_text = {' : 1 time/s','S: 1 time/s','U: 1 time/s','c: 1 time/s','f: 1 time/s','i: 1 time/s','k: 1 time/s','n: 1 time/s','o: 2 time/s','r: 1 time/s','s: 1 time/s','t: 1 time/s'}
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['3', '0,3-1,2' , '2,10-3,5', '6,15-3,10'])
    def test_longest_intersection_length_5(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.longest_intersection()

        printed_text = captured_output.getvalue().strip()
        expected_text = 'Longest intersection is [6, 7, 8, 9, 10] with length 5'
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['5', '0,10-2,5', '3,8-1,7', '1,8-2,4', '4,7-2,5', '1,10-2,11'])
    def test_longest_intersection_length_9(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.longest_intersection()

        printed_text = captured_output.getvalue().strip()
        expected_text = 'Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9'
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['4','Pesho','Stefan','Stamat', 'Gosho'])
    def test_battle_of_names_4_results(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.battle_of_names()

        printed_text = captured_output.getvalue().strip()
        expected_text = '304, 128, 206, 511'
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['6','Preslav', 'Gosho','Ivan','Stamat','Pesho','Stefan'])
    def test_battle_of_names_2_results(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.battle_of_names()

        printed_text = captured_output.getvalue().strip()
        expected_text = '733, 101'
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['4 2 10 5', '3 15 15 11 6'])
    def test_cups_and_bottles_bottles_win1(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.cups_and_bottles()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Bottles: 3\nWasted litters of water: 26"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['10 20 30', '5 5'])
    def test_cups_and_bottles_cups_win2(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.cups_and_bottles()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Cups: 20 30\nWasted litters of water: 0"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=['1 2 3', '10 20 30 40 50'])
    def test_cups_and_bottles_multiple_bottles_left(self, mock_input):

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.cups_and_bottles()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Bottles: 10 20\nWasted litters of water: 114"
        self.assertEqual(printed_text, expected_text)


if __name__ == '__main__':
    unittest.main()

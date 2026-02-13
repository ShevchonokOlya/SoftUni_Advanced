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
        self.assertEqual(result, ["(2 + 3)" ,"(2 + 3)"] )

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

    @patch('builtins.input', side_effect=[ 'End'
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

        #print(f"\n⏱ Время выполнения: {execution_time:.5f} секунд")

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
        '2', 'Peter', 'Amy','Start', '2','refill 1','1', 'End'
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
        '10', 'Peter', 'George', 'Amy', 'Alice','Start', '2','3','3','3','End'
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
        'Tracy Emily Daniel','2'])
    def test_hot_potato(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.hot_potato()

        printed_text = captured_output.getvalue().strip()
        expected_text = "Removed Emily\nRemoved Tracy\nLast is Daniel"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        'George Peter Michael William Thomas','10'])
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
        '9', '1 97', '2', '1 20' , '2', '1 26', '1 20', '3', '1 91', '4' ])
    def test_stacked_queries_example(self, mock_input):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tasks.stacked_queries()

        printed_text = captured_output.getvalue().strip()
        expected_text = "26\n20\n91, 20, 26"
        self.assertEqual(printed_text, expected_text)

    @patch('builtins.input', side_effect=[
        '10', '2', '1 47', '1 66' , '1 32', '4', '3', '1 25', '1 16','1 8', '4' ])
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
if __name__ == '__main__':
    unittest.main()
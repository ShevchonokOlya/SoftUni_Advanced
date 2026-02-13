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

        print("\nТЕСТ supermarket_deque НА 20000")
        execution_time = end_time - start_time

        print(f"\n⏱ Время выполнения: {execution_time:.5f} секунд")

    @patch('builtins.input', side_effect=generate_huge_input())
    def test_supermarketPOP_1000queue_example(self, mock_input):
        captured_output = io.StringIO()
        start_time = time.perf_counter()

        with redirect_stdout(captured_output):
            tasks.supermarket_pop()
        end_time = time.perf_counter()

        printed_text = captured_output.getvalue().strip()

        print("\nТЕСТ supermarket_pop НА 20000 ")
        execution_time = end_time - start_time

        print(f"\n⏱ Время выполнения: {execution_time:.5f} секунд")

if __name__ == '__main__':
    unittest.main()
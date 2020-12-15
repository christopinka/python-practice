from unittest import TestCase
from fb import fizz_buzz


class Test(TestCase):
    def test_should_print_from_one_to_fifty(self):
        self.assertEqual(len(fizz_buzz()), len(range(1, 51)))
        self.assertEqual(list(fizz_buzz().keys())[0], list(range(1, 51))[0])
        self.assertEqual(list(fizz_buzz().keys())[49], list(range(1, 51))[49])

    def test_should_print_fizz_when_factor_of_three(self):
        self.assertEqual(fizz_buzz()[3], "Fizz")
        self.assertEqual(fizz_buzz()[48], "Fizz")
        self.assertEqual(sum(x == "Fizz" for x in fizz_buzz().values()), 13)

    def test_should_print_buzz_when_factor_of_five(self):
        self.assertEqual("Buzz", fizz_buzz()[5])
        self.assertEqual("Buzz", fizz_buzz()[50])
        self.assertEqual(7, sum(x == "Buzz" for x in fizz_buzz().values()))

    def test_should_print_fizzbuzz_when_factor_of_five_and_factor_of_three(self):
        self.assertEqual("FizzBuzz", fizz_buzz()[15])
        self.assertEqual("FizzBuzz", fizz_buzz()[45])
        self.assertEqual(3, sum(x == "FizzBuzz" for x in fizz_buzz().values()))

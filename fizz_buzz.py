"""
Module to solve FizzBuzzChallenge
"""


def num_in_range(num: int) -> bool:
    """
    :param num: integer to be checke  (if in range)
    :return True if number in converted (int) number, 1 <= n < m < 10000, else False
    """
    return True if num in range(1, 10001) else False


def get_num() -> int:
    """
    Check if number is valid for int conversion and in range, if is - convert and return
    :return: integer number
    """
    number = None
    while number is None:
        try:
            number = int(input('Type a number\n'))
            while not num_in_range(number):
                number = int(input('Type a number\n'))
        except ValueError:
            print('Not valid integer number')
    return number


def generate_fizz_buzz():
    """print strings according to specification"""
    number_start = get_num()
    number_end = get_num()
    # print(number_start, number_end)
    # add 1 (inclusive range)
    for number in range(number_start, number_end + 1):
        if number % 5 == 0 and number % 3 == 0:
            print('FizzBuzz')
        elif number % 5 == 0:
            print('Buzz')
        elif number % 3 == 0:
            print('Fizz')
        else:
            print(number)


def main():
    """Handle entire module"""
    generate_fizz_buzz()


if __name__ == "__main__":
    main()

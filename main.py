#!/usr/bin/python3

MIN_NUMBER_FOR_SENTENCE_IN_SEQUENCE = 0  # presupposition of task
MAX_NUMBER_FOR_SENTENCE_IN_SEQUENCE = 1_000_000_000  # presupposition of task


class SheypoorInterviewTaskSequence:
    """
    Consider the following infinite sequence:
        0, 1, 1, 2, 3, 5, 8, 13, 12, 7, 10, 8, 9, ...
      The 0th element is 0 and the 1st element is 1. Each of the next elements is equal to the sum of the digits
      of the previous two elements.
    """

    msg_for_non_integer_negative_inputs = "Input to this sequence must be a non-negative integer"
    msg_for_out_of_bound = (
        f"Input to this sequence must be in range of {MIN_NUMBER_FOR_SENTENCE_IN_SEQUENCE} "
        f"to {MAX_NUMBER_FOR_SENTENCE_IN_SEQUENCE}"
    )

    @classmethod
    def sum_digits(cls, value: int) -> int:
        sum = 0
        while value > 9:
            sum += value % 10
            value //= 10
        return sum + value

    @classmethod
    def find_nth_sentence(cls, n: int) -> int:
        try:
            if (not isinstance(n, int)) or (n < 0):
                raise IOError({"message": cls.msg_for_non_integer_negative_inputs})
            if n > MAX_NUMBER_FOR_SENTENCE_IN_SEQUENCE:
                raise IOError({"message": cls.msg_for_out_of_bound})
            a0 = 0
            a1 = 1
            for i in range(n):
                next = cls.sum_digits(a0) + cls.sum_digits(a1)
                a0 = a1
                a1 = next
            return a0

        except IOError as exception:
            details = exception.args[0]
            return details["message"]


def main():
    try:
        n = int(input("Enter a number between 0 and 1000000: "))
        print("In running with docker, the n argument is 10 by default.")
    except EOFError:
        n = 10  # The last example of the task
    print(f"The value of sentence you're looking for is: {SheypoorInterviewTaskSequence.find_nth_sentence(n)}")


if __name__ == "__main__":
    main()

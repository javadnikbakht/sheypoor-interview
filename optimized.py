#!/usr/bin/python3

MIN_NUMBER_FOR_SENTENCE_IN_SEQUENCE = 0
MAX_NUMBER_FOR_SENTENCE_IN_SEQUENCE = 1_000_000_000


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

    def __init__(self):
        self.memo = {0: 0, 1: 1}

    @staticmethod
    def sum_digits(value: int) -> int:
        digit_sum = 0
        while value > 9:
            digit_sum += value % 10
            value //= 10
        return digit_sum + value

    def find_nth_sentence(self, n: int) -> int:
        """
        Finds the nth sentence in the sequence.

        Args:
            n: The index of the sentence to find.

        Returns:
            The nth sentence in the sequence.

        Raises:
            ValueError: If n is not a non-negative integer or is out of bounds.
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError(self.msg_for_non_integer_negative_inputs)
        if n > MAX_NUMBER_FOR_SENTENCE_IN_SEQUENCE:
            raise ValueError(self.msg_for_out_of_bound)

        if n in self.memo:
            return self.memo[n]

        a0 = self.find_nth_sentence(n - 2)
        a1 = self.find_nth_sentence(n - 1)
        next_value = SheypoorInterviewTaskSequence.sum_digits(a0) + SheypoorInterviewTaskSequence.sum_digits(a1)
        self.memo[n] = next_value

        return next_value


def main():
    seq = SheypoorInterviewTaskSequence()
    n = int(
        input(
            f"Enter the number of sentence you're looking for (between {MIN_NUMBER_FOR_SENTENCE_IN_SEQUENCE} and "
            f"{MAX_NUMBER_FOR_SENTENCE_IN_SEQUENCE}): "
        )
    )
    print(f"The value of sentence you're looking for is: {seq.find_nth_sentence(n)}")


if __name__ == "__main__":
    main()

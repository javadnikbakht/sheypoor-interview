import unittest

from main import MAX_NUMBER_FOR_SENTENCE_IN_SEQUENCE
from main import SheypoorInterviewTaskSequence


class RequestedSentencesTestCase(unittest.TestCase):
    def test_second_sentence_of_sequence(self):
        n = 2
        print(f"\nTest The {n}nd sentence of sequence")
        desired_result = 1
        self.assertEqual(SheypoorInterviewTaskSequence.find_nth_sentence(n), desired_result)

    def test_sixth_sentence_of_sequence(self):
        n = 6
        print(f"\nTest The {n}th sentence of sequence")
        desired_result = 8
        self.assertEqual(SheypoorInterviewTaskSequence.find_nth_sentence(n), desired_result)

    def test_tenth_sentence_of_sequence(self):
        n = 10
        print(f"\nTest The {n}th sentence of sequence")
        desired_result = 10
        self.assertEqual(SheypoorInterviewTaskSequence.find_nth_sentence(n), desired_result)


class BadInputsTestCase(unittest.TestCase):
    def test_a_float_number_as_input(self):
        n = 2.5
        desired_msg = SheypoorInterviewTaskSequence.msg_for_non_integer_negative_inputs
        print("\nTest for a non-integer(float) number as number of sentence in the sequence")
        self.assertEqual(SheypoorInterviewTaskSequence.find_nth_sentence(n), desired_msg)

    def test_a_string_as_input(self):
        n = "lurem ipsum"
        desired_msg = SheypoorInterviewTaskSequence.msg_for_non_integer_negative_inputs
        print("\nTest for a non-integer(string) input as number of sentence in the sequence")
        self.assertEqual(SheypoorInterviewTaskSequence.find_nth_sentence(n), desired_msg)

    def test_a_negative_number_as_input(self):
        n = -4
        desired_msg = SheypoorInterviewTaskSequence.msg_for_non_integer_negative_inputs
        print("\nTest for a negative number as number of sentence in the sequence")
        self.assertEqual(SheypoorInterviewTaskSequence.find_nth_sentence(n), desired_msg)

    def test_an_out_of_bound_number_as_input(self):
        n = MAX_NUMBER_FOR_SENTENCE_IN_SEQUENCE + 1
        desired_msg = SheypoorInterviewTaskSequence.msg_for_out_of_bound
        print("\nTest for a negative number as number of sentence in the sequence")
        self.assertEqual(SheypoorInterviewTaskSequence.find_nth_sentence(n), desired_msg)


if __name__ == "__main__":
    unittest.main()

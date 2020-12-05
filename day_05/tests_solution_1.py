import unittest

from day_05.solution_1 import compute_seven_first_char, compute_last_three_char, compute_seat_id


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sequence_seven_first_char = 'FBFBBFF'
        self.sequence_three_last_char = 'RLR'

    def test_compute_seven_first_char_should_return_44(self):
        self.assertEqual(compute_seven_first_char(self.sequence_seven_first_char), 44)

    def test_compute_last_three_char_should_return_5(self):
        self.assertEqual(compute_last_three_char(self.sequence_three_last_char), 5)

    def test_compute_seat_id_should_return_567(self):
        seat_id = 567
        sequence = 'BFFFBBF'
        sequence2 = 'RRR'

        self.assertEqual(compute_seat_id(sequence, sequence2), seat_id)

    def test_compute_seat_id_should_return_119(self):
        seat_id = 119
        sequence = 'FFFBBBF'
        sequence2 = 'RRR'

        self.assertEqual(compute_seat_id(sequence, sequence2), seat_id)

    def test_compute_seat_id_should_return_820(self):
        seat_id = 820
        sequence = 'BBFFBBF'
        sequence2 = 'RLL'

        self.assertEqual(compute_seat_id(sequence, sequence2), seat_id)

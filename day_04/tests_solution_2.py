import unittest

from day_04.solution_2 import verify_byr, verify_iyr, verify_eyr, verify_hgt, verify_hcl, verify_ecl, verify_pid


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_given_document = {'pid': '000000001', 'hgt': '60in', 'ecl': 'brn', 'iyr': '2012', 'eyr': '2030',
                                     'byr': '2002', 'hcl': '#123abc'}
        self.invalid_given_document = {'pid': '0123456789 ', 'hgt': '59cm', 'ecl': 'wat', 'iyr': '2023', 'eyr': '2038',
                                       'byr': '2003', 'hcl': '123abc'}

    def test_verify_byr_should_return_true(self):
        self.assertTrue(verify_byr(self.valid_given_document))

    def test_verify_byr_should_return_false(self):
        self.assertFalse(verify_byr(self.invalid_given_document))

    def test_verify_iyr_return_true(self):
        self.assertTrue(verify_iyr(self.valid_given_document))

    def test_verify_iyr_return_false(self):
        self.assertFalse(verify_iyr(self.invalid_given_document))

    def test_verify_eyr_should_return_true(self):
        self.assertTrue(verify_eyr(self.valid_given_document))

    def test_verify_eyr_should_return_false(self):
        self.assertFalse(verify_eyr(self.invalid_given_document))

    def test_verify_hgt_should_return_true(self):
        self.assertTrue(verify_hgt(self.valid_given_document))

    def test_verify_hgt_should_return_false(self):
        self.assertFalse(verify_hgt(self.invalid_given_document))

    def test_verify_hcl_should_return_true(self):
        self.assertTrue(verify_hcl(self.valid_given_document))

    def test_verify_hcl_should_return_false(self):
        self.assertFalse(verify_hcl(self.invalid_given_document))

    def test_verify_ecl_should_return_true(self):
        self.assertTrue(verify_ecl(self.valid_given_document))

    def test_verify_ecl_should_return_false(self):
        self.assertFalse(verify_ecl(self.invalid_given_document))

    def test_verify_pid_should_return_true(self):
        self.assertTrue(verify_pid(self.valid_given_document))

    def test_verify_pid_should_return_false(self):
        self.assertFalse(verify_pid(self.invalid_given_document))

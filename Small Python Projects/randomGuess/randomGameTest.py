import unittest
import randomGame


class TestGame(unittest.TestCase):
    def test_input(self):
        # run_guess(guess, answer)
        result = randomGame.run_guess(6, 6)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        # run_guess(guess, answer)
        result = randomGame.run_guess(3, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        # run_guess(guess, answer)
        result = randomGame.run_guess(15, 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

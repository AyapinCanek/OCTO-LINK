import unittest
from src.convivencia import Situation, choose_action


class ConsentTests(unittest.TestCase):
    def test_explicit_request_and_consent(self):
        self.assertEqual(choose_action(Situation(True, True)).action, "ofrecer_ayuda")

    def test_rejection_respected(self):
        self.assertEqual(choose_action(Situation(True, False)).action, "respetar_distancia")

    def test_unknown_consent(self):
        self.assertEqual(choose_action(Situation(True, None)).action, "pedir_permiso")

    def test_no_request(self):
        self.assertEqual(choose_action(Situation(False, True)).action, "no_intervenir")

    def test_withdrawal_overrides_previous_consent(self):
        self.assertEqual(choose_action(Situation(True, True, True)).action, "detenerse")


if __name__ == "__main__":
    unittest.main()

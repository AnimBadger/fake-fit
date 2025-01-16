import unittest
from scripts.generators.id_generator import generate_id

class TestGenerateId(unittest.TestCase):

    def test_generate_id_length(self):
        generated_id = generate_id()
        self.assertEqual(len(generated_id), 12)

    def test_generate_id_is_string(self):
        generated_id = generate_id()
        self.assertTrue(isinstance(generated_id, str))

    def test_generate_id_is_unique(self):
        generated_ids = {generate_id() for _ in range(1000)}
        self.assertEqual(len(generated_ids), 1000)

if __name__ == "__main__":
    unittest.main()
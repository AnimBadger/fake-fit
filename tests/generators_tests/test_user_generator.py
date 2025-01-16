import unittest
from scripts.generators.user_generator import generate_users

class TestGenerateUsers(unittest.TestCase):

    def test_generate_users_length(self):
        num_users = 5
        users = generate_users(num_users)
        self.assertEqual(len(users), num_users)

    def test_generate_users_structure(self):
        num_users = 3
        users = generate_users(num_users)
        for user in users:
            self.assertIn('user_id', user)
            self.assertIn('name', user)
            self.assertIn('email', user)
            self.assertIn('age', user)
            self.assertIn('phone', user)
            self.assertIn('address', user)
            self.assertIn('weight', user)
            self.assertIn('height', user)
            self.assertIn('bmi', user)
            self.assertIn('weight_goal', user)
            self.assertIn('fitness_level', user)
            self.assertIn('membership_status', user)

    def test_generate_users_content(self):
        num_users = 2
        users = generate_users(num_users)
        for user in users:
            self.assertTrue(isinstance(user['user_id'], str))
            self.assertTrue(isinstance(user['name'], str))
            self.assertTrue(isinstance(user['email'], str))
            self.assertTrue(isinstance(user['age'], int))
            self.assertTrue(isinstance(user['phone'], str))
            self.assertTrue(isinstance(user['address'], str))
            self.assertTrue(isinstance(user['weight'], int))
            self.assertTrue(isinstance(user['height'], int))
            self.assertTrue(isinstance(user['bmi'], float))
            self.assertTrue(isinstance(user['weight_goal'], int))
            self.assertTrue(user['fitness_level'] in ['beginner', 'intermediate', 'advanced', 'athlete'])
            self.assertTrue(user['membership_status'] in ['active', 'inactive'])

if __name__ == "__main__":
    unittest.main()
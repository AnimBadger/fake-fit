import uuid 
import random
from faker import Faker

faker = Faker()

def generate_id():
    return str(uuid.uuid4())

def generate_users(count=10):
    users = []
    for _ in range(count):
        user_id = generate_id()
        weight = random.randint(40, 400)
        height = random.randint(75, 200)
        bmi = weight / (height / 100) ** 2
        users.append({
            'user_id': user_id,
            'name': faker.name(),
            'email': faker.email(),
            'age': random.randint(16, 60),
            'phone': faker.phone_number(),
            'address': faker.address(),
            'weight': weight,
            'height': height,
            'bmi': bmi,
            'weight_goal': random.randint(40, 400),
            'fitness_level': random.choice(['beginner', 'intermediate', 'advanced', 'athlete']),
            'membership_status': random.choice(['active', 'inactive']),
        })
        #TODO: check if member is active and add membership_start_date and membership_end_date, else add date expired
        return users

#TODO: think about this again    
def generate_workouts(users, count=10):
    workouts = []
    for _ in range(count):
        workout_id = generate_id()
        user = random.choice(users)
        workouts.append({
            'user_id': user['user_id'],
            'workout_id': workout_id,
            'name': faker.word(),
            'description': faker.sentence(),
            'duration': random.randint(10, 120),
            'calories_burned': random.randint(50, 1000),
            'intensity': random.choice(['low', 'medium', 'high']),
            'category': random.choice(['cardio', 'strength', 'flexibility', 'balance']),
            'equipment': random.choice(['dumbbells', 'kettlebells', 'resistance bands', 'bodyweight']),
        })
    return workouts


def generate_nutrition(users, count=30):
    nutrition = []

    if count <= len(users):
        selected_users = random.sample(users, count)
        for user in selected_users:
            nutrition.append({
                "user_id": user["user_id"],
                "date": faker.date_this_year(),
                "protein": random.randint(10, 200),
                'carbs': random.randint(10, 200),
                'fat': random.randint(10, 200),
                'water': random.randint(1, 10),
                "meal": random.choice(["Breakfast", "Lunch", "Dinner", "Snack"]),
                "calories": random.randint(200, 800)
            })
    else:
        for user in users:
            nutrition.append({
                "user_id": user["user_id"],
                "date": faker.date_this_year(),
                "meal": random.choice(["Breakfast", "Lunch", "Dinner", "Snack"]),
                'carbs': random.randint(10, 200),
                'fat': random.randint(10, 200),
                'water': random.randint(1, 10),
                "calories": random.randint(200, 800)
            })

        remaining_count = count - len(users)

        for _ in range(remaining_count):
            user = random.choice(users)
            nutrition.append({
                "user_id": user["user_id"],
                "date": faker.date_this_year(),
                "meal": random.choice(["Breakfast", "Lunch", "Dinner", "Snack"]),
                'carbs': random.randint(10, 200),
                'fat': random.randint(10, 200),
                'water': random.randint(1, 10),
                "calories": random.randint(200, 800)
            })

    return nutrition

def generate_progress(users, count=10):
    progress = []
    for _ in range(count):
        progress_id = generate_id()
        user = random.choice(users)
        progress.append({
            'user_id': user['user_id'],
            'progress_id': progress_id,
            'weight': random.randint(40, 400),
            'bmi': random.randint(10, 50),
            'calories_burned': random.randint(50, 1000),
            'workouts_completed': random.randint(1, 100),
            'meals_eaten': random.randint(1, 100),
            'water_drank': random.randint(1, 100),
            'date': faker.date_this_year(),
        })
    return progress

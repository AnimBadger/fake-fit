from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()

    # Load environment variables
    env_file = os.getenv('ENV_FILE', '.env')
    load_dotenv(env_file)
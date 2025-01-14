# Fitness Data API

This project generates fake fitness data for users, provides API endpoints to access this data, and includes scripts to upload the data to MongoDB daily. The data is cleared at the end of every week.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Scripts](#scripts)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AnimBadger/fake-fit.git
    cd fake-fit
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your MongoDB connection string in a `.env` file:
    ```env
    MONGODB_URI=mongodb://your_mongodb_uri
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. The API will be available at `http://localhost:5000`.

## API Endpoints


## Scripts

- `generate_data.py`: Generates fake fitness data for users and uploads it to MongoDB. This script is scheduled to run daily.
- `clear_data.py`: Clears all fitness data from MongoDB. This script is scheduled to run at the end of every week.

### Running Scripts Manually

1. Generate fake data and upload to MongoDB:
    ```sh
    python scripts/generate_data.py
    ```

2. Clear all fitness data from MongoDB:
    ```sh
    python scripts/clear_data.py
    ```

## License

This project is licensed under the MIT License. See the  file for details.
# Dentiva Care API

Welcome to the Dentiva Care API project! This guide will help you set up and run the project on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.12.3

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone url
    cd dentiva-care-fastapi
    ```

2. **Install Dependencies:**

    Install the required packages using npm:
    ```bash
    pip install -r requirements.txt
    ```

3. Configuration:

    Create a .env file in the project root and configure your environment variables. You can start by copying the .env.example file and updating the values:
    ```bash
    cp .env.example .env
    ```


5. Running the API:

    Start the development server:
    ```bash
    uvicorn main:app --reload
    ```

   The API will be accessible at http://localhost:[PORT].

   [PORT] value will depend on the environment variable you have configured in step 3. 

   ---

Remember that the API documentation is exposed at http://localhost:[PORT]/docs when it is running
# Body Forge

Body Forge is a Django-based web application designed for fitness enthusiasts. It provides a platform to create and manage workouts, track progress, and engage with a community forum.

## Features

*   **User Accounts:** Register, log in, and manage user profiles.
*   **Workout Management:**
    *   Create and customize workout routines.
    *   Define different workout types (e.g., cardio, strength training).
    *   Add exercises and group them by muscle groups.
    *   Track sets, repetitions, and weight for each exercise.
*   **Community Forum:**
    *   Ask fitness-related questions.
    *   Provide answers and engage in discussions.
    *   Moderation tools for approving and deleting questions.

## Technologies Used

*   **Backend:** Django
*   **Frontend:** HTML, CSS, JavaScript
*   **Database:** PostgreSQL
*   **Image Handling:** Pillow

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/body-forge.git
    cd body-forge
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    pip install -r requrenments.txt
    ```

3.  **Set up the PostgreSQL database:**
    *   Create a PostgreSQL database named `body_forge_db`.
    *   Update the database credentials in `body_forge/settings.py`.

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

6.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Application Structure

*   `accounts/`: Handles user authentication and profile management.
*   `common/`: Contains common views and templates, including the home page.
*   `forum/`: Manages the community forum, including questions and answers.
*   `workouts/`: Manages workout creation, tracking, and related models.
*   `static/`: Contains static assets (CSS, JavaScript, images).
*   `templates/`: Contains Django templates for rendering HTML pages.

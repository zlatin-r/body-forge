# Body Forge

![Body Forge Logo](https://via.placeholder.com/150) <!-- Replace with your actual logo URL -->

**Body Forge** is a powerful and intuitive web application built with Django, designed to help fitness enthusiasts create, track, and manage their workouts. It also features a community forum for users to connect, share knowledge, and support each other on their fitness journeys.

---

## ✨ Features

*   **👤 User Authentication & Profiles:**
    *   Secure user registration and login.
    *   Personalized user dashboards and profiles.
    *   Ability to upload and change profile pictures.

*   **🏋️ Workout Management:**
    *   Create and customize detailed workout plans.
    *   Define various workout types (e.g., Strength, Cardio, HIIT).
    *   Build a library of exercises and categorize them by muscle group.
    *   Track sets, reps, weight, and duration for each exercise.
    *   **RESTful API:** Programmatic access to workout data for integration with other services or front-end applications.

*   **💬 Community Forum:**
    *   Ask questions and get advice from the community.
    *   Answer questions and share your expertise.
    *   Engage in discussions on various fitness topics.
    *   Moderation tools to ensure a positive and supportive environment.

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-darkgreen.svg?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.15-red.svg?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![python-decouple](https://img.shields.io/badge/python--decouple-3.8-lightgrey.svg?style=for-the-badge)

---

## 🚀 Getting Started

Follow these instructions to get a local copy of Body Forge up and running on your machine.

### Prerequisites

*   [Python 3.11+](https://www.python.org/downloads/)
*   [PostgreSQL](https://www.postgresql.org/download/)
*   [Git](https://git-scm.com/downloads/)
*   [Docker](https://www.docker.com/get-started) (for deployment with Docker Compose)
*   [Nginx](https://nginx.org/en/download.html) (for serving static/media files in production-like environments)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/body-forge.git
    cd body-forge
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS and Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    Create a `.env` file in the root directory of the project with the following variables:
    ```
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost # Ensure these are configured for CSRF protection
    ```
    Replace `your_secret_key_here` with a strong, unique secret key.

5.  **Set up the database:**
    *   Log in to your PostgreSQL server.
    *   Create a new database: `CREATE DATABASE body_forge_db;`
    *   Update the `DATABASES` configuration in `body_forge/settings.py` with your PostgreSQL username, password, and port if they differ from the defaults.

6.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8.  **Access the application:**
    Open your favorite web browser and navigate to `http://127.0.0.1:8000/`.

---

## 🐳 Deployment with Docker and Nginx

For production-like environments, Body Forge can be deployed using Docker Compose with Nginx serving static and media files.

### Docker Compose Setup

The `docker-compose.yml` file defines an Nginx service that acts as a reverse proxy and serves static/media files.

1.  **Build and run the Docker containers:**
    ```bash
    docker-compose up --build -d
    ```

2.  **Static and Media Files:**
    Nginx is configured to serve static and media files directly from bind mounts.
    *   **Static Files:** Ensure you run `python manage.py collectstatic` to gather all static files into the `static_files` directory (as defined by `STATIC_ROOT` in `settings.py`). This directory is then bind-mounted into the Nginx container.
    *   **Media Files:** User-uploaded media files are expected in the `mediafiles` directory (as defined by `MEDIA_ROOT` in `settings.py`), which is also bind-mounted into the Nginx container.

3.  **Nginx Configuration:**
    The Nginx configuration is bind-mounted from `./nginx/nginx.conf`. Ensure this file is correctly configured to serve your Django application and the static/media files. A typical Nginx configuration for static and media files would include `location` blocks like:

    ```nginx
    # In your nginx.conf
    location /static/ {
        alias /usr/share/nginx/html/static_files/; # Matches STATIC_ROOT bind mount
    }

    location /media/ {
        alias /path/to/your/project/mediafiles/; # Matches MEDIA_ROOT bind mount
    }
    ```
    **Note:** Replace `/path/to/your/project/mediafiles/` with the absolute path to your `mediafiles` directory on the host machine if it's not already correctly configured in your `nginx.conf`.

---

## ⚡ Asynchronous Operations

Body Forge is designed with potential for asynchronous operations to enhance performance, particularly for I/O-bound tasks like database queries and external API calls. Views that interact heavily with the database are candidates for conversion to `async def` functions, leveraging Django's asynchronous ORM capabilities.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
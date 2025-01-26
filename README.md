markdown
# Productivity Chat App

A real-time messaging platform designed to help users efficiently manage conversations, track tasks, and integrate with productivity tools like Todoist. This app uses FastAPI, PostgreSQL, and integrates external APIs for task management and calendar functionalities.

---

## Features

- **User Authentication**: Secure login with JWT-based authentication.
- **Real-time Messaging**: Conversations between users with support for media messages (future enhancements).
- **Task Integration**: Ability to send messages to Todoist as tasks.
- **Conversation Management**: Manage conversations, participants, and task prioritization.
- **Search and Pagination**: Efficient searching and paginated results for conversations and messages.

---

## Technologies Used

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **Authentication**: JWT
- **Message Queue**: Future enhancements can integrate something like Celery or RabbitMQ for offline messages (coming soon).
- **To-Do List Integration**: Todoist API for creating tasks from messages.
- **Testing**: Pytest for unit and integration tests.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/productivity-chat-app.git
cd productivity-chat-app
```

### 2. Set up the environment

Create a `.env` file or use the sample template to fill in your environment variables:

```env
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TODOIST_API_KEY=your-todoist-api-key
```

### 3. Install dependencies

Create a virtual environment and install required Python dependencies.

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

### 4. Database Setup

Run the migration scripts to set up the database schema.

```bash
# Assuming Alembic is used for migrations
alembic upgrade head
```

### 5. Running the Application

Run the app using `uvicorn`.

```bash
uvicorn api.main:app --reload
```

### 6. Access the API

Open the app in your browser at `http://127.0.0.1:8000`. You can access the API documentation via Swagger UI at `http://127.0.0.1:8000/docs`.

---

## API Endpoints

### Authentication

- **POST `/auth/login`**: Login a user and obtain a JWT access token.  
  - Input: Username and password.
  - Output: Access token and token type.

### Conversations

- **GET `/conversations/`**: Retrieve all conversations of the authenticated user.
  - Query parameters: `limit`, `skip`, `search` for pagination and searching by conversation title.
  - Output: List of conversations.

- **POST `/conversations/`**: Create a new conversation.
  - Input: List of participants and optional fields like `priority` and `title`.
  - Output: Newly created conversation details.

### Messages

- **POST `/messages/`**: Send a message in a conversation.
  - Input: `conversation_id` and `content` of the message.
  - Output: The newly created message.

### Tasks

- **POST `/tasks/`**: Add a message as a Todoist task.
  - Input: `message_id` to extract content.
  - Output: Task creation in Todoist with the task's URL.

---

## Testing

### Running Tests

To run the tests, ensure you have `pytest` installed and use the following command:

```bash
pytest
```

You can also run the tests using `pytest` with additional configuration in your IDE, or set up a continuous integration pipeline for automated tests.

---

## Contribution

Feel free to fork this repository and create a pull request with any improvements, bug fixes, or suggestions.

---

## License

Distributed under the MIT License. See LICENSE for more information.

---

## Future Features

- **Real-time Notifications**: Integrate websockets for live message notifications.
- **Task Creation from Messages**: Expand to include task integration with multiple productivity apps (e.g., Google Calendar).
- **Offline Messages**: Implement handling for offline users and delayed message delivery using a message queue.

---

### Breakdown of `README.md`:
- **App Overview**: A description of the app and its features.
- **Technologies Used**: An outline of key technologies and libraries.
- **Installation Instructions**: Step-by-step guide on how to set up the app locally, including environment setup, database configuration, and running the app.
- **API Endpoints**: A summary of the key API endpoints along with expected inputs and outputs.
- **Testing**: How to run the tests for your app.
- **Contribution**: Guidelines for contributing to the repository.
- **License**: Indicates the MIT License, which you can update based on your actual licensing preferences.

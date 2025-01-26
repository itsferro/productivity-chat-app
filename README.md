# Productivity Chat App

A productivity messaging app designed to help users efficiently capture task to Get Things Done productivity by integrating with productivity tools like Todoist. This app uses FastAPI, PostgreSQL, and integrates external APIs for task management.

the api is publicly available on "http://138.197.188.193/"
---

## Authors
**Feras Alzaidi**:
- Email: feras.mamon.alzaidi@gmail.com
- GitHub: https://github.com/itsferro

**Peninnah Kyakuwa**:
- Email: pennykyakuwa@gmail.com
- GitHub: https://github.com/Penin65n

---

## Features

- **User Authentication**: Secure login with JWT-based authentication.
- **Real-time Messaging(not implemented yet)**: Conversations between users with support for media messages (future enhancements).
- **Task Integration**: Ability to send messages to Todoist as tasks.
- **Conversation Management**: Manage conversations participants, and priority.
- **Search and Pagination**: Efficient searching and paginated results for users, conversations, and messages.

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

- **POST `/auth/signup`**: Sign up a new user by providing username, password, and an optional email.
- **POST `/auth/login`**: Login a user and obtain a JWT access token.  

### Users

- **GET `/users/`**: Retrieve all users.
- **GET `/users/{id}/status`**: (not implemented yet) Retrieve the user online/offline status.
- **GET `/users/{id}`**: Retrieve user details.
- **PUT `/users/{id}`**: Edit user details.
- **DELETE `/users/{id}`**: Delete user.
- **POST `/users/bans`**: (not implemented yet) Retrieve all users.

### Conversations

- **POST `/conversations/`**: reate a new conversation between the authenticated user and any other user.
- **GET `/conversations/`**: Retrieve all conversations of the authenticated user.
- **GET `/conversations/{id}/details`**: Retrieve all conversations details.
- **PUT `/conversations/{id}/details`**: Edit all conversations details.
- **GET `/conversations/{id}`**: Retrieve all conversations messages.
- **DELETE `/conversations/{id}`**: Delete conversation.

### Messages

- **POST `/messages/`**: Send a message in a conversation.
- **GET `/messages/{id}`**: Get message details.
- **PUT `/messages/{id}`**: Update a message content or status.
- **DELETE `/messages/{id}`**: Delete a message.

### Tasks

- **POST `/tasks/`**: Add a message as a Todoist task.

---

## Future Features

- **Real-time Notifications**: Integrate websockets for live message notifications.
- **Task Creation from Messages**: Expand to include task integration with multiple productivity apps (e.g., Google Calendar).
- **Offline Messages**: Implement handling for offline users and delayed message delivery using a message queue.

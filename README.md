A productivity chat app API
This is a productivity chat API built with FastAPI and SQLModel. It has integrations with the productivity apps, and helps user Get Things Done easier, faster, and efficient

Features
User Authentication with JWT access tokens
CRUD operations for users, messages, and coverstions
Support for real time chatting
Efficient database handling with SQLModel and PostgreSQL
exception handling for token validation and error responses

Getting Started
1. Clone the Repository
git clone https://github.com/itsferro/productivity-chat-app/
cd productivity-chat-app

2. Set Up Virtual Environment
python3 -m venv env source env/bin/activate

3. Install Dependencies
poetry install

4. Configure Environment Variables
Create a .env file in the project root:

DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/task_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Start the Application
fastapi dev api/

The API will be available at http://localhost:8000.

API Endpoints
Authentication
POST /auth/signup - Register a new user
POST /auth/login - Login and receive an access token

Users
GET /users/{user_id} - Get user details by ID
PUT /users/{user_id} - Update user details
DELETE /users/{user_id} - Delete a user

Tasks


Models
Conversation: Fields include title, priority.
User: Fields include username, email, phone, and last_seen_online.
Messages: Fields include content, status.

Authentication
After logging in, users receive an access token which should be included in the Authorization header for protected routes:

Authorization: Bearer your_jwt_token

Testing
Run tests with pytest:

pytest

Future Enhancements
Future goals include:
Creating a frontend interface

Author
Peninnah Kyakuwa pennykyakuwa@gmail.com
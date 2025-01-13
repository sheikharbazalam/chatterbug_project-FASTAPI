Password Generator & Bitcoin Price API with FastAPI and Vue.js

This project showcases a secure password generator along with a real-time Bitcoin price tracker, built using FastAPI for the backend and Vue.js for the frontend. The backend generates secure passwords and fetches Bitcoin prices from a third-party API, while the frontend visualizes the data using Chart.js.

🛠️ Technologies Used

Backend:

FastAPI (REST API framework)

Python 3.10+

Uvicorn (ASGI server)

Third-Party API Integration (real-time Bitcoin price)

Swagger UI (API documentation)

Postman/Insomnia (API testing tools)

Frontend:

Vue.js (for building the UI)

Chart.js (data visualization)

Tailwind CSS (styling framework)

🚀 Setup Instructions

1️⃣ Backend Setup

Prerequisites:

Python 3.10+

Steps:

Clone the repository:

git clone <repository_url>
cd <repository_folder>

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

Install dependencies:

pip install -r requirements.txt

Run the FastAPI server using Uvicorn:

uvicorn main:app --reload

Access the API documentation at:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

2️⃣ Frontend Setup

Prerequisites:

Node.js 22+

Steps:

Navigate to the frontend folder:

cd frontend

Install dependencies:

npm install

Run the development server:

npm run serve

Access the frontend at:

http://localhost:8080/

📋 API Endpoints

1️⃣ Password Generator API

Endpoint: /generate-password

Method: POST

Request Payload:

{
  "length": 12
}

Response:

{
  "password": "aB1cD2eF3gH4",
  "length": 12
}

Description: Generates a secure password of the specified length.

2️⃣ Bitcoin Price API

Endpoint: /get-bitcoin-price

Method: GET

Response:

{
  "price": 45678.90,
  "currency": "USD"
}

Description: Fetches the current Bitcoin price from a third-party API.

🎨 Frontend Features

Password Generator:

Users can generate secure passwords of custom lengths.

Bitcoin Price Tracker:

Displays real-time Bitcoin prices in a chart.

Responsive Design:

Styled using Tailwind CSS for a modern, mobile-friendly UI.

Pages:

Home Page:

Form to generate a secure password.

Displays the generated password and its length.

Bitcoin Price Page:

Real-time Bitcoin price visualization using Chart.js.

🧪 API Testing

You can test the backend API using the following tools:

Swagger UI:

Run the backend server and go to http://localhost:8000/docs.

Postman:

Import the API endpoints and send test requests.

Insomnia:

Another API testing tool to verify endpoint responses.

📄 Project Structure

.
├── backend
│   ├── main.py          # FastAPI application
│   ├── requirements.txt # Python dependencies
├── frontend
│   ├── src
│   │   ├── App.vue        # Main Vue component
│   │   └── components
│   │       ├── PasswordGenerator.vue
│   │       └── BitcoinPrice.vue
│   └── public
└── README.md

⚠️ Error Handling

Returns appropriate error messages for invalid inputs.

Gracefully handles third-party API downtime.

🧑‍💻 Contributors

Sheikh Arbaz Alam

📂 GitHub Repository

The code is available on GitHub at:

GitHub Repository Link

📸 Screenshots

Swagger UI:

Screenshot showing the API documentation interface.

Vue.js Frontend:

Screenshot of the password generator and Bitcoin price chart.

💡 Future Enhancements

Add password customization options (e.g., include special characters, symbols).

Integrate additional third-party APIs for financial data.

Improve UI/UX with animations and interactive charts.


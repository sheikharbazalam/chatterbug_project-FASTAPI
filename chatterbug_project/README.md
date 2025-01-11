## Chatterbug Password API

This is a FastAPI-based project that allows you to generate secure passwords and fetch real-time Bitcoin prices.

### Endpoints:
1. **POST /generate-password**
   - Generates a secure password based on specified criteria.
   - **Request Body**:
     ```json
     {
       "length": 12,
       "include_special": true,
       "include_numbers": true
     }
     ```
   - **Response**:
     ```json
     {
       "password": "GeneratedPassword123!",
       "length": 12
     }
     ```

2. **GET /bitcoin-price**
   - Fetches the current Bitcoin price in USD.
   - **Response**:
     ```json
     {
       "bitcoin_price_usd": 45000.00
     }
     ```

### Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd chatterbug_project

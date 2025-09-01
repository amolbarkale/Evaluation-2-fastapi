# Digital Wallet API Application

## Overview
This project is a FastAPI-based application that provides a digital wallet system. Users can manage their wallet balance, perform transactions, and transfer money to other users. The application includes endpoints for user management, wallet operations, and transfer functionality.

---

## Features
- **User Management**:
  - Create new users.
  - Retrieve user details.
  - Update user information.
- **Wallet Operations**:
  - Check wallet balance.
  - Add money to the wallet.
  - Withdraw money from the wallet.
- **Transfer Functionality**:
  - Transfer money between users.
  - Retrieve transfer details.

---

## Endpoints

### **User Endpoints**
- **`POST /users`**: Create a new user.
- **`GET /users/{user_id}`**: Retrieve user details.
- **`PUT /users/{user_id}`**: Update user information.

### **Wallet Endpoints**
- **`GET /wallet/{user_id}/balance`**: Check wallet balance.
- **`POST /wallet/{user_id}/add-money`**: Add money to the wallet.
- **`POST /wallet/{user_id}/withdraw`**: Withdraw money from the wallet.

### **Transfer Endpoints**
- **`POST /transfers`**: Transfer money between users.
- **`GET /transfers/{transfer_id}`**: Retrieve transfer details.

---

## Models

### **User Model**
- `id`: Unique identifier for the user.
- `username`: Username of the user.
- `email`: Email address of the user.
- `password`: Password for authentication.
- `phone_number`: Contact number of the user.
- `balance`: Wallet balance.
- `created_at`: Timestamp of user creation.
- `updated_at`: Timestamp of last update.

### **Transfers Model**
- `id`: Unique identifier for the transfer.
- `sender_user_id`: ID of the sender.
- `recipient_user_id`: ID of the recipient.
- `amount`: Amount transferred.
- `description`: Description of the transfer.
- `created_at`: Timestamp of transfer creation.

### **Transactions Model**
- `id`: Unique identifier for the transaction.
- `user_id`: ID of the user.
- `transaction_type`: Type of transaction (`CREDIT`, `DEBIT`, `TRANSFER_IN`, `TRANSFER_OUT`).
- `amount`: Amount involved in the transaction.
- `description`: Description of the transaction.
- `reference_transaction_id`: Reference ID for linked transactions.
- `recipient_user_id`: ID of the recipient (for transfers).
- `created_at`: Timestamp of transaction creation.

---

## Setup Instructions

### **Requirements**
- Python 3.10+
- FastAPI
- SQLAlchemy
- Uvicorn

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/amolbarkale/Evaluation-2-fastapi.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Evaluation-2-fastapi
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Run the Application**
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

### **Access the API**
Visit the API documentation at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Testing

### **Run Tests**
To run unit tests:
```bash
pytest
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author
**Amol Barkale**

# 🧪 Automation Test - SauceDemo

## 📌 Overview

This project contains automated test scripts for the SauceDemo application using **Python, Selenium, and Pytest**.
The tests cover login, add-to-cart, and checkout functionality.

---

## 🚀 Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)

---

## 📂 Project Structure

```
automation-task/
│
├── pages/
│   ├── login/
│   ├── products/
│   ├── cart/
│   └── checkout/
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── base/
│   └── basePage.py
│
├── conftest.py
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone repository

```
git clone <your-repo-url>
cd automation-task
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Tests

Run all tests:

```
pytest -s
```

Run specific test:

```
python -m pytest -s tests/test_login.py
```

---

## ✅ Test Coverage

### 1. Login

* Valid login
* Invalid login
* Locked user
* Empty fields validation

### 2. Add to Cart

* Add product to cart
* Validate product name
* Validate quantity

### 3. Checkout

* Fill checkout form with random data
* Complete checkout
* Validate success message
* Back to product page

---

## 🧠 Framework Design

* Page Object Model (POM)
* Reusable Base Page methods
* Data-driven testing approach
* Dynamic locators

---

## 🎯 Notes

* Uses dynamic locators for scalability
* Avoids hardcoded test data where possible
* Designed for easy extension and maintenance

---

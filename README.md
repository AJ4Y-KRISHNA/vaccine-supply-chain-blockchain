# 💉 Vaccine Supply Chain Tracking System (Blockchain + AI)

## 📌 Project Overview

This project implements a **Blockchain-based Vaccine Supply Chain Management System** that ensures transparency, traceability, and security in vaccine distribution.

The system integrates **Blockchain, Data Analytics, and Artificial Intelligence** to monitor vaccine movement from **manufacturer → distributor → healthcare centers**.

It also includes **AI-based demand forecasting and sentiment analysis** to help healthcare authorities make better decisions.

---

# 🚀 Technologies Used

| Technology        | Purpose                       |
| ----------------- | ----------------------------- |
| Python            | Backend logic                 |
| Streamlit         | Web Dashboard UI              |
| Solidity          | Smart contract                |
| Hardhat           | Local Ethereum blockchain     |
| Web3.py           | Python–Blockchain integration |
| Pandas            | Data analytics                |
| Transformers / ML | Sentiment analysis            |
| CSS               | UI styling                    |

---

# 🏗 System Architecture

```
Streamlit Dashboard
        ↓
Python Backend
        ↓
Web3 Connector
        ↓
Ethereum Smart Contract
        ↓
Hardhat Local Blockchain
```

---

# 📦 Project Modules

## 1️⃣ Dashboard

Main control panel showing system metrics and blockchain actions.

Features:

* Batch registration
* Batch transfer
* Transaction monitoring
* System statistics

---

## 2️⃣ Vaccine Batch Registration

Registers vaccine batches on blockchain.

Stored Data:

* Batch ID
* Vaccine Name
* Manufacturer
* Current Holder

---

## 3️⃣ Vaccine Transfer Tracking

Tracks movement of vaccine batches across supply chain participants.

Example flow:

```
Manufacturer → Distributor → Hospital
```

---

## 4️⃣ Real-Time Tracking

Users can verify batch details stored on blockchain.

Displayed data:

* Batch ID
* Vaccine
* Manufacturer
* Current holder

---

## 5️⃣ Blockchain Analytics

Interactive charts showing supply chain distribution statistics.

Technologies:

* Pandas
* Streamlit charts

---

## 6️⃣ Sentiment Analysis

AI module that analyzes public opinion regarding vaccines.

Output categories:

* Positive
* Negative
* Neutral

---

# ⚙️ How to Run the Project

### 1️⃣ Start Blockchain

```
cd blockchain-backend
npx hardhat node
```

---

### 2️⃣ Deploy Smart Contract

```
npx hardhat run scripts/deploy.js --network localhost
```

---

### 3️⃣ Run Dashboard

```
streamlit run app.py
```

---

# 📊 Features

✔ Blockchain-based vaccine tracking
✔ Transparent supply chain monitoring
✔ Real-time batch verification
✔ Data analytics dashboard
✔ AI sentiment analysis

---

# 🎯 Future Improvements

* QR code verification for vaccine batches
* IoT-based cold chain monitoring
* Cloud blockchain deployment
* Role-based authentication

---

# 👨‍💻 Author

Aj4yKrishna
Blockchain + AI Based Vaccine Supply Chain System

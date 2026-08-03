<<<<<<< HEAD
# Track_my_learn
TrackMyLearn is a machine learning-based application that analyzes users' study habits and learning patterns. It tracks study time, subjects, and consistency to provide personalized insights and recommendations. Built using Python, it helps users improve productivity through data-driven decisions.

🚀 Features
📊 Study Tracking – Records daily study time and subject-wise activity
📈 Pattern Analysis – Identifies learning trends using data analysis
🤖 ML-Based Insights – Uses machine learning to detect productivity patterns
🎯 Personalized Recommendations – Suggests improvements based on user behavior
📉 Data Visualization – Displays progress using charts and graphs

🛠️ Tech Stack
Programming Language: Python
Libraries: Pandas, NumPy, Matplotlib / Seaborn
Database (optional): MySQL / SQLite
Tools: Jupyter Notebook / VS Code

📂 Project Structure
TrackMyLearn/
│── data/                # Dataset (user study logs)
│── notebooks/           # Jupyter notebooks for analysis
│── src/                 # Source code
│   ├── data_processing.py
│   ├── model.py
│   ├── visualization.py
│── app.py               # Main application file
│── requirements.txt     # Dependencies
│── README.md            # Project documentation

⚙️ How It Works
User inputs study data (time, subject, frequency)
Data is stored and processed
ML model analyzes patterns and trends
System generates insights and recommendations
Results are visualized using graphs

▶️ Installation & Setup
git clone https://github.com/Gaurav-21-06/Track_my_learn.git
cd TrackMyLearn
pip install -r requirements.txt
python app.py

📌 Future Enhancements
📱 Mobile app integration
☁️ Cloud-based data storage
🔔 Smart reminders & notifications
🧠 Advanced ML models for better predictions
🤝 Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request.
=======
# TrackMyLearn AI

TrackMyLearn AI is an intelligent study habit tracking system that helps users monitor their learning habits and analyze their productivity using machine learning techniques.

The system allows users to log study activities, track habits, analyze performance trends, and receive AI-based predictions and recommendations to improve learning efficiency.

---

## 🚀 Features

### User Authentication

* User signup and login
* Secure password hashing using Flask-Bcrypt
* Session management using Flask-Login

### Habit Tracking

* Create and manage study habits
* Categories: Programming, Mathematics, Reading, Science, Language, Other
* Difficulty levels: Easy, Medium, Hard

### Study Logging

Users can log:

* Study time
* Skipped days
* Quiz score
* Mood level
* Focus level
* Completion status

### Study Timer

Built-in timer to track study sessions and store session durations.

### Dashboard Analytics

Interactive dashboard showing:

* Total study time
* Completed tasks
* Skipped tasks
* Current streak
* Weekly study progress (Bar Chart)
* Completion ratio (Pie Chart)

Charts are powered by **Chart.js**.

### AI Insights

The system analyzes user study behavior to determine:

* Best study time
* Most productive category
* Average focus level
* Focus trend over time

### AI Prediction

A machine learning model predicts whether a user will **complete or skip a habit** based on:

* Study time
* Skipped days
* Quiz score
* Mood
* Focus

Model used: **Random Forest Classifier**

### AI Recommendation

The system recommends optimal study duration using:

* Regression model
* Previous study performance

### AI Productivity Score

The dashboard calculates a productivity score based on:

* Focus level
* Quiz performance
* Study time
* Skipped days

This gives users a quick overview of their study efficiency.

---

## 🧠 Machine Learning Components

| Feature                     | Algorithm          |
| --------------------------- | ------------------ |
| Habit Completion Prediction | Random Forest      |
| Study Time Recommendation   | Linear Regression  |
| Behavior Pattern Analysis   | K-Means Clustering |

---

## 🛠 Tech Stack

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

### Backend

* Python
* Flask

### Database

* MySQL (XAMPP)

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

---

## 📂 Project Structure

```
trackmylearn_ai/
│
├── app.py
├── config.py
├── requirements.txt
│
├── routes/
│   ├── auth_routes.py
│   ├── dashboard_routes.py
│   ├── habit_routes.py
│   ├── studylog_routes.py
│   ├── timer_routes.py
│   ├── insights_routes.py
│   ├── prediction_routes.py
│   ├── history_routes.py
│   └── recommendation_routes.py
│
├── templates/
│
├── static/
│   ├── css/
│   └── js/
│
├── utils/
│   ├── db_connection.py
│   ├── insights_engine.py
│   ├── recommendation_engine.py
│   ├── productivity_engine.py
│   └── ml_loader.py
│
└── ml/
    ├── datasets/
    ├── models/
    ├── generate_dataset.py
    ├── train_prediction_model.py
    └── train_recommendation_model.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/trackmylearn_ai.git
cd trackmylearn_ai
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Setup MySQL Database

Start **XAMPP** and open **phpMyAdmin**.

Create a database:

```
trackmylearn_ai
```

Import the required tables.

### 4️⃣ Generate Dataset

```
python ml/generate_dataset.py
```

### 5️⃣ Train Machine Learning Models

```
python ml/train_prediction_model.py
python ml/train_recommendation_model.py
```

### 6️⃣ Run the Application

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 📊 Future Improvements

* Real-time model retraining using user data
* Advanced productivity analytics
* Mobile responsive UI
* Cloud deployment

---

## 👨‍💻 Author

Developed as a Machine Learning + Full Stack project for academic and portfolio purposes.
>>>>>>> b8109e6 (Initial commit)

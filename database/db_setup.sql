CREATE DATABASE IF NOT EXISTS trackmylearn_ai;
USE trackmylearn_ai;

-- ==============================
-- USERS TABLE
-- ==============================

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==============================
-- EMAIL VERIFICATION TOKENS
-- ==============================

CREATE TABLE email_verification (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    token VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- ==============================
-- HABITS TABLE
-- ==============================

CREATE TABLE habits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    habit_name VARCHAR(100),
    category VARCHAR(50),
    difficulty VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- ==============================
-- STUDY LOGS TABLE
-- ==============================

CREATE TABLE study_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    habit_id INT,
    study_time INT,
    skipped_days INT,
    quiz_score INT,
    mood INT,
    focus INT,
    completed BOOLEAN,
    log_date DATE DEFAULT (CURRENT_DATE),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (habit_id) REFERENCES habits(id) ON DELETE CASCADE
);

-- ==============================
-- TIMER LOGS TABLE
-- ==============================

CREATE TABLE timer_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    habit_id INT,
    duration_seconds INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (habit_id) REFERENCES habits(id) ON DELETE CASCADE
);

-- ==============================
-- PREDICTION HISTORY
-- ==============================

CREATE TABLE prediction_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    habit_id INT,
    study_time INT,
    skipped_days INT,
    quiz_score INT,
    mood INT,
    focus INT,
    prediction_result VARCHAR(50),
    confidence FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (habit_id) REFERENCES habits(id) ON DELETE CASCADE
);
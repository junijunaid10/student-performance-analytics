# Student Performance Analytics System

### 1. Project Title
* **Project Name:** Student Performance Analytics System
* **Author:** Mohammad Rafiq Tantray
* **Domain:** Python with AI (Batch 1)
* **Organization:** EWB EduTech Private Limited

---

### 2. Objective
The objective of this project is to develop a modular, Python-driven analytics system that automates the evaluation of student academic records. The system reads structured academic datasets, computes statistical metrics, assigns performance grades, tracks attendance, and identifies top and bottom performers to help educational institutions make data-backed decisions.

---

### 3. Technologies Used
* **Programming Language:** Python 3.x
* **Numerical Processing:** NumPy
* **Data Manipulation & Analysis:** Pandas
* **Version Control:** Git & GitHub

---

### 4. Dataset Description
The dataset (`students.csv`) consists of 20 realistic student records across multiple engineering departments (CSE, ECE, MECH, CIVIL) with the following attributes:
* `StudentID`: Unique identifier for each student (e.g., STU001).
* `Name`: Full name of the student.
* `Department`: Academic branch/department.
* `Maths`, `Physics`, `Chemistry`: Marks obtained in individual subjects (out of 100).
* `Attendance`: Class attendance percentage.

---

### 5. Implementation
The solution is implemented sequentially through structured functions:
1. **Data Ingestion:** Pandas reads `students.csv` into a structured DataFrame.
2. **Numerical Computation:** Subject marks are vectorized into NumPy arrays to calculate `Total_Marks` and `Average_Marks` efficiently.
3. **Evaluation Logic:** Custom functions and iterative loops evaluate individual subject scores against minimum passing standards (minimum 40 marks per subject) and assign percentage-based letter grades.
4. **Performance Aggregation:** Aggregation functions compute class-wide statistics, subject-wise averages, and department summaries.

---

### 6. Key Features
* Automated calculation of total marks and average scores.
* Dynamic letter grading system (A+, A, B, C, D, F).
* Subject-level pass/fail validation.
* Subject-wise class average benchmark comparison.
* Ranking mechanism to identify top-performing students.
* Department-wise performance grouping.

---

### 7. Output Summary
* **Total Records Evaluated:** 20
* **Class Overall Average:** 68.60%
* **Passing Percentage:** 80.0%
* **Highest Scorer:** Ananya Sen (Total: 283/300, Average: 94.33%, Grade: A+)

---

### 8. Final Outcome
The project successfully delivers an automated data analysis pipeline that transforms raw tabular student marks into actionable academic insights without requiring manual calculation.

---

### 9. Challenges & Learning
* **Vectorized Array Operations:** Learned how converting Pandas columns to NumPy arrays speeds up numerical calculations.
* **Conditional Row Iteration:** Handled multi-subject pass/fail criteria using structured decision conditions within iterative loops.
* **Data Organization:** Learned practical version control and project repository structuring on GitHub.

---

### 10. GitHub Repository
* **Repository URL:** https://github.com/junijunaid10/student-performance-analytics

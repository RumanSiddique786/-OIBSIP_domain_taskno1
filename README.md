# -OIBSIP_domain_taskno1
This is my work as the data science intern 

# 🌸 Iris Flower Classification using Machine Learning

## Project Overview

This project focuses on building a Machine Learning model to classify Iris flowers into different species based on their physical measurements.  

The Iris dataset is one of the most popular beginner datasets in data science and is widely used for classification problems.

The model predicts the species of an Iris flower using features such as:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

---

##  Objective

The objective of this project is to:

- Load and explore the Iris dataset
- Perform basic data preprocessing
- Split the dataset into training and testing sets
- Train a Logistic Regression classification model
- Evaluate model performance
- Predict the species of a new flower sample

---

##  Dataset Information

- **Source:** Kaggle  
- **Dataset Name:** Iris CSV  
- **Provider:** saurabh00007  
- **Total Records:** 150  
- **Target Variable:** Species  

The dataset contains three flower species:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

---

##  Tools & Technologies Used

- **Python**
- **Pandas** – Data loading and preprocessing
- **Scikit-learn** – Machine Learning model training
- **KaggleHub** – Dataset download

---

##  Steps Performed

1. Downloaded the dataset using KaggleHub.
2. Loaded the dataset into a Pandas DataFrame.
3. Removed the unnecessary `Id` column.
4. Separated features (X) and target variable (y).
5. Split the dataset into training and testing sets (80% training, 20% testing).
6. Trained a Logistic Regression model.
7. Evaluated the model using accuracy score.
8. Predicted the species for a new sample flower.

---

##  Model Performance

- **Algorithm Used:** Logistic Regression
- **Accuracy Achieved:** 100% (on test data)

The model performed very well on the dataset and correctly classified the flower species.

---

## 🌼 Sample Prediction

Example input:
Sepal Length = 5.1  
Sepal Width = 3.5  
Petal Length = 1.4  
Petal Width = 0.2

Predicted Output:
Iris-setosa



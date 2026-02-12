import kagglehub
import os
import pandas as pd

path = kagglehub.dataset_download("saurabh00007/iriscsv")
print("Dataset downloaded at:", path)

# Load dataset
file_path = os.path.join(path, "Iris.csv")
data = pd.read_csv(file_path)

print(data.head())


# Remove unnecessary column
data.drop(columns=['Id'], inplace=True)

print(data.info())

# Features and target
X = data.drop('Species', axis=1)
y = data['Species']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

sample_flower = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=X.columns
)

prediction = model.predict(sample_flower)
print("Predicted Species:", prediction[0])


import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class TitanicSurvivalPredictor:
    def __init__(self, random_state: int = 42):
        self.model = RandomForestClassifier(n_estimators=100, random_state=random_state)
        self.features = ['Pclass', 'Sex_Code', 'Age', 'SibSp', 'Parch', 'Fare']

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        data = df.copy()
        if 'Sex' in data.columns:
            data['Sex_Code'] = data['Sex'].map({'female': 1, 'male': 0}).fillna(0)
        if 'Age' in data.columns:
            data['Age'] = data['Age'].fillna(data['Age'].median() if not data['Age'].empty else 28.0)
        if 'Fare' in data.columns:
            data['Fare'] = data['Fare'].fillna(data['Fare'].median() if not data['Fare'].empty else 14.0)
        return data

    def fit(self, X: pd.DataFrame, y: pd.Series):
        X_proc = self.preprocess(X)
        self.model.fit(X_proc[self.features], y)
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        X_proc = self.preprocess(X)
        return self.model.predict(X_proc[self.features])

import pytest
import pandas as pd
import numpy as np
from src.titanic_engine import TitanicSurvivalPredictor

def test_titanic_engine_workflow():
    train_df = pd.DataFrame({
        'Pclass': [1, 3, 2, 3],
        'Sex': ['female', 'male', 'female', 'male'],
        'Age': [29.0, 22.0, 38.0, 26.0],
        'SibSp': [0, 1, 1, 0],
        'Parch': [0, 0, 0, 0],
        'Fare': [100.0, 7.5, 30.0, 8.0]
    })
    y = pd.Series([1, 0, 1, 0])
    
    predictor = TitanicSurvivalPredictor()
    predictor.fit(train_df, y)
    preds = predictor.predict(train_df)
    
    assert len(preds) == 4
    assert np.all(np.isin(preds, [0, 1]))

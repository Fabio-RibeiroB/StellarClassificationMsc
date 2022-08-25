import joblib
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
loaded_rf = joblib.load("./random_forest.pkl")
filename=input('Enter file path:')
data = pd.read_csv(filename)
data = data[['u','g','r','i','z', 'redshift']]
prediction = pd.DataFrame(loaded_rf.predict(data))
prediction.to_csv('rf_predictions.csv')
print(prediction.value_counts())
prediction.to_csv('rf_predictions.csv')

import pickle
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
loaded_model = pickle.load(open('finalised_model.sav', 'rb'))
filename=input('Enter file path:')
data = pd.read_csv(filename)
data = data[['u','g','r','i','z', 'redshift']]
prediction = pd.DataFrame(loaded_model.predict(data))
prediction.to_csv('rf_predictions.csv')
print(prediction.value_counts())

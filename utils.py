import numpy as np
import json
import pickle 
import os
import warnings
warnings.filterwarnings("ignore")

class RegressionModel():
    def __init__(self,coin_name,high_value,low_value,open_value,volume_shared,marketcap,date_year,date_month,date_day):
       
        self.coin_name = coin_name
        self.high_value = high_value
        self.low_value = low_value
        self.open_value = open_value
        self.volume_shared = volume_shared
        self.marketcap = marketcap
        self.date_year = date_year
        self.date_month = date_month
        self.date_day = date_day

    def load_model(self):
        with open("lr_model.pkl","rb") as f :
            self.model = pickle.load(f)

        with open("robust_scaling.pkl","rb") as f :
            self.robust_scalar = pickle.load(f)

        with open("features_names.json","r") as f :
            self.features = json.load(f)

    def get_predict(self):

        self.load_model()
        test_array = np.zeros(len(self.features["feature_names"]))

        test_array[0] = self.features["coin_name"][self.coin_name]
        test_array[1] = self.high_value
        test_array[2] = self.low_value
        test_array[3] = self.open_value
        test_array[4] = self.volume_shared
        test_array[5] = self.marketcap
        test_array[6] = self.date_year
        test_array[7] = self.date_month
        test_array[8] = self.date_day

        scaled_array = self.robust_scalar.transform([test_array])

        predicted_value = self.model.predict(scaled_array)

        result = predicted_value[0]

        return result

# obj = RegressionModel("Bitcoin",700.976013,644.026001,700.177979,2.230470e+09,6.451766e+10,2018,5,22)
# print(obj.get_predict())
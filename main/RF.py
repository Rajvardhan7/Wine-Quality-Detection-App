import pandas as pd
import joblib

class MLmodel1():
    model = joblib.load("random_forest.joblib")
    #def __init__(self):
     #   pathToSavedModels = "research/"
      #  self.model = joblib.load("random_forest.joblib")
       # self.encoders = joblib.load(pathToSavedModels + "encoders")

    def preprocessing(self, input_data):
        input_data = pd.DataFrame(input_data, index=[0])

        for column in [
            "workclass",
            "education",
            "marital_status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "native_country",
            ]:
            categorical_convert = self.encoders[column]
            input_data[column] = categorical_convert.transform(input_data[column])

        return input_data

    def predict(self, input_data):
        return self.model.predict_proba(input_data)

    def make_prediction(self, input_data):
        input_data = self.preprocessing(input_data)
        prediction =  self.predict(input_data)[0]
        return prediction
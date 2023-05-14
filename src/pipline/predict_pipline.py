import os
import sys
import pandas as pd 
import numpy as np 
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from src.utils import load_object

class PredictPipline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            ## Load pickel File
            ## This Code Work in /any system
            preprocessor_path = os.path.join("artifcats","preprocessor.pkl")
            model_path = os.path.join("artifcats","model.pkl")

            # Load Pickel File
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            logging.info("Error Occure in Prediction Pipline")
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                SEX:int,
                EDUCATION:int,
                AGE:int,
                PAY_0:int,
                PAY_2:int,
                PAY_3:int,
                PAY_4:int,
                PAY_5:int,
                PAY_6:int):

            self.SEX = SEX
            self.EDUCATION = EDUCATION
            self.AGE = AGE
            self.PAY_0 = PAY_0
            self.PAY_2 = PAY_2
            self.PAY_3 = PAY_3
            self.PAY_4 = PAY_4
            self.PAY_5 = PAY_5
            self.PAY_6 =  PAY_6


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "SEX":[self.SEX],
                "EDUCATION":[self.EDUCATION],
                "AGE":[self.AGE],
                "PAY_0":[self.PAY_0],
                "PAY_2":[self.PAY_2],
                "PAY_3":[self.PAY_3],
                "PAY_4":[self.PAY_4],
                "PAY_5":[self.PAY_5],
                "PAY_6":[self.PAY_6]
            }
            
            

            data = pd.DataFrame(custom_data_input_dict)
            logging.info("Data Frame Gathered")
            return data

            print(data)

        except Exception as e:
            logging.info("Error Occured In Predict Pipline")
            raise CustomException(e, sys)









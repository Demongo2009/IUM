import xgboost
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd

class ModelA():

    def __init__(self, modelSavePath):
        self.xGBClassifier = XGBClassifier()
        self.modelSavePath = modelSavePath

        if modelSavePath.is_file():
            self.xGBClassifier.load_model(modelSavePath)

    def train(self, xTrain, yTrain):
        trainDMatrix = xgboost.DMatrix(xTrain.values, yTrain.values)
        params = {
            "learning_rate": 0.01,
            "max_depth": 25
        }
        self.xGBClassifier = xgboost.train(params, trainDMatrix, num_boost_round=100, early_stopping_rounds=20)
        self.xGBClassifier.safe_model(self.modelSavePath)

    def predict(self,
                discount,
                buyingProductFrequency,
                buyingFrequency,
                userBuyingProductFrequency,
                buyingWithBiggerDiscountFrequency,
                buyingWithLowerDiscountFrequency,
                buyingWithDiscountFrequency,
                buyingWithoutDiscountFrequency,
                buyingThisProductWithBiggerDiscountFrequency,
                buyingThisProductWithLowerDiscountFrequency,
                buyingThisProductWithDiscountFrequency,
                buyingThisProductWithoutDiscountFrequency,
                userBuyingThisProductWithBiggerDiscountFrequency,
                userBuyingThisProductWithLowerDiscountFrequency,
                userBuyingThisProductWithDiscountFrequency,
                userBuyingThisProductWithoutDiscountFrequency,
                differenceBiggerLower,
                differenceDiscountWithout,
                differenceThisProductBiggerLower,
                uesrDifferenceThisProductBiggerLower):

        x = [discount,
             buyingProductFrequency,
             buyingFrequency,
             userBuyingProductFrequency,
             buyingWithBiggerDiscountFrequency,
             buyingWithLowerDiscountFrequency,
             buyingWithDiscountFrequency,
             buyingWithoutDiscountFrequency,
             buyingThisProductWithBiggerDiscountFrequency,
             buyingThisProductWithLowerDiscountFrequency,
             buyingThisProductWithDiscountFrequency,
             buyingThisProductWithoutDiscountFrequency,
             userBuyingThisProductWithBiggerDiscountFrequency,
             userBuyingThisProductWithLowerDiscountFrequency,
             userBuyingThisProductWithDiscountFrequency,
             userBuyingThisProductWithoutDiscountFrequency,
             differenceBiggerLower,
             differenceDiscountWithout,
             differenceThisProductBiggerLower,
             uesrDifferenceThisProductBiggerLower]
        return self.xGBClassifier.predict(x)

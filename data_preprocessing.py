import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from collections import  Counter
from imblearn.over_sampling import SMOTE

def load_data(file_path):
    data=pd.read_csv(file_path)
    return data

def preprocess_data(data):
    data.drop('Amount',axis=1, inplace=True)


def split_data(data):
    x_train,x_test,y_train,y_test=train_test_split(data.drop('Output',axis=1),data['Output'],test_size=0.25,random_state=42)
    return x_train,x_test,y_train,y_test

def scale_data(x_train,x_test):
    scaler=RobustScaler()
    x_train=scaler.fit_transform(x_train)
    x_test=scaler.transform(x_test)
    return x_train,x_test

def balance_data(x_train,y_train):
    print('Original dataset shape %s' % Counter(y_train))

    smt = SMOTE(random_state=42)
    x_train_smt, y_train_smt = smt.fit_resample(x_train, y_train)

    print('Resampled dataset shape %s' % Counter(y_train_smt))

    return x_train_smt,y_train_smt







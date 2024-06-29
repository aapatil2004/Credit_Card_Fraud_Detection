import pandas as pd
import model_testing
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import accuracy_score,roc_auc_score,f1_score

def prepare_data(new_data,x_train):
    scaler=RobustScaler()
    x_train_scaled2=scaler.fit_transform(x_train)
    print("Initiating the scaling of new data.\n")
    new_data_scaled=scaler.transform(new_data)
    print("Scaling of new data completed.\n")
    return new_data_scaled

def make_prediction(model,new_data):
    print("Initiating the prediction.\n")
    y_pred_new=model.predict(new_data)
    print("Prediction process completed")
    return y_pred_new

def display_prediction(y_pred_new,y_test):
    # accuracy_new=accuracy_score(y_test,y_pred_new)
    # roc_auc_new=roc_auc_score(y_test,y_pred_new)
    # f1_new=f1_score(y_test,y_pred_new)
    # #accuracy_new,roc_auc_new,f1_new=model_testing.evaluate_model(y_test,y_pred_new)
    if(y_pred_new[0]==0):
        print("According to the model's prediction, the transaction is legitimate.\n")
    else:
        print("According to the model's prediction, the transaction is fraud.\n")
    print("The accuracy of prediction is ".format(model_testing.accuracy_score))
    #return accuracy_new,roc_auc_new,f1_new




def predtocsv(new_data,y_pred_new,filepath):
    columns=new_data.columns.tolist()+['Output']
    predictiondf=pd.DataFrame([new_data.values[0].tolist()+[y_pred_new[0]]],columns=columns)
    predictiondf.to_csv(filepath,index=False)
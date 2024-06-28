import pandas as pd

def make_prediction(model,new_data):
    print("Initiating the prediction.\n")
    y_pred_new=model.predict(new_data)
    print("Prediction process completed")
    return y_pred_new

def display_prediction(y_pred_new):
    if(y_pred_new[0]==0):
        print("According to the model's prediction, the transaction is legitimate.\n")
    else:
        print("According to the model's prediction, the transaction is fraud.\n")


def predtocsv(new_data,y_pred_new,filepath):
    columns=new_data.columns.tolist()+['Output']
    predictiondf=pd.DataFrame([new_data.values[0].tolist()+[y_pred_new[0]]],columns=columns)
    predictiondf.to_csv(filepath,index=False)
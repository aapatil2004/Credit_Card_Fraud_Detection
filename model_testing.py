from sklearn.metrics import accuracy_score,roc_auc_score,f1_score,classification_report,confusion_matrix

def test_model(model,x_test):
    print("Initiating the testing of the model.\n")
    y_pred=model.predict(x_test)
    print("Model testing completed.\n")
    return y_pred

def evaluate_model(y_test,y_pred):
    accuracy=accuracy_score(y_test,y_pred)
    roc_auc=roc_auc_score(y_test,y_pred)
    f1=f1_score(y_test,y_pred)
    print("Accuracy Score: {}".format(accuracy))
    print("Roc Auc Score: {}".format(roc_auc))
    print("F1 score: {}".format(f1))
    print("\nThe classification report:-\n")
    print(classification_report(y_test,y_pred))
    print("\nThe confusion matrix:-\n")
    print(confusion_matrix(y_test,y_pred))


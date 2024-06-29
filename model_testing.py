import time
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,roc_auc_score,f1_score,classification_report,confusion_matrix,roc_curve

def test_model(model,x_test):
    t0=time.time()
    print("Initiating the testing of the model.\n")
    y_pred=model.predict(x_test)
    print("Model testing completed.\n")
    time_taken=time.time()-t0
    return y_pred,time_taken

def plot_roc_cur(fper, tper):
    plt.plot(fper, tper, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()

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
    # print("The time taken for the model testing is {}".format(time_taken))
    # probs = model.predict_proba(x_test)
    # probs = probs[:, 1]
    # fper, tper, thresholds = roc_curve(y_test, probs)
    # plot_roc_cur(fper, tper)
    return accuracy,roc_auc,f1



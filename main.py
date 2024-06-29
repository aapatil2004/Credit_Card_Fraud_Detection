import data_preprocessing
import model_training
import model_testing
import prediction

def main():
    #Loading the data
    #filepath=input("Enter the filepath.\n:-")
    data=data_preprocessing.load_data("data/finaldataset.csv")

    #preprocessing the data
    data_preprocessing.preprocess_data(data)

    #Splitting the data
    x_train,x_test,y_train,y_test=data_preprocessing.split_data(data)

    #Scaling the data
    x_train_scaled,x_test_scaled=data_preprocessing.scale_data(x_train,x_test)

    #Balancing the data
    x_train_smt,y_train_smt=data_preprocessing.balance_data(x_train_scaled,y_train)

    #Training the model and determinig the best version of it using the hyper parameter tuning
    final_model=model_training.train_model(x_train_smt,y_train_smt)

    #Testing the model
    y_pred_initial,time_taken_initial=model_testing.test_model(final_model,x_test_scaled)

    #Evaluating the model
    model_testing.evaluate_model(y_test,y_pred_initial)

    filepath_newdata=input("Enter the filepath:-\n")
    new_data=data_preprocessing.load_data(filepath_newdata)

    #Predicting
    y_pred_new=prediction.make_prediction(final_model,new_data)

    prediction.display_prediction(y_pred_new)

if __name__== '__main__':
    main()


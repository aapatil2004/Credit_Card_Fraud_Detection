import xgboost as xgb
from sklearn.model_selection import GridSearchCV


def train_model(x_train,y_train):
    params_xgb={'n_estimators': 20,'max_depth': 16}

    model=xgb.XGBClassifier(**params_xgb)
    print("Starting the training.\n")
    model.fit(x_train,y_train)
    print("Model training Completed.\n")
    
    # param_grid = {
    #     'ax_depth': [3, 5, 7],
    #     'learning_rate': [0.1, 0.5, 1],
    #     'n_estimators': [50, 100, 200],
    #     'gamma': [0, 0.1, 0.5],
    #     'colsample_bytree': [0.5, 0.8, 1],
    #     'ubsample': [0.5, 0.8, 1],
    #     'eg_alpha': [0, 0.1, 0.5],
    #     'eg_lambda': [0, 0.1, 0.5]

    # }

    # Perform hyperparameter tuning using GridSearchCV
    #grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
    #grid_search.fit(x_train, y_train)

    # Get the best model and its hyperparameters
    #best_model = grid_search.best_estimator_
    #best_params = grid_search.best_params_

    #print(f'Best hyperparameters: {best_params}')
    #print(f'Best model score: {grid_search.best_score_:.3f}')

    return model


















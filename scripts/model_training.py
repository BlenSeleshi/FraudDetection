import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import tensorflow as tf

# Check for GPU availability
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
    print('GPU device not found. Using CPU.')
else:
    print(f'Found GPU at: {device_name}')

# Random Forest Model with Hyperparameter Tuning
def random_forest_model(X_train, y_train, X_test, y_test):
    rf = RandomForestClassifier()
    param_grid = {'n_estimators': [100, 200], 'max_depth': [10, 20], 'min_samples_split': [2, 5]}
    
    grid_search = GridSearchCV(rf, param_grid, scoring='accuracy', cv=5)
    grid_search.fit(X_train, y_train)

    best_rf = grid_search.best_estimator_
    y_pred = best_rf.predict(X_test)

    evaluate_model(y_test, y_pred, "Random Forest")
    return best_rf

# Gradient Boosting Model with Hyperparameter Tuning
def gradient_boosting_model(X_train, y_train, X_test, y_test):
    gb = GradientBoostingClassifier()
    param_grid = {'n_estimators': [100, 200], 'learning_rate': [0.1, 0.01], 'max_depth': [3, 5]}
    
    grid_search = GridSearchCV(gb, param_grid, scoring='accuracy', cv=5)
    grid_search.fit(X_train, y_train)

    best_gb = grid_search.best_estimator_
    y_pred = best_gb.predict(X_test)

    evaluate_model(y_test, y_pred, "Gradient Boosting")
    return best_gb

# Multi-Layer Perceptron (MLP) Model with Hyperparameter Tuning
def mlp_model(X_train, y_train, X_test, y_test):
    mlp = MLPClassifier()
    param_grid = {'hidden_layer_sizes': [(100,), (150,)], 'activation': ['relu', 'tanh'], 'solver': ['adam']}
    
    grid_search = GridSearchCV(mlp, param_grid, scoring='accuracy', cv=5)
    grid_search.fit(X_train, y_train)

    best_mlp = grid_search.best_estimator_
    y_pred = best_mlp.predict(X_test)

    evaluate_model(y_test, y_pred, "MLP")
    return best_mlp

# LSTM Model with GPU Utilization and Early Stopping
def lstm_model(X_train, y_train, X_test, y_test):
    # Reshaping for LSTM input (required format: [samples, time_steps, features])
    X_train_reshaped = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
    X_test_reshaped = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

    model = Sequential()
    model.add(LSTM(100, activation='relu', input_shape=(1, X_train.shape[1])))
    model.add(Dropout(0.2))  # Dropout to prevent overfitting
    model.add(Dense(1, activation='sigmoid'))  # Output layer for binary classification
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    # Training the model
    model.fit(X_train_reshaped, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

    # Predictions
    y_pred_prob = model.predict(X_test_reshaped)
    y_pred = (y_pred_prob > 0.5).astype("int32")  # Threshold to get binary class

    evaluate_model(y_test, y_pred, "LSTM")
    return model


# Evaluation Metrics and Plotting Confusion Matrix
def evaluate_model(y_test, y_pred, model_name):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    print(f"{model_name} Accuracy: {accuracy:.4f}")
    print(f"{model_name} Precision: {precision:.4f}")
    print(f"{model_name} F1 Score: {f1:.4f}")
    print(f"{model_name} ROC AUC: {roc_auc:.4f}")
    print(f"{model_name} Confusion Matrix:\n {cm}")
    
    # Plot confusion matrix
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"{model_name} Confusion Matrix")
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

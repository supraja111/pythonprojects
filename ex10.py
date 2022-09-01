import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataframe=pd.read_csv("dataset.csv")
x= dataframe['Feature'].values
y= dataframe['Class'].values
from sklearn.model_selection import train_test_split
features_tr, features_te, label_tr, label_te= train_test_split(x, y, random_state=0, train_size= 0.5 )
features_tr = np.array (features_tr).reshape(-1,1)
features_te = np.array (features_te). reshape(-1,1)
from sklearn.preprocessing import StandardScaler
normalization= StandardScaler()
features_tr= normalization.fit_transform (features_tr)
features_te= normalization.transform (features_te)
from sklearn.neighbors import KNeighborsClassifier
model= KNeighborsClassifier (n_neighbors=3 )
model.fit (features_tr, label_tr)
predict_class= model.predict (features_te)
print ("Predicted Test Samples Output: ",predict_class)
from sklearn.metrics import confusion_matrix
model_evaluation= confusion_matrix(label_te, predict_class)
print ("Confusion matrix: \n", model_evaluation)
count=sum (sum(model_evaluation))
accuracy=(model_evaluation[0,0]+model_evaluation[1,1])/count
print ('Accuracy =:accuracy')
sense = model_evaluation[0,0]/(model_evaluation[0,0]+model_evaluation[0,1])
print ('Sensitivity sense')
spec = model_evaluation[1,1]/(model_evaluation[1, 0]+model_evaluation[1,1])
print('Specificity =: ', spec)

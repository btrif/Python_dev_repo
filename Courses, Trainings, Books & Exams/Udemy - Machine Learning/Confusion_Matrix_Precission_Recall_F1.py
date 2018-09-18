#  Created by Bogdan Trif on 04-07-2018 , 1:45 PM.

'''

# Confusion Matrix
# First row is called Negative Class - in our case the non-zeros
# Second row is the positive Class - the Actual Zeros
# The first column is the Negative Prediction
# The Second Column is the Positive Prediction

Confusion Matrix is a 2x2 Matrix which has the role to calculate the following Parameters :
----------
1.  PRECISION

**Precision** measures the accuracy of positive predictions. Also called the `precision` of the classifier

precision = True Positives / ( True Positives + False Positives)
----------
2.  RECALL
`Precision` is typically used with `recall` (`Sensitivity` or `True Positive Rate`).
The ratio of positive instances that are correctly detected by the classifier.

recall = True Positives / (True Positives + False Negatives)
--------
3.  F1 SCORE

F1 score is the harmonic mean of precision and recall.
Regular mean gives equal weight to all values. Harmonic mean gives more weight to low values.

F1 = 2 / (1/precision + 1/recall ) = 2 × (precision × recall) / ( precision + recall ) = TP / (TP + FN+FP/2)
The F1 score favours classifiers that have similar precision and recall.

Example :
confusion_matrix(y_train_0, y_train_pred)
array([[53543,   534],
       [  354,  5569]], dtype=int64)
'''

import  numpy as np

def get_precision_recall_f1_scores( matrix2x_2  ) :
    confusion_matrix = np.array( matrix2x_2 )
    print('confusion_matrix : \n',confusion_matrix)
    precision = confusion_matrix[1][1] /(confusion_matrix[1][1]+confusion_matrix[0][1])
    print('Precision score : ', round(precision,4)  )
    recall = confusion_matrix[1][1] /(confusion_matrix[1][1]+confusion_matrix[1][0])
    print('Recall score : ', round(recall,4) )

    F1 = 2/(1/precision + 1/recall )
    print('F1 score : ', round(F1, 4) )
    return precision, recall, F1


get_precision_recall_f1_scores( [[ 1000, 50], [35, 950] ] )
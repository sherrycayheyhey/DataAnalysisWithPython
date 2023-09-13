import numpy as np

'''
The input of the function should be a list containing 9 digits. 

The function should convert the list into a 3 x 3 Numpy array, and then return a 
dictionary containing the mean, variance, standard deviation, max, min, and sum along 
both axes and for the flattened matrix.
'''

def calculate(list):
  if len(list)==9:
    #turn the list into a numpy array
    og_array = np.array(list)
    # reshape the array into a 3x3 matrix
    array = np.reshape(og_array, (3, 3))

    # axis1 (cols), axis2 (rows), flattened (whole array)
    mean_cols = np.mean(array, axis=0).tolist()
    mean_rows = np.mean(array, axis=1).tolist()
  
    var_cols = np.var(array, axis=0).tolist()
    var_rows = np.var(array, axis=1).tolist()
  
    std_cols = np.std(array, axis=0).tolist()
    std_rows = np.std(array, axis=1).tolist()
    
    max_cols = np.max(array, axis=0).tolist()
    max_rows = np.max(array, axis=1).tolist()
    
    min_cols = np.min(array, axis=0).tolist()
    min_rows = np.min(array, axis=1).tolist()
    
    sum_cols = np.sum(array, axis=0).tolist()
    sum_rows = np.sum(array, axis=1).tolist()
  
    ##############################################################################
    # print the results as a dictionary
    calculations = {
      'mean': [mean_cols, mean_rows, np.mean(array)],
      'variance': [var_cols, var_rows, np.var(array)],
      'standard deviation': [std_cols, std_rows, np.std(array)],
      'max': [max_cols, max_rows, np.max(array)],
      'min': [min_cols, min_rows, np.min(array)],
      'sum': [sum_cols, sum_rows, np.sum(array)]
    }

  else:
    raise ValueError("List must contain nine numbers.")
  return calculations

print(calculate([2,6,2,8,4,0,1,5,7]))



##### why is there an error with "array" for mean, var and std?

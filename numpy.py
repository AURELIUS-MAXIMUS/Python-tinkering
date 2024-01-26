# create three new lists for height, weight and age
height = [1.82, 1.65, 1.34, 1.56, 1.82, 1.79, 1.90, 1.66]
weight = [63.5, 77.2, 81.7, 75.6, 77.9, 79.3, 82.2, 73.8]
age = [22, 21, 24, 27, 26, 29, 27, 25]
# create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
np_age    = np.array(age)
# calculate bmi
bmi = np_weight / np_height ** 2
print(bmi)

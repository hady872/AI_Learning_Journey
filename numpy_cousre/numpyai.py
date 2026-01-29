import numpy as np
numbers = np.array([1, 2, 3, 4, 5])
print(numbers)

print(numbers.dtype)
print(numbers.shape)
print(numbers +10)
print(numbers * 2)

print(numbers[0])
print(numbers[-1])

print(numbers[1:4])

print(numbers > 3)
print(numbers[numbers > 3])
reshaped = numbers.reshape(5,1)
print(reshaped)

a = np.arange(1,7)
b = a.reshape(2,3)

print(a)
print(b)
print(b.shape)

print(np.sum(b))
print(np.sum(b, axis=0))
print(np.sum(b, axis=1))

print(np.mean(b))
print(np.max(b))
print(np.min(b))
print(np.std(b))

c= b + 10
print(c)

d = np.array([1,2,3])
print(b + d)

print("--------------------------------------------")

# Day2 

# Random data
print("Day 2: Random Data")
rng = np.random.default_rng(42)
x = rng.integers(0, 101, size=(3,4))
print(x)
print(x.shape)
print(x.dtype)

print("--------------------------------------------")
#  mean and std
mean=x.mean()
std=x.std()
print("Mean:", mean)
print("Standard Deviation:", std)

print("--------------------------------------------")
# Normalization
z = (x - x.mean()) / x.std()
print("Normalized Data:")
print(z)
print("z mean:", z.mean())
print("z std:", z.std())


# Day 3: axis mean example
print("-----------------Day 3: axis mean example---------------------------")

import numpy as np
x = np.array([[10,50,30,40],
              [80,40,70,20],
              [90,100,110,120]])
print("Original array:")
print(x)

# column axis=0, row axis=1 
print("\nMean per column (axis=0):")
print(np.mean(x, axis=0))
print("\nMean per row (axis=1):")
print(np.mean(x, axis=1))

print("\nSum per column (axis=0):")
print(np.sum(x, axis=0))
print("\nSum per row (axis=1)")
print(np.sum(x, axis=1))
print("\nStd per column (axis=0)")
print(np.std(x, axis=0))
print("\nStd per row (axis=1)")
print(np.std(x, axis=1))

print("\nMean axis=0 without keepdims:")
print(np.mean(x, axis=0))
print("Shape:", np.mean(x, axis=0).shape)

print("\nMean axis=0 with keepdims:")
print(np.mean(x, axis=0, keepdims=True))
print("Shape:", np.mean(x, axis=0, keepdims=True).shape)

print("------------day 4: Normalization (z-score) ---------------------------")
import numpy as np
x= np.array([[60,90,80,70],
             [65,95,85,75],
             [50,80,70,60]])

# mean and std per column
mean = np.mean(x, axis=0, keepdims=True)
std = np.std(x, axis=0, keepdims=True)

#normalization
x_norm = (x-mean) / std

print("Original data:")
print(x)
print("\nMean:")
print(mean)
print("\nStandard Deviation:")
print(std)
print("\nNormalized data:")
print(x_norm)


# x= np.array([[60,90,80,70],
#              [65,95,85,75],
#              [50,80,70,60]])
print("--------------day 5: Min-Max Normalization----------------------")
min_val = np.min(x, axis=0, keepdims=True)
max_val = np.max(x, axis=0, keepdims=True)
x_minmax = (x-min_val) / (max_val - min_val)
print("\nMin values:")
print(min_val)
print("\nMax values:")
print(max_val)
print("\nMin-Max Normalized data:")
print(x_minmax)


print("\n--------------day 6: Indexing and Slicing--------------------------------------")
# x= np.array([[60,90,80,70],
#              [65,95,85,75],
#              [50,80,70,60]])


#Indexing: select a full row
student_1 = x[0]
print("Student number 1 scores:", student_1)
print(student_1)

#Indexing: select a full column 
subject_1 = x[:,0]
print("\nSubject number 1 scores (all students):", subject_1)
print(subject_1)


#Slicing: select first two rows
first_two_rows = x[0:2]
print("\nFirst two students' scores:")
print(first_two_rows)

#Slicing: select last two columns
last_two_columns = x[:,2:4]
print("\nScores for last two subjects (all students):")
print(last_two_columns)

#Slicing: select rows and columns together
sub_matrix = x[0:2, 0:2]
print("\nfirst two students' scores for first two subjects:")
print(sub_matrix)



print("\n--------------day 7: Feature scale--------------------------------------")
# x= np.array([[60,90,80,70],
#              [65,95,85,75],
#              [50,80,70,60]])


# Select columns to scale (first two columns)
features_to_scale = x[:, 0:2]
print("\nFeatures to scale (first two columns):")
print(features_to_scale)

min_val = np.min(features_to_scale, axis=0, keepdims=True)
max_val = np.max(features_to_scale, axis=0, keepdims=True)
scaled_features = (features_to_scale - min_val) / (max_val - min_val)
print("\nScaled features (min-max):")
print(scaled_features)


# Replace original columns with scaled ones
# Copy original data
x_scaled = x.copy()
x_scaled[:, 0:2] = scaled_features
print("\nFinal data after partial scaling:")
print(x_scaled)

print("\n--------------day 8: Boolean Indexing--------------------------------------")
# x= np.array([[60,90,80,70],
#              [65,95,85,75],
#              [50,80,70,60]])

high_scores = x[x > 70]
print("Scores greater than 70:")
print(high_scores)

# Boolean Indexing on a specific column 
mask = x[:,1] > 75
print(mask)

selected_students = x[mask]
print("\nStudents whith subject 2 score greater than 75:")
print(selected_students)

# Boolean Indexing on multiple conditions
condition = (x[:,0] > 70) & (x[:,2] > 80)
print("\nCondition (subject 1 > 70 and subject 2 > 80):")
print(condition)
filtered_students = x[condition]
print("\nFiltered students:")
print(filtered_students)

print("\n--------------day 9: Sorting and Argsort--------------------------------------")
scores = np.array([70,80,90,60])
print("Original scores:")
print(scores)
sorted_scores = np.sort(scores)
print("\nSorted scores:")
print(sorted_scores)
print("---------------")
indices = np.argsort(scores)
print("\nIndices that would sort the scores:")
print(indices)
 
print("\nSorted scores using argsort indices:")
print(scores[indices])


print("\n--------------day 10: Advanced Indexing--------------------------------------")

# Sort rows first column (subject 1 )
# x= np.array([[60,90,80,70],
#              [65,95,85,75],
#              [50,80,70,60]])


order = np.argsort(x[:,0])
print("\nOrder by subject 1: ")
print(order)
sorted_by_subject1 = x[order]
print("\nStudents sorted by subject 1 scores:")
print(sorted_by_subject1)

# another array of another degrees to understand the idea of advanced indexing
y= np.array([[60,80,80,70],
             [65,95,85,75],
             [50,90,70,60]])
order = np.argsort(y[:,0])
print("\nOrder by subject 1: ")
print(order)
sorted_by_subject1 = y[order]
print("\nStudents sorted by subject 1 scores:")
print(sorted_by_subject1)


print("\n----------------Day 11: Aggregation & Statistics---------------------------")
# x= np.array([[60,90,80,70],
#              [65,95,85,75],
#              [50,80,70,60]])

mean_per_subject = np.mean(x, axis=0)
print("Mean per subject:")
print(mean_per_subject)

mean_per_student = np.mean(x, axis=1)
print("\nMean per student:")
print(mean_per_student)

max_per_subject = np.max(x, axis=0)
print("\nMax per subject:")
print(max_per_subject)

min_per_student = np.min(x, axis=1)
print("\nMin per student:")
print(min_per_student)

print("\n----------------Day 12: Standard Deviation on axes---------------------------")

std_per_subject = np.std(x, axis=0)
print("Standard Deviation per subject:")
print(std_per_subject)
std_per_student = np.std(x, axis=1)
print("\nStandard Deviation per student:")
print(std_per_student)


# x= np.array([[60,90,80,70],
#              [65,95,85,75],
#              [50,80,70,60]])
print("\nShapes:")
print("x shape:", x.shape)
print("mean_per_subject shape:", mean_per_subject.shape)
print("mean_per_student shape:", mean_per_student.shape)
print("std_per_subject shape:", std_per_subject.shape)
print("std_per_student shape:", std_per_student.shape)

mean_cols_kd = np.mean(x, axis=0, keepdims=True)
std_cols_kd = np.mean(x, axis=0, keepdims=True)
print("\nWith keepdims:")
print("mean_cols_kd shape:", mean_cols_kd.shape)
print("std_cols_kd shape:", std_cols_kd.shape)

print("---------------------Day 13: Reshaping arrays----------------")
a = np.arange(1, 13)
print("a:")
print(a)
print("a shape:", a.shape)

b = a.reshape(3, 4)
print("\nReshape to (3, 4):")
print(b)
print("b shape:", b.shape)

# flatten: return a copy
b_flatten = b.flatten()
print("\nFlatten result:")
print(b_flatten)
print("flatten shape:", b_flatten.shape)

# ravel: returns a view when possible
b_ravel = b.ravel()

print("\nRavel result:")
print(b_ravel)
print("b_ravel shape", b_ravel.shape)


# Ravel result:
# [ 1  2  3  4  5  6  7  8  9 10 11 12]
# b_ravel shape (12,)

print("\nBefore change:")
print("b[0,0]=", b[0,0])

# change through ravel
b_ravel [0] = 999
print("\nAfter change via ravel:")
print("b_ravel[0]=",b_ravel[0])
print("b[0,0]=",b[0,0])
print("\nb matrix now:")
print(b)

# reshape with -1 (Numpy calculate the missing dimension)


# a:[ 1  2  3  4  5  6  7  8  9 10 11 12]
# a shape: (12,)

C = a.reshape(3, -1)
print("\nReshape with -1 (3, -1):")
print(c)
print("c shape:",c.shape)

# convert to column vector (n, 1)
col = a.reshape(-1, 1)
print("\nColumn vector (-1, 1):")
print(col)
print("col shape", col.shape)

print("\n--------------------------Day 14: Reshaping - clear view----------------------")
a = np. arange(1, 13)
print("\nOriginal array a:")
print(a)
# a = [ 1  2  3  4  5  6  7  8  9 10 11 12]
print("shape of a :",a.shape)
print("size of a :",a.size)

# a = [ 1  2  3  4  5  6  7  8  9 10 11 12]
b = a.reshape(3, -1)
print("\nReshape to (3, -1):")
print(b)
print("shape:",b.shape)

# a = [ 1  2  3  4  5  6  7  8  9 10 11 12]
c = a.reshape(-1,1)
print("\nReshape to column (-1, 1):")
print(c)
print("shape:", c.shape)

print("--------------------------Day 15: Element-wise vs Matrix multiplication------------------------")
A = np.array([
    [3, 2],
    [5, 4]
])

B = np.array([
    [20, 10],
    [40, 30]
])

print("\nMatrix A:")
print(A)
print("A shape:",A.shape)

print("\nMatrix B:")
print(B)
print("\nB shape:",B.shape)

A = np.array([
    [3, 2],
    [5, 4]
])

B = np.array([
    [20, 10],
    [40, 30]
])

elem_mul = A * B 
print("\nElement-wise multiplication (A * B):")
print(elem_mul)

mat_mal = A @ B 
print("\nMatrix multiplication (A @ B):")
print(mat_mal)

print("\n-------------------------Day 16: Concatenate----------------------")
A = np.array([
    [3, 2, 1]
    ,[6, 5, 4]
])

B = np.array([
    [9, 8, 7]
    ,[12, 11, 10]
])

concatenate = np.concatenate((A, B), axis=0)
print("\nConcatenate axis=0 (stack rows):")
print(concatenate)
print("Con shape:",concatenate.shape)

C1 = np.concatenate((A, B), axis=1)
print("\nConcatenate axis=1 (stack columns):")
print(C1)
print("C1 shape:",C1.shape)
print("\n-------------------------Day 17: Stack----------------------")
A = np.array([
    [3, 2, 1]
    ,[6, 5, 4]
])
B = np.array([
    [9, 8, 7]
    ,[12, 11, 10]
])
stack0= np.stack((A, B), axis=0)
print("\nStack axis=0 ")
print(stack0)
print("Stack0 shape:", stack0.shape)
stack1= np.stack((A, B), axis=1)
print("\nStack axis=1 ")
print(stack1)
print("Stack1 shape:", stack1.shape)
A = np.array([
    [3, 2, 1]
    ,[6, 5, 4]
])
B = np.array([
    [9, 8, 7]
    ,[12, 11, 10]
])
stack2 = np.stack((A, B), axis=2)
print("\nStack axis=2 ")
print(stack2)
print("Stack2 shape:", stack2.shape)


print("---------------------------Day 18: concatenate vs stack----------------------")
A = np.array([
    [3, 2, 1]
    ,[6, 5, 4]
])
B = np.array([
    [9, 8, 7]
    ,[12, 11, 10]
])
print("\nA shape:", A.shape)
print("\nB shape:", B.shape)
concat0 = np.concatenate((A, B), axis=0)
print("\nConcatenate axis=0:\n", concat0)
print("shape:", concat0.shape)
concat1 = np.concatenate((A, B), axis=1)
print("\nConcatenate axis=1:\n", concat1)
print("shape:", concat1.shape)
stack0 = np.stack((A, B), axis=0)
print("\nStack axis=0:\n", stack0)
print("shape:", stack0.shape)
stack1 = np.stack((A, B), axis=1)
print("\nStack axis=1:\n", stack1)
print("shape:", stack1.shape)
stack2 = np.stack((A, B), axis=2)
print("\nStack axis=2:\n", stack2)
print("shape:", stack2.shape)

print("---------------------------Day 19: Advanced Indexing & Boolean Masks----------------------")
scores = np.array([ [75, 70, 65]
                  ,[90, 85, 80]
                  ,[88, 90, 60]
                  ,[95, 68, 72] ])
print("\nScores array:")
print(scores)
print("Scores shape:", scores.shape)
print("\nFirst student:", scores[0])
print("\nSecond subject for all students:", scores[:,1])

mask =scores > 80
print("\nMask (scores > 80):")
print(mask)
print("\nValues greater than 80:")
print(scores[mask])

cond = (scores[:,0] > 70) & (scores[:,1] > 80)
print("\nCondition (subject 1 > 70 and subject 2 > 80):")
print(cond)
print("\nStudents matching condition:")
print(scores[cond])

# scores = np.array([ [75, 70, 65]
#                   ,[90, 85, 80]
#                   ,[88, 90, 60]
#                   ,[95, 68, 72] ])

print("\n-----------------------Real-world example: Data Cleaning---------------------")
pass_mask = scores >= 60
print("\nPass mask (scores >= 60)")
print(pass_mask)

students_pass_all = np.all(scores >= 60, axis=1)
print("\nStudents who passed all subjects:")
print(students_pass_all)

clean_scores = scores[students_pass_all]
print("\nCleaned scores (only passed students)")
print(clean_scores)

top_third_subject = scores[:,2] >= 90
print("\ntop students in subject 3 (score >= 90):")
print(top_third_subject)

print("----------------Day 20: Broadcasting---------------------")
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
x = 20
B = A + x
print("\nMatrix B:")
print(B)

print("\n----------------Day 21: View vs Copy---------------------")
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = a.copy()
b[0] = 100
print(a)
print(b)

#----------------------------------------------

a = np.array([1, 2, 3, 4, 5])
c = a.view()
c[0] = 100
print(a)
print(c)

print("\n-------------------Day 22: Min-Project------------------------------")
import numpy as np
grades = np.array([[85, 90, 78],
                   [70, 88, 92],
                   [95, 91, 89],
                   [60, 75, 70],
                   [88, 84, 90]])

student_avg = grades.mean(axis=1)
print("Student averages:")
print(student_avg)

subject_avg = grades.mean(axis=0)
print("\nSubject averages:")
print(subject_avg)

max_grades = grades.max(axis=0)
min_grades = grades.min(axis=0)
print("\nMax grades per subject:")
print(max_grades)

print("\nMin grades per subject:")
print(min_grades)

passed_students = grades[student_avg >= 80]
print("\nPassed students:\n", passed_students)
print("\n")

# grades = np.array([[85, 90, 78],
#                    [70, 88, 92],
#                    [95, 91, 89],
#                    [60, 75, 70],
#                    [88, 84, 90]])


math_scores = grades[:, 0]
math_scores [0] = 0
print(grades)
print("\n")
grades = np.array([[85, 90, 78],
                   [70, 88, 92],
                   [95, 91, 89],
                   [60, 75, 70],
                   [88, 84, 90]])

math_scores_safe = grades[:, 0].copy()
math_scores_safe[0] = 0
print(grades)

sorted_indices = np.argsort(student_avg)[::-1]
sorted_grades = grades[sorted_indices]
print("\nSorted grades by performance:", sorted_grades)
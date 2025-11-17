#q7 distribute candies equally
n = int(input("enter no of candies(n):"))
k = int(input("enter no of students(k):"))
candies_per_student = n//k
candies_left = n%k
print("each student get candies:", candies_per_student)
print("candie left:",candies_left )

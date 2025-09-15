# Create the function projectPartners with the parameter n representing the number of students in Mrs. Frizzle's class. 
# The function should return the total number of unique pairs she can make with n students.

def pairs(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count

print(pairs(4))
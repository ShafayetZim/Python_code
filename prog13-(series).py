# series 1^2+2^2+...n^2
n = int(input("Enter a number:"))
sum = 0
for z in range(1, n+1, 1):
    sum = sum + z*z
print(sum)
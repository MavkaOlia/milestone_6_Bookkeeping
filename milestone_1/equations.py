import math

# Step 1.
# Extracting the coefficients
eq = '4x^2 +4x +    (-8) =  0'
eq_new = eq.replace(' ', '').replace('(', '').replace(')', '')
a = int(eq_new[0])
b = int(eq_new[5])
c = int(eq_new[-4:-2])
print(a, b, c)

# Step 2.
# Calculate quadratic equations
x1 = int(((-b) + math.sqrt((b ** 2) - (4 * a * c)))/(2 * a))
x2 = int(((-b) - math.sqrt((b ** 2) - (4 * a * c)))/(2 * a))

print(x1, x2)   # 1 -2

num = 12345
i = 0
while num > 1:
    if num % 2 == 0:
        num = num/2
    else:
        num = (num*3) + 1
    i += 1
print(i)


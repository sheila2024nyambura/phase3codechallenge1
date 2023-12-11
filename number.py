def two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2


print(two_positive(-12, 4, -3))  # Output False
print(two_positive(4, 5, 8))     # Output False
print(two_positive(6, -8, 9))    # Output True
print(two_positive(6, 18, 9)) 
print(two_positive(6, -468, 9))
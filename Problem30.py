'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

#We know max for one digit is 9**5=59059, so the maximum
#size to check is (9**5)*6. (9**5)*7 < 1000000, so no
#seven digit number can work.
sum5 = 0
for i in range(2,6*9**5):
    s = sum([int(x)**5 for x in str(i)])
    if s == i:
        sum5+=s
print(sum5)

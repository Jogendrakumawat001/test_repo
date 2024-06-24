'''
Write a program to create a list of numbers, extract integer
 numbers from a list based on
below conditions. a. Number must be 4 digit long i.e (1000 to 9999)
b. First digit of the number must be odd and the last digit must be even.
c. Number must be divisible by either 3 or 7.
'''


def extract_number(num):
    '''extract integer numbers from a list based'''
    list_of_num = []
    for i in num:
        num_s = str(i)
        if len(num_s) == 4 and int(num_s[0]) % 2 != 0 and int(num_s[-1]) % 2 == 0:
            if (int(num_s) % 3 == 0 or int(num_s) % 7 == 0):
                list_of_num.append(i)
    return list_of_num


nums = list(map(int, input().split()))
print(extract_number(nums))
#sfsdgfdaf

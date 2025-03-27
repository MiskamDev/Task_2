# Determine the number of digits in the base-27 
# representation of the number that have a numerical 
# value greater than 9:
# 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029
#----------------------------------------------------#

n = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029

cnt = 0
while n > 0:
    if n % 27 > 9: cnt += 1
    n = n // 27
print(cnt)
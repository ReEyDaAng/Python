sum_par = 0
dob_nepar = 1

for i in range(21):
    if i % 2 == 0:
        sum_par += i
    else:
        dob_nepar *= i

print("Сума парних елементів = ", sum_par)
print("Сума непарних елементів = ", dob_nepar)

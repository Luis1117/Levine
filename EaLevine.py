import numpy as np
import matplotlib.pyplot as plt
import glob
import csv

a = glob.glob('./*K.txt')
k = np.char.replace(np.array(a), 'K.txt', '')
l = np.char.replace(k, './', '')
m = sorted(l.astype(float), key=float)

# print(m)
# guardia = []

novo02 = []
for i in range(len(a)):
    novo = []
    with open(a[i], 'r') as f:
        lol = csv.reader(f)
        for row in lol:
            novo.append(row)
    lol = novo + [l[i]]
    novo02.append(lol)

matrix = np.reshape(np.array(novo02, dtype=object), (len(a), 2))

matrix02 = np.reshape(matrix[1, 0], (501, 5))

# matrix[20, 0]
# for i in range(len(a)):
#     matrix02 = np.reshape(matrix[i, 0], (501, 5))


# print(np.r_[matrix02[5], [5, l[5]]])
array = []
for i in range(len(a)):
    matrix02 = np.reshape(matrix[i, 0], (501, 5))
    for j in range(101):
        c = (5*j)
        d = matrix02[c]
        e = np.r_[d, [i, l[i]]]
        array.append(e)

print(array[10])
# b = np.genfromtxt(a[1], dtype='str')
# c = np.genfromtxt
# c = b[1:7]
# print(type(b))

# matrix = np.array(array).astype(float)
# matrix02 = np.c_[matrix, np.log(np.abs(matrix[:, 1])), 1 / matrix[:, 3]]
# prova = np.reshape(matrix02, (57, 101, 6))

# final = []
# for i in range(100):
#     prova02 = prova[:, i][prova[:, i][:, 3].argsort()]
#     final.append(prova02)

# Ln = np.array(final)

# # for i in range(100):
# #     plt.title('Amostra 1395')
# #     plt.scatter(Ln[i][27:55, 5], Ln[i][27:55, 4])
# #     plt.xlabel("1 / Temperatura $(K^{-1})$")
# #     plt.ylabel("Ln(I-d) $(Ln(A))$")
# # plt.show()

# LnvsT = []

# for i in range(100):
#     LinearRegression = np.polyfit(Ln[i][33:47, 5],
#                                   Ln[i][33:47, 4], 1, cov=True)
#     AngCoef = LinearRegression[0][0], np.sqrt(
#         LinearRegression[1][0, 0]), -5 + 0.1*i
#     LnvsT.append(AngCoef)

# Ea = np.array(LnvsT)

# EavsV = np.c_[Ea, -Ea[:, 0]*8.61e-5, -Ea[:, 1] *
#               8.61e-5, -Ea[:, 0]*8.61e-2, -Ea[:, 1]*8.61e-2]

# x_Ea = EavsV[:, 2]
# y_Ea = EavsV[:, 5]
# Err_Y = EavsV[:, 6]

# plt.title('Amostra 1395-Modelo Levine (paso voltagem = 0.1V)')
# # plt.scatter(x_EA, y_EA, yerr=Err_Y, fmt='o')
# plt.grid(axis='both')
# plt.xlabel('Tensão (V)')
# plt.ylabel('Ea (meV)')
# plt.errorbar(x_Ea, y_Ea, yerr=Err_Y, fmt='o', color='r')
# # plt.savefig('line_plot.jpg', dpi=300)
# np.savetxt('Ea1395MelhorRes.txt', EavsV, delimiter=',')

# plt.show()

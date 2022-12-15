import numpy as np
import matplotlib.pyplot as plt
import glob
import csv

a = glob.glob('./*K.txt')
k = np.char.replace(np.array(a), 'K.txt', '')
l = np.char.replace(k, './', '')
m = sorted(l.astype(float), key=float)

# Carregando dados dos txt, usar listas é melhor para isso

novo02 = []
for i in range(len(a)):
    novo = []
    with open(a[i], 'r') as f:
        lol = csv.reader(f)
        for row in lol:
            novo.append(row)
    lol = novo + [l[i]]
    novo02.append(lol)

# Uma vez carregado pasamos para numpy array:
matrix = np.reshape(np.array(novo02, dtype=object), (len(a), 2))

# Testamos 'matrix02 = np.reshape(matrix[1, 0], (501, 5))', estamos procurando
# um paso de voltagem de 0.01 V, Agora introducimos um for para pegarmos I-d para esse paso:

array = []
for i in range(len(a)):
    matrix02 = np.reshape(matrix[i, 0], (501, 5))
    for j in range(101):
        c = (5*j)
        d = matrix02[c]
        e = np.r_[d, [j, l[i]]]
        array.append(e)

# Reajeitamos, 21 txt, 101 pontos a ler, 7 columnas:

matrix03 = np.reshape(np.array(array), (21, 101, 7))
print(matrix03[1][0][4])


# matrix = np.array(array).astype(float)
# matrix02 = np.c_[matrix, np.log(np.abs(matrix[:, 1])), 1 / matrix[:, 3]]
# prova = np.reshape(matrix02, (57, 101, 6))

# final = []
# for i in range(100):
#     prova02 = prova[:, i][prova[:, i][:, 3argsort()]
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

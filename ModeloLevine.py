import numpy as np
import matplotlib.pyplot as plt
import glob
import os


all_folders = np.sort(os.listdir())
# ['.git' '.vscode' '1395IvsV13092022' '1395IvsV26092022' '1395IvsV27092022'
#  '1395IvsV28092022' '1395IvsV29092022' 'Comparação'
#  'InformaçõesMedidas.odt' 'ModeloLevine.py' 'TesisProject']

# print(all_folders)
def cargar_dados(indice_folder):
    my_files = np.sort(glob.glob(str(all_folders[indice_folder]) + "/*.txt"))
    my_files02 = np.char.replace(np.array(my_files), '.txt', '')
    my_files03 = np.char.replace(np.array(my_files), 'K.txt', '')
    temperture02 = np.char.replace(np.array(my_files02), str(all_folders[indice_folder])+'/', '')
    temperture03 = np.char.replace(np.array(my_files03), str(all_folders[indice_folder])+'/', '')
    
    novo02 = []
    for i in range(len(my_files)):
        c = np.genfromtxt(my_files[i], dtype=float, delimiter=',')
        d = np.reshape(c, (501, 5))
        e = d, [temperture02[i]], temperture03[i]
        novo02.append(e)
    array = np.asarray(novo02, dtype=object)
    return array


a = cargar_dados(2)

if len(a) == 22:
    list = []
    for i in range(0, 22):
        if i == 0:
            list.append(a[21])
        else:
            list.append(a[i-1])
            
    arreglo = np.asarray(list, dtype=object)
    
else:
    arreglo = a

c = arreglo[:, 0]
d1 = arreglo[:, 1].tolist()
d2 = arreglo[:, 2].tolist()
e = np.vstack(d1)
f = np.reshape(e, (1, len(d1)))
g = f[0]

# print(g)

def myplot():
    for i in range(len(c)):
        d = c[i]
        e = np.c_[d, np.abs(d[:, 1])]
        plt.title('Amostra1395 \n Mesa03Terra07')
        plt.scatter(e[:, 0], e[:, 5])
        plt.yscale('log')
        plt.legend(g, prop={'size': 8})
        plt.grid(b=True, which='minor', color='b', linestyle='--')
        plt.grid(b=True, which='major', color='b', linestyle='-')
        
    plt.show()
    
# print(myplot())

# def ActivationEnergyLevine():
#     a = glob.glob('./*K.txt')
#     k = np.char.replace(np.array(a), 'K.txt', '')
#     l = np.char.replace(k, './', '')
#     m = sorted(l.astype(float), key=float)P

#     # Carregando dados dos txt, usar listas é melhor para isso

#     novo02 = []
#     for i in range(len(a)):
#         novo = []
#         with open(a[i], 'r') as f:
#             lol = csv.reader(f)
#             for row in lol:
#                 novo.append(row)
#         lol = novo + [l[i]]
#         novo02.append(lol)

#     # Uma vez carregado pasamos para numpy array:
#     matrix = np.reshape(np.array(novo02, dtype=object), (len(a), 2))

#     # Testamos 'matrix02 = np.reshape(matrix[1, 0], (501, 5))', estamos procurando
#     # um paso de voltagem de 0.01 V, Agora introducimos um for para pegarmos I-d para esse paso:

def ActivationEnergy():
    array = []
    for i in range(len(c)):
        matrix = c[i]
        for j in range(101):
            d = (5*j)
            e = matrix[d]
            f = np.r_[e, [j, d2[i]]]
            array.append(f)

    # Reajeitamos, em 21 txt, 101 pontos a ler, 7 columnas:

    matrix02 = np.reshape(np.array(array), (len(c), 101, 7)).astype(float)
    
    # graficos = []
    # for i in range(101):
    #     ordenando = matrix03[:, i][matrix03[:, i][:, 6].argsort()]
    #     ordenando02 = np.c_[ordenando, 1/ordenando[:, 6]]
    #     graficos.append(ordenando02)

    
    return matrix02[0][0]

print(len(ActivationEnergy()))

# for i in range(101):
# x =
# y =

#     fig, ax = plt.subplots()
#     fig.suptitle("Ln(I-d)vs 1/T")
#     ax.plot(x, y)

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

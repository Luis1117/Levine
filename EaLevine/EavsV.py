import numpy as np
import matplotlib.pyplot as plt
import os

path_figure = '/home/luis11/Documentos/Casa/Ea_Levine_todo.png'
# EavsV = [coef ang, erro coef ang, voltagem, Ea(eV), Erro-Ea(eV), Ea(meV), Erro-Ea(meV)]

a = np.loadtxt('EavsV_1395_Levine_07terra02corrente.txt', delimiter=',')
b = np.loadtxt('EavsV_1395_Levine_07terra03corrente.txt', delimiter=',')
c = np.loadtxt('EavsV_1395_Levine_07terra04corrente.txt', delimiter=',')
d = np.loadtxt('EavsV_1395_Levine_07terra05corrente.txt', delimiter=',')
e = np.loadtxt('EavsV_1395_Levine_07terra06corrente.txt', delimiter=',')
    
def plot_energy_activation_levine():
    
    fig, ax1 = plt.subplots()

    ax1.errorbar(a[:, 2], a[:, 5], yerr=a[:, 6], fmt='o', label='Mesa#02-Terra#07')
    ax1.errorbar(b[:, 2], b[:, 5], yerr=b[:, 6], fmt='o', label='Mesa#03-Terra#07')
    ax1.errorbar(c[:, 2], c[:, 5], yerr=c[:, 6], fmt='o', label='Mesa#06-Terra#07')
    ax1.errorbar(d[:, 2], d[:, 5], yerr=a[:, 6], fmt='o', label='Mesa#02-Terra#07')
    ax1.errorbar(e[:, 2], e[:, 5], yerr=b[:, 6], fmt='o', label='Mesa#03-Terra#07')

    ax1.set_title('Modelo Levine\n Amostra 1395')
    ax1.set_xlabel('Tensão (V)')
    ax1.set_ylabel('Ea (meV)')
    ax1.legend(prop={'size': 8})
    plt.grid(which='minor', color='#999999', linestyle='--', alpha=0.4)
    plt.grid(which='major', color='#666666', linestyle='-', alpha=0.7)
    plt.minorticks_on()
    if os.path.isfile(path_figure) == False:
        plt.savefig(path_figure, dpi=300)
        plt.show()
    else:
        plt.show()
    return

print(plot_energy_activation_levine())
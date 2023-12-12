import numpy as np
import matplotlib.pyplot as plt

# Визначаємо функцію Y(x)
def Y(x):
    return 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

# Згенеруйте значення x в інтервалі [0, 5] для побудови графіку
x_values = np.linspace(0.01, 5, 1000)  # Додатні значення x, оминання x=0 (ділення на нуль)

# Знайдимо відповідні значення y
y_values = Y(x_values)

# Побудова графіку
plt.plot(x_values, y_values, linestyle='-', color='blue', linewidth=2, label=r'$Y(x) = \frac{5 \cos(10x) \sin(3x)}{\sqrt{x}}$')

# Додавання осей
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Додавання назви графіку
plt.title('Графік функції Y(x)')

# Додавання підписів до осей
plt.xlabel('x')
plt.ylabel('Y(x)')

# Додавання легенди
plt.legend()

# Показуємо графік
plt.show()

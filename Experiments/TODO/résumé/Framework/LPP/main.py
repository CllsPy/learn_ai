# Computer Limite
# Plotar Limite

import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# LimPyPlot
class LPP(object):
    def __init__(self):
        x, y, z = symbols('x y z')
        init_printing(use_unicode=True)

    # Limits
    def compute_limite(self, fx, x, x0):
        fx = str(fx)
        x = str(x)
        exp = limit(fx, x, x0)
        print(f'O limite de {fx} quando {x} tende para {x0} é :{exp}')

    # Draw
    def draw_fx(self, fx_plot, fx):
        x_axis = np.linspace(-6, 6)
        y_axis = []
        
        for x in x_axis:
            y_axis.append(fx_plot(x))

        fig, (ax) = plt.subplots()

        # AX
        ax.plot(x_axis, y_axis)
        ax.grid(True)
        ax.set_title(f'F(x) = {(fx)}')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        plt.show()

diff = LPP()

fx, fxp = 'sin(x)/x', lambda x: sin(x)/x
x = 'x'
x0 = 0

#diff.draw_fx(fxp, fx)
diff.compute_limite(fx, x, x0)
diff.draw_fx(fxp, fx)
# -*- coding: utf-8 -*-
"""Campo_Direccional_EDO1erOrden_v4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qbzJPNCeR-Q2g3Mc6o_OWnX91_1FYBlV

#<h1 align="center"> Campos Direccionales  </h1>
 <h1 align="center"> Curvas Solución </h1>

# EDO de 1er orden
\begin{align*}
y' &= f(t, y) \\
\end{align*}
$y(t): D \subseteq \mathbb{R} ⟶ \mathbb{R}$ <br>



<br>Referencias:

  * Odubanjo, Oluwatosin (27 Dic 2021). How to Plot a Direction Field with Python -sec.6- <br> web: https://pubhtml5.com/enyy/ikvo/basic/
  * Matplotlib, Api Reference Matplotlib.pyplot.quiver
  <br> web https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html

---
Material para: FC MCA4 25-2  

Profesor: Roberto Méndez Méndez

Editado: Feb 18 25  v4

### Ejemplo 1) Campo Direccional de la EDO

\begin{equation}
    \frac{dy}{dt} = -x^2 - y(x -1)
\end{equation}
### siendo $f(x,y)= -x^2 - y(x -1)$
"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función f(x,y) [Derivada]
def f(x,y):
    return -x**2 - y*(x -1)

nx, ny = .2, .2
x = np.arange(-3, 3, nx)
y = np.arange(-2, 2, ny)

# MESHGRID
X, Y = np.meshgrid(x, y)

# Derivative
dy = f(X,Y)
dx =np.ones(X.shape)

# Normalizar
dyu = dy/np.sqrt(dx**2 + dy**2)
dxu = dx/np.sqrt(dx**2 + dy**2)

# Gráficas
plt.quiver(X,Y,dxu,dyu, color = "orange",  headwidth = 2)
plt.xticks(x, rotation = 60)
plt.yticks(y)
plt.title("Directional Field y' = -x**2 -(x -1)*y", color='blue',
              fontsize ='x-large')
plt.show()

"""### Ejemplo 2) Campo Direccional de la EDO

\begin{equation}
\frac{dy}{dt} = -\frac{y}{x} - \frac{1}{x^2}
\end{equation}
### siendo f(x,y)= -y/x - 1/x**2
"""

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función f(x,y) [Derivada]
def f(x,y):
    return -y/x - 1/x**2

#nx, ny = .3, .3
nx, ny = .2, .2
x = np.arange(-3, 3, nx)
y = np.arange(-2, 2, ny)

# MESHGRID
X, Y = np.meshgrid(x, y)

# Derivative
dy = f(X,Y)
dx =np.ones(X.shape)

# Normalizar
dyu = dy/np.sqrt(dx**2 + dy**2)
dxu = dx/np.sqrt(dx**2 + dy**2)

# Gráficas
plt.quiver(X,Y,dxu,dyu, color = "orange",  headwidth = 2)
plt.xticks(x, rotation = 60)
plt.yticks(y)
plt.title("Directional Field y' = -y/x - 1/x**2", color='blue', fontsize ='x-large')
plt.show()

"""### Ejemplo 3) Campo Direccional de la EDO

\begin{equation}
\frac{dy}{dt} = \frac{x^2 + y^3}{xy^2}
\end{equation}
### siendo f(x,y)= (x^2 + y^3)/(xy^2)
---
Editado: 9 Feb 25

"""

import numpy as np
import matplotlib.pyplot as plt


# Definicónde la Derivada
def f(x,y):
    return (x**2 + y**3)/(x*y**2)

#nx, ny = .3, .3
nx, ny = .2, .2
x = np.arange(-3, 3, nx)
y = np.arange(-2, 2, ny)

# MESHGRID
X, Y = np.meshgrid(x, y)

# Derivative
dy = f(X,Y)
dx =np.ones(X.shape)

# Normalizar
dyu = dy/np.sqrt(dx**2 + dy**2)
dxu = dx/np.sqrt(dx**2 + dy**2)

# Gráficas
plt.quiver(X,Y,dxu,dyu, color = "orange",  headwidth = 2)
plt.xticks(x, rotation = 60)
plt.yticks(y)
plt.title("Directional Field y' = (x**2 + y**3)/(x*y**2)", color='blue',
          fontsize ='x-large')
plt.show()

"""### Ejemplo 2) EDO separable

\begin{equation}
\frac{dy}{dt} = \frac{4 - 2x}{3y^2 - 5}
\end{equation}
### Campo Direccional y Curvas Solución

Referencia:
* Edwards & Penney (2015). Differential Equations and Boundary Value Problems, 5th edition, Pearson. pag. 32

---
Editado: 10 Feb 25
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definicónde la Derivadak
def f(x,y):
    return (4 - 2*x)/(3*y**2 - 5)

#  nx, ny = .3, .3
nx, ny = .3, .3
x = np.arange(-2, 5, nx)
y = np.arange(-3, 3, ny)

# MESHGRID
X, Y = np.meshgrid(x, y)

# Derivative
dy = f(X,Y)
dx =np.ones(X.shape)

# Normalización
dyu = dy/np.sqrt(dx**2 + dy**2)
dxu = dx/np.sqrt(dx**2 + dy**2)

# Solución con odeint
steps = 50
t1 = np.linspace(0,4, steps)
sol1 = odeint(f, [1.3], t1, tfirst=True)
y0 = 1.2
t2 = np.linspace(0,4,steps)
sol2 = odeint(f, y0, t2, tfirst=True)

t3 = np.linspace(-0.8,4.6,steps)
sol3 = odeint(f, -2.6, t3, tfirst=True)

# Gráfica Directional Field
plt.quiver(X,Y,dxu,dyu, color = "orange",  headwidth = 2)

# Grafica Curvas Integrales
plt.plot(t1, sol1, color='red')
plt.plot(t2, sol2, color='red')
plt.plot(t3, sol3, color='red')

plt.xticks(x, rotation = 60, fontsize=8 )
plt.yticks(y, fontsize=8 )
plt.title("Directional Field y' = (4 - 2x)/(3y^2 - 5)", color='blue',
          fontsize ='x-large')
plt.show()

"""Gráficas de las soluciones implícitas

\begin{equation}
y^3 - 5y = 4x - x^2 + C
\end{equation}
de la EDO separable

\begin{equation}
\frac{dy}{dt} = \frac{4 - 2x}{3y^2 - 5}
\end{equation}

Referencia:
* Edwards & Penney (2015). Differential Equations and Boundary Value Problems, 5th edition, Pearson. pag. 32

---
Editado: 10 Feb 25
"""



from sympy import symbols, Eq
from sympy import plot_implicit
import math

x, y = symbols('x y')

# Gráfica de todas separadas
p1 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, -6), (x, -2, 6),
              (y, -3, 3), line_color = 'darkgoldenrod',
               title = "y^3 - 5y + x^2  - 4x = -6 ",
               fontsize = 'medium');
p2 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, 0), (x, -2, 6),
              (y, -3, 3), line_color = 'darkorange',
               title = "y^3 - 5y + x^2  - 4x = 0 ",
               fontsize = 'medium');
p3 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, .5), (x, -2, 6),
              (y, -3, 3), line_color = 'olivedrab',
               title = "y^3 - 5y + x^2  - 4x = 0.5 ",
               fontsize = 'medium');
p4 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, 6), (x, -2, 6),
              (y, -3, 3), line_color = 'crimson',
               title = "Gráficas de la soución  y^3 - 5y + x^2  - 4x = 6 ",
               fontsize = 'medium');

# Gráfica de todas juntas
p5 = plot_implicit(Eq(y, math.sqrt(5/3)), (x, -2, 6),
              (y, -3, 3), line_color = 'black', show=False);
p6 = plot_implicit(Eq(y, -math.sqrt(5/3)), (x, -2, 6),
              (y, -3, 3), line_color = 'black', show=False);
p7 = plot_implicit(Eq(y**3 - 5*y + x**2  - 4*x, -6), (x, -2, 6),
              (y, -3, 3), line_color = 'darkgoldenrod',
               title = "Gráficas de la solución  y^3 - 5y + x^2  - 4x = c ",
               fontsize = 'medium', show=False);
p7.append(p2[0])
p7.append(p3[0])
p7.append(p4[0])
p7.append(p5[0])
p7.append(p6[0])
p7.show()

"""# Logistic Model (ODE)

In 1838, Pierre-Francois
Verhulst argued that the growth rate should depend on the population
level, which implicitly assumes dependence on resource.If the population is low the rate of growth is positive and if it is high the rate is
negative.Verhulst proposed the differential equation, which he termed
the logistic equation,

\begin{align*}
\frac{dy}{dt} &= r\left(1 - \frac{P}{K}\right)P \\
& = g(P;r,K)P
\end{align*}

where $K > 0$ is the "carrying capacity" and $r > 0$ "growth rate", both constants. In this case we think of the growth rate as $g(P;r, k)$ as a function of the
populations rather than a constant as Malthus did. <br>
The Analitic Solution of this ODE with the  initial conditions  $P(t_0) = P_0$, is <br/>

\begin{equation*}
P(t) = \frac{KP_0}{P_0 + (K - P_0)e^{r(t_0 - t)}}
\end{equation*}

---

References:

* Mathematical Modeling the Life Sciences Numeric Python y Matlab  2023 Cogan
 pág. 53.  (Texto histórico)
* Mathematical Analysis of Infectious Diseases 2022 ed  Agarwal Nieto pág. 5 (solución analítica de la logística con $t_0 = 0$)

---

Created: Feb 18 2025
Edited: Feb 20 2'25
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
K=2
r=1

# Model
def f(x,y):
    return r*y*(1 - y/K)

nx, ny = .2, .2
x = np.arange(-3, 3, nx)
y = np.arange(-2, 4, ny)

# MESHGRID
X, Y = np.meshgrid(x, y)

# Derivative
dy = f(X,Y)
dx =np.ones(X.shape)

# Normalizar
dyu = dy/np.sqrt(dx**2 + dy**2)
dxu = dx/np.sqrt(dx**2 + dy**2)

# Gráficas
plt.quiver(X,Y,dxu,dyu, color = "orangered",  headwidth = 2)
plt.axhline(y = K, color = 'dodgerblue', linestyle = '-')
plt.axhline(y = 0, color = 'purple', linestyle = '-')
plt.xticks(x, rotation = 60, fontsize=7)
plt.yticks(y, fontsize=7 )
plt.title("Directional Field P' = r(1 - P/k)P", color='blue',
          fontsize ='x-large')
plt.show()
# -*- coding: utf-8 -*-
"""MN_Euler_Explícito_v4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15ps5SfizdPKVkzM2Bz--giRxjPmMGBe-

# <h1 align="center"> Euler Explícito </h1>

## Dada la EDO con condiciones de Cauchy  
\begin{align*}
y' &= f(t, y) \\
y(t_0) &= y_0
\end{align*}
## La solución numérica de y(t) se calcula mediante
\begin{align*}
y_i &= y_{i-1} + hf(t_{i-1}, y_{i-1}) \\
\end{align*}
## con *h* el tamaño de paso, $i = 1,2, … , n$

---

Autor: Roberto Méndez Méndez

Editado: 26 Ago 24 <br>
&emsp; &emsp; &emsp;  10 Oct 24 v4

-------------------------------------------------------------------------

### Caso 1.1) Solución númerica de la EDO

\begin{align}
\frac{dy}{dt} &= -cy \\
y(t_0) &= y_0
\end{align}
Este problema de Cauchy tiene como solución analítica
\begin{equation*}
y(t) =y_0e^{c*t_0}*e^{-ct}
\end{equation*}
### Para la sustitución numérica
\begin{align*}
f(t,y) &= -cy,\\
t_0 &= t_0 \hspace{.7cm} \\
y_0 &= y(t_0)
\end{align*}
### el método de Euler toma la forma
\begin{equation}
y_i = y_{i-1} - h*c*y_{i-1}
\end{equation}
con $i \in \{1, 2, 3, \ldots, n\}$
"""



import numpy as np
import matplotlib.pyplot as plt

t0 = 1
tf = 6
y0 = 2
c = 1
h = 0.1
t = np.arange(t0, tf, h)

y = np.zeros(len(t))
y[0] = y0

# MN Euler
for i in range(len(t) - 1):
    y[i+1] = y[i] - h*c*y[i]

# Solución analítica
solExac = y0*np.exp(c*t0)*np.exp(-c*t)


# Gráficas
plt.plot(t, y, 'green', linestyle="-", linewidth=3 )
plt.plot(t, solExac, 'orange', linestyle="--", linewidth=2)
plt.xlabel('t')
plt.ylabel('y_n')
plt.legend(['Euler', 'Analítica'] )
plt.show()

"""### Caso 1.2) Solución númerica de la EDO

\begin{align}
\frac{dy}{dt} &= -cy \\
y(t_0) &= y_0
\end{align}
Este problema de Cauchy tiene como solución analítica
\begin{equation*}
y(t) =y_0e^{c*t_0}*e^{-ct}
\end{equation*}
### Para la sustitución numérica
\begin{align*}
f(t,y) &= -cy,\\
t_0 &= t_0 \hspace{.7cm} \\
y_0 &= y(t_0)
\end{align*}
### el método de Euler toma la forma
\begin{equation}
y_i = y_{i-1} - h*c*y_{i-1}
\end{equation}
con $i \in \{1, 2, 3, \ldots, n\}$
### que simplificado algebraicamente es:
\begin{equation}
y_i = y_0(1 - h*c)^i
\end{equation}

"""

import numpy as np
import matplotlib.pyplot as plt

t0 = 1
tf = 6
y0 = 2
c = 1
h = 0.01
t = np.arange(t0, tf, h)

# MN Euler
i = np.arange(0,len(t))
yn = y0*(1 - h*c)**i

# Solución analítica
solExac = y0*np.exp(c*t0)*np.exp(-c*t)

# Gráficas
plt.plot(t, yn, 'green', linestyle="-", linewidth=3 )
plt.plot(t, solExac, 'orange', linestyle="--", linewidth=2)
plt.xlabel('t')
plt.ylabel('y_n')
plt.legend(['Euler', 'Analítica'] )
plt.show()

"""### Caso 1.3) **Inestabilidad en la solución númerica de la EDO**

\begin{align}
\frac{dy}{dt} &= -cy \\
y(t_0) &= y_0
\end{align}
Este problema de Cauchy tiene como solución analítica
\begin{equation*}
y(t) =y_0e^{c*t_0}*e^{-ct}
\end{equation*}
### Para la sustitución numérica
\begin{align*}
f(t,y) &= -cy,\\
t_0 &= t_0 \hspace{.7cm} \\
y_0 &= y(t_0)
\end{align*}
### y el método de Euler toma la forma
\begin{equation}
y_i = y_{i-1} - h*c*y_{i-1}
\end{equation}
con $i \in \{1, 2, 3, \ldots, n\}$

### Utilizando los valores <br> c= 15, $t_0 = 0$, $y_0 = 1$, $h = 0.1$
"""

import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf = 1.5
y0 = 1
c = 15
h = 0.1
t = np.arange(t0, tf, h)

y = np.zeros(len(t))
y[0] = y0

# MN Euler
for i in range(len(t) - 1):
    y[i+1] = y[i] - h*c*y[i]

# Solución analítica
solExac = y0*np.exp(c*t0)*np.exp(-c*t)


# Gráficas
plt.plot(t, y, 'green', linestyle="-", linewidth=3 )
plt.plot(t, solExac, 'orange', linestyle="--", linewidth=2)
plt.xlabel('t')
plt.ylabel('y_n')
plt.legend(['Euler', 'Analítica'] )
plt.show()
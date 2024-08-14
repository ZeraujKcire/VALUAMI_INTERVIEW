
# === EJERCICIO === (((
# 3. Hacer un código de Python que genere 53 puntos con coordenadas aleatorias 
#    entre 3 y 133, calcule los parámetros de la recta de regresión por mínimos 
#    cuadrados  y haga la gráfica de los puntos y la recta
# )))

# === MODULOS === (((
import numpy as n # para el sub-modulo n.random
import matplotlib.pyplot as plt # para graficacion
# )))

# === PARAMETROS === (((
N = 53
a = 3
b = 133
# )))

# === PUNTOS === (((
x = n.random.randint(a,b,size=N)
y = n.random.randint(a,b,size=N)
# )))

# === REGRESION LINEAL === (((
x_sum = float(sum(x)) # float64
y_sum = float(sum(y)) # float64

# Calculo de covarianzas. (suma de cuadrados)
s_xy = sum(x*y) - x_sum*y_sum/N # cov(x,y)
s_xx = sum(x*x) - x_sum*x_sum/N # cov(x,x) = var(x)
s_yy = sum(y*y) - y_sum*y_sum/N # cov(y,y) = var(y)

# Coef. de correlación lineal de Pearson.
r = s_xy/(n.sqrt(s_xx)*n.sqrt(s_yy))

# Coeficientes de recta de regresion
# Y = B_0 + B_1X + E. (E es el error total).
B_1 = s_xy/s_xx
B_0 = y_sum/N - B_1*x_sum/N
y_fit = B_0 + B_1*x
# )))

# === GRAFICACION === (((
plt.scatter(x,y,color='blue',s=20,marker = 'o')
plt.plot(x,y_fit,color='red')
plt.savefig("Linear_regression.pdf", format="pdf", bbox_inches="tight")
plt.show()
# )))

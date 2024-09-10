import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

### O código a seguir traça parte da trajetória seguida pela formiga 3 no sentido horário de movimento com v=5.
### Nesse código é utilizado a forma polar descoberta na primeira solução.

##############Configurações#################

v=5
a=15 #Tamanho do lado do triangulo inicial
e = 0.00001 #Passo




def angulo(a,v,t):
	theta = -0.523598-0.577350269*np.log(0.57735*a-0.866025*v*t)+0.577350269*np.log(0.57735*a)
	return theta

def raio(a,v,t):
	r = a*0.57735-0.866025*v*t
	return r

def trajetoria(a,e,v):
	distancia = 0 # Aqui é calculado a distancia infinitesimal a cada passo

	nd = 0 #Variável ant-bug

	y = [-0.288675134*a] #Valor inicial de y, dado a posição da formiga 3
	x = [a/2] #Valor inicial de x

	t=e

	r_now = 8.66025
	theta_now = -0.523598
	while r_now >=0:
		r_now = raio(a,v,t)
		theta_now = angulo(a,v,t)
		y.append(r_now*np.sin(theta_now))
		x.append(r_now*np.cos(theta_now))

		nd = distancia + np.sqrt((x[-1]-x[-2])**2 + (y[-1]-y[-2])**2)
		try:
			if nd > distancia:
				distancia = nd
		except:
			pass

		print(distancia)
		t=t+e

	nd = distancia

	print("Distância percorrida: %s"%(str(round(distancia, 3))))
	# Criar o gráfico
	plt.plot(x, y, marker='o') #'marker' adiciona marcadores nos pontos
	plt.xlabel('x') #Rótulo do eixo x
	plt.ylabel('y') #Rótulo do eixo y
	plt.suptitle('Trajetória da formiga 3') #Título do gráfico
	plt.title('Distância percorrida: %s'%(str(round(distancia, 3)))) #Subtítulo do gráfico
	plt.grid(True) #Adiciona uma grade ao gráfico
	plt.show() #Exibe o gráfico


trajetoria(a,e,v)

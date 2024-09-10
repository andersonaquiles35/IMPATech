import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

### O código a seguir traça parte da trajetória seguida pela formiga 3 no sentido anti-horário
### Aqui é descrito pela segunda forma comentada na solução da questão

##############Configurações#################

a=15 #Tamanho do lado do triangulo inicial
e = 0.00001 #Passo





def trajetoria(a,e):
	distancia = 0 # Aqui é calculado a distancia infinitesimal a cada passo

	y = [-0.288675134*a] #Valor inicial de y, dado a posição da formiga 3
	x = [a/2] #Valor inicial de x

	t = np.arctan(-y[-1]/x[-1]) #Angulo inicial, esse t representa o theta

	while t <= 1.5706: # Primeira iteração
		dyx = np.tan(t-np.radians(30))
		if dyx < 0:
			dyx = dyx*(-1)

		x.append(x[-1]-e)
		y.append(dyx*e+y[-1])
		t = np.arctan(-y[-1]/x[-1])
		if t < 0:
			t = t*(-1)

		distancia = distancia + np.sqrt((x[-1]-x[-2])**2 + (y[-1]-y[-2])**2)

	# Resetamos tudo e recomeçamos aqui, pois isso nao é uma função!!!
	t = 0
	ny = y[-1]
	if ny > 0:
		ny = ny*(-1)
	y.append(ny)
	x.append(0)

	while t <= 0.523598775: # Segunda iteração
		dyx = np.tan(t+np.radians(60))
		if dyx < 0:
			break
		x.append(x[-1]-e)
		y.append(dyx*e+y[-1])
		t = np.arctan(x[-1]/y[-1])
		if t < 0:
			t = t*(-1)
		distancia = distancia + np.sqrt((x[-1]-x[-2])**2 + (y[-1]-y[-2])**2)



	t = 0.523598775 # Resetar

	while t <= 3*0.523: # Terceira iteração
		dyx = np.tan(t-np.radians(30))
		y.append(y[-1]+e)
		x.append(e*dyx+x[-1])
		t = np.arctan(-x[-1]/y[-1])
		if t < 0:
			t = t*(-1)
		distancia = distancia + np.sqrt((x[-1]-x[-2])**2 + (y[-1]-y[-2])**2)




	nx = x[-1] # Resetar
	if nx > 0:
		nx = nx*(-1)

	x.append(nx)
	y.append(0)

	t = np.arctan(-y[-1]/x[-1])

	while t <= 0.523598: # Quarta iteração
		dyx = np.tan(np.radians(30)-t)
		if dyx < 0:
			dyx = dyx*(-1)

		x.append(x[-1]+e)
		y.append(dyx*e+y[-1])
		t = np.arctan(-y[-1]/x[-1])
		if t < 0:
			t = t*(-1)
		distancia = distancia + np.sqrt((x[-1]-x[-2])**2 + (y[-1]-y[-2])**2)




	print("Distância percorrida: %s"%(str(round(distancia, 3))))
	# Criar o gráfico
	plt.plot(x, y, marker='o') #'marker' adiciona marcadores nos pontos
	plt.xlabel('x') #Rótulo do eixo x
	plt.ylabel('y') #Rótulo do eixo y
	plt.suptitle('Trajetória da formiga 3') #Título do gráfico
	plt.title('Distância percorrida: %s'%(str(round(distancia, 3)))) #Subtítulo do gráfico
	plt.grid(True) #Adiciona uma grade ao gráfico
	plt.show() #Exibe o gráfico


trajetoria(a,e)

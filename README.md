# Reto1-Python
Optimizando la producción

En una empresa de confitería se fabrican diferentes tipos de dulces, al final del día el controlador de la operación debe reportar las cajas entregadas al área de bodegaje en el orden de recepción, para lo cual debe utilizar la letra inicial del nombre del producto. Por ejemplo:

 

Chocolatina

Frunas

Frunas

Frunas

Gomitas

Gomitas

Frunas

Arequipe

 

Entonces el controlador de la operación reportará lo siguiente: C F F F G G F A (tenga en cuenta que las letras están separadas por un espacio).

 

Como la empresa fue creciendo su producción, la cantidad de cajas producidas por día se incrementó exponencialmente, y el controlador debía calcular la cantidad de cajas recibidas de forma consecutiva para cada producto. Por lo tanto, los dueños de la empresa decidieron construir un software que realice el conteo de forma automática, el cual deberá imprimir las letras iniciales de los nombres de los productos en la primera línea, y en la segunda el conteo de cajas recibidas de forma consecutiva para cada producto. Para el ejemplo, la salida sería: (Tenga en cuenta que el separador de letras debe ser UN espacio, igualmente para los números del conteo de la fila dos)

 

Entrada

C F F F G G F A

Salida

C     F     G    F     A

1     3     2    1     1

 

 

Ejemplos

 

Entrada

Salida

K K K K O O O U U B M T T G D K K G G G

K O U B M T G D K G

4 3 2 1 1 2 1 1 2 3

W W W W Z Z Z Z P P S S S S Q Q Q Q R R R R E E E O O N N N

W Z P S Q R E O N

4 4 2 4 4 4 3 2 3

M M M M S S S S B C C C H H B H H H H J J J N N N Q Q

M S B C H B H J N Q

4 4 1 3 2 1 4 3 3 2


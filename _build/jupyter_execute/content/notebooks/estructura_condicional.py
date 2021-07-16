#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
# Run and print a shell command.
def run(cmd):
    print('>> {}'.format(cmd))
    get_ipython().system("{cmd}  # This is magic to run 'cmd' in the shell.")
def compile(nombre_clase):
    #run('javac {}.java'.format(nombre_clase))
    javaFile = nombre_clase + ".java"
    os.system("javac " + javaFile)

def execute(nombre_clase):    
    # os.system("java " + nombre_clase)
    run('java {}'.format(nombre_clase))
    
def ejecutar(nombre_clase):
    compile(nombre_clase)
    execute(nombre_clase)


# In[2]:


run("java -version")


# # Estructuras de selección en java

# ## Recordando el tema anterior
# 
# En las secciones anteriores se estudió todo aquello relacionado a la creación de programas sencillos, los tipos de datos, los tipos de operadores y las instrucciones de entrada y salida. Recuerde los métodos de la clase ```Scanner``` mostrados en la siguiente tabla:
# 
# |Tipo|Método|
# |:---|:---|
# |```byte```|```nextByte```|
# |```short```|```nextShort```|
# |```int```|```nextInt```|
# |```long```|```nextLong```|
# |```float```|```nextFloat```|
# |```double```|```nextDouble```|
# |```boolean```|```nextBoolean```|
# |```String```|```nextString```|
# 
# A modo de repaso vamos a realizar el siguiente ejemplo:
# 
# **Ejemplo 1**: Hacer un programa que solicite una candidad de segundos y retorne una salida en la que se muestre la cantidad de minutos y segundos restantes asociados. A continuación se muestra un caso de uso cuando la cantidad de segundos ingresada es de ```500```:
# 
# ```bash
# Digite la cantidad de segundos: 500
# 500 segundos equivale a 8 minutos y 20 segundos
# ```
# 
# **Solución en Python**

# In[ ]:


seconds = int(input("Digite la cantidad de segundos: "))
minutes = seconds//60
remainingSeconds = seconds%60
print(str(seconds) + " segundos equivale a 8 minutos " + str(minutes) 
      + " minutos y " + str(remainingSeconds) + " segundos")


# **Solución en Java**

# In[5]:


get_ipython().run_cell_magic('writefile', 'DisplayTime.java ', 'import java.util.Scanner;\n\npublic class DisplayTime {\npublic static void main(String[] args) {\n    Scanner input = new Scanner(System.in);\n\n    System.out.print("Enter an integer for seconds: ");\n    int seconds = input.nextInt();\n    int minutes = seconds/60; \n    int remainingSeconds = seconds%60; \n    System.out.println(seconds + " seconds is " + minutes +\n                       " minutes and " + remainingSeconds + " seconds");\n    }\n}')


# In[6]:


compile("DisplayTime")


# In[ ]:


# Solo sirve online
execute("DisplayTime")


# ## Introducción
# 
# Para aquellos problemas en los cuales se hace necesario elegir entre dos o mas posibilidades se usa la estructura **condicional**. En una estructura condicional el flujo de ejecución del programa depende de operaciones cuyo resultado es **booleano** (```true``` o ```false```) por lo que a modo de repaso mostramos lo diferentes operadores tanto en python como en java:
# * **Operadores relacionales**:
# 
# |Python|Java|
# |:---|:---|
# |```>```|```>```|
# |```<```|```<```|
# |```>=```|```>=```|
# |```<=```|```<=```|
# |```==```|```==```|
# |```!=```|```1=```|
# 
# 
# * **Operadores lógicos**:
# 
# |Python|Java|
# |:---|:---|
# |```and```|```&``` o ```&&```|
# |```or```|```\|``` o ```\|\|```|
# |```not```|```!```|
# 
# 
# La teniendo en cuenta lo anterior, la siguiente tabla muestra algunos casos en los cuales se muestran expresiones logicas implementadas en **python** y **Java**:
# 
# |Enunciado en palabras | Python | Java |
# |:---|:---|:---|
# |Sea ```pob``` una variable asociada a la población escriba <br>la condición que indique si la población es menor que  ```10000000```|```pob < 10000000```|```pob < 10000000```|
# |Teniendo en cuenta la variable ```pob``` asociada a la <br>población, una condición que muestre que la población <br>se encuentra entre ```10000000``` y ```35000000``` incluidos|```10000000 <= pob <= 35000000```|```(pob >= 10000000) && (pob <= 35000000)```|
# |Sea ```num``` una variable que guarda un numero. ¿Cual es <br>la condición para indicar que el numero es positivo?|```num >= 0```|```num >= 0```|
# |Sea ```num``` una variable que guarda un numero. ¿Cual es <br>la condición para indicar que el numero es par?|```num%2 == 0```|```num%2 == 0```|
# |Sea ```num``` una variable que guarda un numero. <br>¿Cual es la condición para indicar que el numero es <br>multiplo de ```2```, ```3``` y ```5```?|```(num%2 == 0) and (num%3 == 0) and (num%5 == 0)```|```(num%2 == 0) && (num%3 == 0) && (num%5 == 0)```|

# ## Tipos de condicionales
# 
# En lo que respecta las estructuras condicionales se manejan tres tipos:
# 1. Condicional simple.
# 2. Condicional doble.
# 3. Condicional multiple.
# 4. Estructura switch.
# 
# 
# ### 1. Condicional simple.
# 
# Esta es la forma mas simple de la estructura condicional. Para este caso solo hay ejecución de las instrucciones cuando la condición es verdadera. La forma se muestra en la siguiente figura:
# 
# ![if](condicionales/if.jpg)
# 
# A continuación se muestra una comparación de la sintaxis de java con la de python:
# 
# |Lenguaje|Sintaxis|
# |:---|:---|
# |Python|```if condicion:```<br>&nbsp;&nbsp;&nbsp;```#Instruciones verdadero```<br>&nbsp;&nbsp;&nbsp;```instruccion 1```<br>&nbsp;&nbsp;&nbsp;```instruccion 2```<br>&nbsp;&nbsp;&nbsp; ```...```&nbsp;&nbsp;&nbsp;<br>```  instruccion N```|
# |Java|```if (condicion) {```<br>&nbsp;&nbsp;&nbsp;```//Instruciones verdadero```<br>&nbsp;&nbsp;&nbsp;```instruccion 1```<br>&nbsp;&nbsp;&nbsp;```  instruccion 2```<br>&nbsp;&nbsp;&nbsp; ```  ...```<br>&nbsp;&nbsp;&nbsp;```  instruccion N```<br>```}```|
# 
# Para comprender el uso de estructuras condicionales en python, observemos el siguiente ejemplo.

# **Ejemplo 1**
# Hacer un programa que solicite el valor de un producto de tal manera que si su valor es mayor o igual a 1000000, se le hace un incremento por IVA del 19 %.
# 
# **Código python**

# In[ ]:


IVA = 0.19
imp = 0

# Entrada de datos
precio_base = int(input("Ingrese el precio del articulo: $"))

# Calculo del impuesto y el precio neto
if precio_base >= 1000000:
    imp = IVA*precio_base
precio_neto = precio_base + imp

# Despliegue de los resultados
print()
print("******** Colilla de pago ********")
print("+ Subtotal -> ", precio_base)
print("+ Impuesto -> ", imp)
print("---------------------------------")
print("+    Total -> ",precio_neto)
print("*********************************")


# **Código java**
# 
# ```java
# import java.util.Scanner;
# 
# public class ArticuloIVA {
#     public static void main(String[] args) {
#         // Variables
#         final float IVA = 0.19f;
#         float imp = 0;
#         float precioBase;
#         float precioNeto;
#         
#         // Objeto tipo Scanner
#         Scanner in = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner
#         
#         // Entrada de datos
#         System.out.print("Ingrese el precio del articulo: ");
#         precioBase = in.nextFloat();    
#         
#         // Calculo del impuesto y el precio neto
#         if (precioBase >= 1000000) {
#             imp = IVA*precioBase;
#             precioNeto = preciBase + imp;
#         }
#         // Despliegue de los resultados
#         System.out.println();
#         System.out.println("******** Colilla de pago ********");
#         System.out.println("+ Subtotal -> " + precioBase);
#         System.out.println("+ Impuesto -> " + imp);
#         System.out.println("---------------------------------");
#         System.out.println("+    Total -> " + precioNeto);
#         System.out.println("*********************************");
#     }
# }
# ```

# In[ ]:


get_ipython().run_cell_magic('writefile', 'ArticuloIVA.java ', 'import java.util.Scanner;\n\npublic class ArticuloIVA {\n    public static void main(String[] args) {\n        // Variables\n        final float IVA = 0.19f;\n        float imp = 0;\n        float precioBase;\n        float precioNeto;\n\n        // Objeto tipo Scanner\n        Scanner in = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner\n\n        // Entrada de datos\n        System.out.print("Ingrese el precio del articulo: ");\n        precioBase = in.nextFloat();    \n\n        // Calculo del impuesto y el precio neto\n        if (precioBase >= 1000000) {\n            imp = IVA*precioBase;\n            precioNeto = preciBase + imp;\n        }\n        // Despliegue de los resultados\n        System.out.println();\n        System.out.println("******** Colilla de pago ********");\n        System.out.println("+ Subtotal -> " + precioBase);\n        System.out.println("+ Impuesto -> " + imp);\n        System.out.println("---------------------------------");\n        System.out.println("+    Total -> " + precioNeto);\n        System.out.println("*********************************");\n    }\n}')


# In[ ]:


run('java -version')


# ### 2. Condicional simple.
# 
# En este tipo de estructura condicional es la forma mas comúnmente usada. Para este caso se manejan dos alternativas de ejecución dependiendo del resultado de evaluar la condición. 
# 
# ![if-else](condicionales/if-else.jpg)
# 
# A continuación se muestra una comparación de la sintaxis de java con la de python:
# 
# |Lenguaje|Sintaxis|
# |:---|:---|
# |Python|```if condicion:```<br>&nbsp;&nbsp;&nbsp;```#Instruciones verdadero```<br>&nbsp;&nbsp;&nbsp;```instruccion 1```<br>&nbsp;&nbsp;&nbsp;```instruccion 2```<br>&nbsp;&nbsp;&nbsp; ```...```<br>&nbsp;&nbsp;&nbsp;```  instruccion N```<br>```else:```<br>&nbsp;&nbsp;&nbsp;```#Instruciones falso```<br>&nbsp;&nbsp;&nbsp;```instruccion 1```<br>&nbsp;&nbsp;&nbsp;```instruccion 2```<br>&nbsp;&nbsp;&nbsp; ```...```<br>&nbsp;&nbsp;&nbsp;```  instruccion M```|
# |Java|```if (condicion) {```<br>&nbsp;&nbsp;&nbsp;```// Instruciones verdadero```<br>&nbsp;&nbsp;&nbsp;```instruccion 1```<br>&nbsp;&nbsp;&nbsp;```  instruccion 2```<br>&nbsp;&nbsp;&nbsp; ```  ...```<br>&nbsp;&nbsp;&nbsp;```  instruccion N```<br>```}```<br>```else {```<br>&nbsp;&nbsp;&nbsp; ```//Instruciones falso```<br>&nbsp;&nbsp;&nbsp;```instruccion 1```<br>&nbsp;&nbsp;&nbsp;```instruccion 2```<br>&nbsp;&nbsp;&nbsp; ```...```<br>&nbsp;&nbsp;&nbsp;```  instruccion M```<br>```}```|
# 
# Para comprender el uso de la estructura anterior, miremos el siguiente ejemplo.

# **Ejemplo 2**:
# 
# Hacer solicite el nombre y la edad de una persona e indique si esta es mayor o menor de edad.
# 
# **Código python**

# In[ ]:


# Entrada de datos
nom = input('-> Digite su nombre por favor: ')
edad = int(input('-> Digite su edad por favor: '))

# Validación de la edad
if edad >= 18:
    print(nom + " usted es un anciano")
else:
    print(nom + " usted es un culicagao")


# **Código java**
# 
# ```java
# import java.util.Scanner;
# 
# public class Edad {
#     public static void main(String[] args) {
#         // Variables
#         String nom;
#         int edad;
# 
# 
#         // Objeto tipo Scanner
#         Scanner input = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner
# 
#         // Entrada de datos
#         System.out.print("-> Digite su nombre por favor: ");
#         nom = input.next(); 
#         System.out.print("-> Digite su edad por favor: ");
#         edad = input.nextInt();
#         
#         System.out.println();
#         // Validación de la edad
#         if (edad >= 18) {
#             System.out.println(nom + " usted es un anciano");
#         }
#         else {
#             System.out.println(nom + " usted es un culicagao");
#         }
#     }
# }
# ```

# ### 3. Condicional múltiple
# Cuando lo que se desea es evaluar es mas de dos alternativas es necesario implementar una estructura condicional multiple. La forma de esta estructura se muestra en el siguiente diagrama de flujo.
# 
# ![if-elif-else](condicionales/if-elif-else.jpg)
# 
# Para solucionar problema de selección multiple se pueden usar 2 formas:
# 
# a. Estructuras de decisión anidadas (if-else) <br>
# b. Empleando la estructura de selección multiple (if-elsif-else)
# 
# #### a. Implementación con condicionales anidados
# 
# Consisten en evaluar una condición dentro de una condición previamente evaluada. A continuación se muestra una comparación de la sintaxis de java con la de python:
# 
# **Python**:
# 
# ```python
# if condicion 1:
#     # Instruciones condicion 1 verdadero
#     instruccion 1
#     instruccion 2
#     ...
#     instruccion C1
# else:
#     if condicion 2:
#         # Instruciones condicion 2 verdadero
#         instruccion 1
#         instruccion 2
#         ...
#         instruccion C2
#     else:
#         if condicion N:
#             # Instruciones condicion N verdadero
#             instruccion 1
#             instruccion 2
#             ...
#             instruccion C
#         else:
#             # Instruciones falso
#             instruccion 1
#             instruccion 2
#             ...
#             instruccion F
# ```
# 
# **Java**:
# 
# ```java
# if (condicion 1) {
#     // Instruciones condicion 1 verdadero
#     instruccion 1;
#     instruccion 2;
#     ...
#     instruccion C1;
# }
# else {
#     if (condicion 2) {
#         // Instruciones condicion 2 verdadero
#         instruccion 1;
#         instruccion 2;
#         ...
#         instruccion C2:
#     }
#     else {
#         if (condicion N) {
#             // Instruciones condicion 2 verdadero
#             instruccion 1;
#             instruccion 2;
#             ...
#             instruccion CN;
#         }
#         else {
#             // Instruciones falso
#             instruccion 1;
#             instruccion 2;
#             ...
#             instruccion F;
#         }
#     }
# }
# ```
# 
# Para comprender el uso de la estructura anterior, miremos el siguiente ejemplo.

# **Ejemplo 3**: 
# 
# Realizar un programa que permita que solicite una nota numerica dentro del rango 0 - 100 y permita la conversión a nota en letras de acuerdo a la siguiente tabla:
# 
# |Nota en letras | Rango de notas numerico |
# |---|---|
# |A|nota numerica mayor o igual a 90|
# |B|nota numerica mayor o igual a 80 y debajo de 90|
# |C|nota numerica mayor o igual a 70 y menor que 80|
# |D|nota numerica mayor o igual a 60 y menor que 70|
# |F|nota numerica menor que 60|
# 
# **Nota**: Para este problema se asume que el usuario no es lo suficiente estupido para no seguir las instrucciones que da el programa, por lo tanto, nunca se va a equivocar en la entrada de la nota numérica.
# 
# A continuación se muestra el diagrama de flujo asociado al problema:
# 
# ![notas_diagrama_de_flujo](condicionales/notas_diagrama_de_flujo.jpg)

# **Código Python**

# In[ ]:


# Ingreso de la nota numerica
score = float(input("Ingrese la nota numerica (dentro del rango [0,100]): "))

# Validación de la nota numerica y obtencion de la nota en letras dependiendo la tabla
if score >= 90.0:
    grade = 'A'
else:
    if score >= 80.0:
        grade = 'B'
    else:
        if score >= 70.0:
            grade = 'C'
        else:
            if score >= 60.0:
                grade = 'D'
            else:
                grade = 'F'

# Despliegue de la nota numerica
print("La nota en letra correspondiente a " + str(score) + " es: " + grade)


# **Código Java**
# 
# ```java
# import java.util.Scanner;
# 
# public class Calificacion {
#     public static void main(String[] args) {
#         // Variables
#         float score;
#         char grade;
# 
# 
#         // Objeto tipo Scanner
#         Scanner input = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner
#         
#         //Ingreso de la nota numerica
#         System.out.print("Ingrese la nota numerica (dentro del rango [0,100]): ");
#         score = input.nextFloat();
#         
#         // Validación de la nota numerica y obtencion de la nota en letras dependiendo la tabla
#         if (score >= 90.0) {
#             grade = 'A';
#         }
#         else {
#             if (score >= 80.0) {
#                 grade = 'B';
#             }
#             else {
#                 if (score >= 70.0) {
#                     grade = 'C';
#                 }
#                 else {
#                     if (score >= 60.0) {
#                         grade = 'D';
#                     }
#                     else {
#                         grade = 'F';
#                     }
#                 }
#             }
#         }
#     }
# }
# ```

# In[ ]:


get_ipython().run_cell_magic('writefile', 'ExampleIO10.java', 'import java.util.Scanner;\n\npublic class Calificacion {\n    public static void main(String[] args) {\n        // Variables\n        float score;\n        char grade;\n\n\n        // Objeto tipo Scanner\n        Scanner input = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner\n\n        //Ingreso de la nota numerica\n        System.out.print("Ingrese la nota numerica (dentro del rango [0,100]): ");\n        score = input.nextFloat();\n\n        // Validación de la nota numerica y obtencion de la nota en letras dependiendo la tabla\n        if (score >= 90.0) {\n            grade = \'A\';\n        }\n        else {\n            if (score >= 80.0) {\n                grade = \'B\';\n            }\n            else {\n                if (score >= 70.0) {\n                    grade = \'C\';\n                }\n                else {\n                    if (score >= 60.0) {\n                        grade = \'D\';\n                    }\n                    else {\n                        grade = \'F\';\n                    }\n                }\n            }\n        }\n    }\n}')


# #### b. Implementacion mediante la estructura de selección multiple (if-else if-else)
# 
# Esta es la mejor forma de evaluar (siempre y cuando el problema se preste para ello), un problema que involucre mas de dos posibilidades. Para ello se emplea la instrucción **if-else if-else**. A continuación se compara la sintaxis de python con la de java para este caso:
# 
# **Python**:
# 
# ```python
# if condicion 1:
#     # Instruciones condicion 1 verdadero
#     instruccion 1
#     instruccion 2
#     ...
#     instruccion C1
# elif condicion 2:
#     # Instruciones condicion 2 verdadero
#     instruccion 1
#     instruccion 2
#     ...
#     instruccion C2
# ...
# elif condicion N:
#     # Instruciones condicion N verdadero
#     instruccion 1
#     instruccion 2
#     ...
#     instruccion CN
# else:
#     # Instruciones falso
#     instruccion 1
#     instruccion 2
#     ...
#     instruccion F
# ```
# 
# **Java**:
# 
# ```java
# if (condicion 1) {
#     // Instruciones condicion 1 verdadero
#     instruccion 1;
#     instruccion 2;
#     ...
#     instruccion C1;
# } 
# else if (condicion 2) {
#     // Instruciones condicion 2 verdadero
#     instruccion 1;
#     instruccion 2;
#     ...
#     instruccion C2:
# }
# ...
# else if (condicion N) {
#      // Instruciones condicion 2 verdadero
#      instruccion 1;
#      instruccion 2;
#      ...
#      instruccion CN;
# }
# else {
#      // Instruciones falso
#      instruccion 1;
#      instruccion 2;
#      ...
#      instruccion F;
# }
# ```
# 
# Para comprender el uso de la estructura anterior, miremos el siguiente ejemplo.

# **Ejemplo 4**: 
# 
# Realizar un programa que permita que solicite una nota numerica dentro del rango 0 - 100 y permita la conversión a nota en letras de acuerdo a la siguiente tabla:
# 
# |Nota en letras | Rango de notas numerico |
# |---|---|
# |A|nota numerica mayor o igual a 90|
# |B|nota numerica mayor o igual a 80 y debajo de 90|
# |C|nota numerica mayor o igual a 70 y menor que 80|
# |D|nota numerica mayor o igual a 60 y menor que 70|
# |F|nota numerica menor que 60|
# 
# **Nota**: Para este problema se asume que el usuario no es lo suficiente estupido para no seguir las instrucciones que da el programa, por lo tanto, nunca se va a equivocar en la entrada de la nota numérica.
# 
# A continuación se muestra el diagrama de flujo asociado al problema:
# 
# ![notas_diagrama_de_flujo](condicionales/notas_diagrama_de_flujo.jpg)

# **Código Python**
# 
# El código solución se muestra a continuación, pero en este caso se hace uso de la estructura **if-elif-else**:

# In[ ]:


# Ingreso de la nota numerica
score = float(input("Ingrese la nota numerica (dentro del rango [0,100]): "))

# Validación de la nota numerica y obtencion de la nota en letras dependiendo la tabla
if score >= 90.0:
    grade = 'A'
elif score >= 80.0:
    grade = 'B'
elif score >= 70.0:
    grade = 'C'
elif score >= 60.0:
    grade = 'D'
else:
    grade = 'F'

# Despliegue de la nota numerica
# print("La nota en letra correspondiente a", score, "es:", grade)
print("La nota en letra correspondiente a " + str(score) + " es: " + grade)


# **Código Java**
# 
# A continuación se muestra como se simplifica el código solución al usar la estructura **if-else if-else** de java:
# 
# ![if_elsif-else](condicionales/if_elsif-else.jpg)
# 
# El código solución en java se muestra a continuación, pero en este caso se hace uso de la estructura if-elif-else:
# 

# ```java
# import java.util.Scanner;
# 
# public class Calificacion {
#     public static void main(String[] args) {
#         // Variables
#         float score;
#         char grade;
# 
# 
#         // Objeto tipo Scanner
#         Scanner input = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner
#         
#         //Ingreso de la nota numerica
#         System.out.print("Ingrese la nota numerica (dentro del rango [0,100]): ");
#         score = input.nextFloat();
#         
#         // Validación de la nota numerica y obtencion de la nota en letras dependiendo la tabla
#         if (score >= 90.0) {
#             grade = 'A';
#         }
#         else if (score >= 80.0) {
#             grade = 'B';
#         }
#         else if (score >= 70.0) {
#             grade = 'C';
#         }
#         else if (score >= 60.0) {
#             grade = 'D';
#         }
#         else {
#             grade = 'F';
#         }
#     }
# }
# ```

# ### 4. Estructura switch
# 
# La sentencia switch, permite que el programa tome diferentes rutas de ejecución, de acuerdo al valor de una variable determinada conocida como **selector** al momento en el que se llega al inicio de la sentencia. Los tipos de variables aceptados son.
# * ```byte```, ```short```, ```char```, ```int```
# * ```String```
# * Clases de empaquetado (```Character```, ```Integer```, etc).
# 
# Esta estructura no se encuentra disponible en **python** de modo que la sintaxis para **java** será:
# 
# ```java
# switch (variable) {
#     case opcion1:
#         sentencia1_1;
#         sentencia1_2;
#         ...
#         sentencia1_N;
#         break;
#     case opcion2:
#         sentencia2_1;
#         sentencia2_2;
#         break;
#         sentencia2_N;
#         break;
#     ...
#     case opcionN:
#         sentenciaN_1;
#         sentenciaN_2;
#         
#         sentenciaN_N;
#         break;
#     default:
#         sentenciaDefault_1;
#         sentenciaDefault_2;
#         sentenciaDefault_N;
#         break;
# }
# ```
# 
# Veamos un ejemplo para aclarar el uso de esta estructura.

# **Ejemplo 5**:
# 
# Hacer un programa que permita solicite digitar un numero entre 1 y 7 que diga el dia de la semana equivalente.
# 
# **Código Java**
# 
# ```java
# import java.util.Scanner;
# 
# public class DiaSemana {
#     public static void main(String[] args) {
#         // Variables
#         byte dia;
# 
#         // Objeto tipo Scanner
#         Scanner input = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner
# 
#         //Ingreso de la nota numerica
#         System.out.print("Ingrese el numero del dia: ");
#         
#         dia = input.nextByte();
# 
#         // Validación de la nota numerica y obtencion de la nota en letras dependiendo la tabla
#         switch (dia) {
#             case 1:
#                 System.out.println("Lunes");
#                 break;
#             case 2:
#                 System.out.println("Martes");
#                 break;
#             case 3:
#                 System.out.println("Miercoles");
#                 break;
#             case 4:
#                 System.out.println("Jueves");
#                 break;                
#             case 5:
#                 System.out.println("Viernes");
#                 break;                
#             case 6:
#                 System.out.println("Sabado");
#                 break;                
#             case 7:
#                 System.out.println("Domingo");
#                 break;
#             default:
#                 System.out.println("Dia invalido");
#         }
#     }
# }
# ```

# **Ejemplo 6**:
# 
# Hacer un programa que solicite un dia de la semana (de manera numerica) y diga si este fin de semena o semana.
# 
# **Código Java**
# 
# ```java
# import java.util.Scanner;
# 
# public class DiaSemana {
#     public static void main(String[] args) {
#         // Variables
#         byte dia;
# 
#         // Objeto tipo Scanner
#         Scanner input = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner
# 
#         //Ingreso de la nota numerica
#         System.out.print("Ingrese el numero del dia: ");
#         
#         dia = input.nextByte();
# 
#         // Validación de la nota numerica y obtencion de la nota en letras dependiendo la tabla
#         switch (dia) {
#             case 1:               
#             case 2:                
#             case 3:                
#             case 4:                
#             case 5:
#                 System.out.println("Dia de la semana");
#                 break;                
#             case 6:
#             case 7:
#                 System.out.println("Dia del fin de semana");
#                 break;
#             default:
#                 System.out.println("Dia invalido");
#         }
#     }
# }
# ```

# ## Referencias 
# 
# * https://github.com/LuisaRestrepo/MisionTIC2022-Ciclo2/blob/master/Presentaciones/Semana%201%20-%202.%20Variables%2C%20Cadenas%2C%20Estructuras%2C%20Arreglos.pdf

# In[ ]:





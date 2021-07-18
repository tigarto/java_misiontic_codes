#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install tutormagic')
get_ipython().run_line_magic('load_ext', 'tutormagic')


# In[ ]:


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# In[ ]:


# Run and print a shell command.
def run(cmd):
    print('>> {}'.format(cmd))
    get_ipython().system("{cmd}  # This is magic to run 'cmd' in the shell.")
    print('')

def compile(nombre_clase):
    run('javac {}.java'.format(nombre_clase))

def execute(nombre_clase):
    run('java {}'.format(nombre_clase))

def ejecutar(nombre_clase):
    compile(nombre_clase)
    execute(nombre_clase)


# In[ ]:


# Check the Java version to see if everything is working well.
run("javac -version")


# # Arreglos #

# ## Definición ##
# 
# Un arreglo es una secuencia de datos del mismo tipo llamados elementos los cuales pueden ser accedidos medinte un subindice.

# ### Declaración  y creación de un arreglo ###
# 
# ### Declaración ###
# 
# Un array se declara de modo similar a otros tipos de datos; sin embargo, se debe indicar al compilador que es un arreglo y esto se hace con corchetes. La declaración se puede hacer de dos formas:
# 1. **Colocando los corchetes al principio**:
# 
# ```java
# tipo [] identificador;
# ```
# 
# 2. **Colocando los corchetes al final**:
# 
# ```java
# tipo identificador[];
# ```
# 
# **Ejemplos**: A continuación se muestran varios ejempls de declración:
# 
# 1. Declaración tipica:
# 
# ```java
# int[] numbers;
# ```
# 
# O tambien la forma equivalente:
# 
# 
# ```java
# int numbers[];
# ```
# 
# 2. Declaración de varios arreglos en una misma linea:
# 
# ```java
# int[] numbers, codes, scores; // numbers, codes, scores son arreglos tipo int
# ```
# 
# 3. Notación que combina arreglos y datos simples:
# 
# ```java
# int numbers[], codes[], scores; // Solo numbers y codes son arrays tipo int, 
#                                 // scores es una variable sencilla tipo int.
# ```
# 
# 
# ### Creación ###
# 
# Java considera que un arreglo es una referencia a un objeto por lo tanto para que realmente cree un arreglo, es necesario usar el operador ```new``` junto altipo de los elementos del arreglo y su número.
# 
# ```java
# tipo nombreArreglo [] = new tipo[numeroDeElementos];
# ```
# 
# ### En resumen ###
# 
# Tal y como se mostró anteriormente, la definición y creación de un arreglo involucra dos pasos tal y como se muestra en el siguiente fragmento de codigo:
# 
# ```java
# int[] numbers;              // 1. Declarar una referencia al array que mantendra los enteros.
# numbers = new int[6];       // 2. Crear un nuevo array que mantenga 6 enteros
# ```
# 
# El proceso anterior (declarar la referencia a un arreglo y crearlo) puede ser realizado en una sola instrucción tal y como se muestra a continuación:
# 
# ```java
# int[] numbers = new int[6]; // Declaración y creacion de un array que mantiene 6 enteros
# ```
# 
# 

# **Ejemplo**: A continuación se muestran varias formas de inicializar un arreglo.

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ArraysExample1 {\n    public static void main(String[] args) {\n        // Forma 1\n        int a[] = new int [10];\n        // Forma 2\n        final int N = 20;\n        float [] vector;\n        vector = new float[N];\n\n    }\n}')


# **Consideraciones sobre el tamaño**:
# * Debe ser un numero entero positivo.
# * Puede ser un valor literal, una constante o una variable.
# 
# ```java
# final int ARRAY_SIZE = 6;
# int[] numbers = new int[ARRAY_SIZE];
# ```
# 
# * Una vez que el  array es creado el tamaño de este es fijo y no puede ser cambiado
# 
# El siguiente fragmento de código aterriza este concepto:
# 
# 

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ArraysExample2 {\n    public static void main(String[] args) {\n        // Tamaño del array constante \n        final int ARRAY_SIZE = 6;\n        int[] numbers = new int[ARRAY_SIZE];\n        \n        // Tamaño del array a partir de una variable\n        int tam = 10;\n        float [] vector = new float[tam];\n    }\n}')


# ## Acceso a un arreglo ##
# 
# Son empleados para acceder a un arreglo especificando la posición a la cual se desea acceder. Un array es accedido por medio:
# 1. La referencia el nombre.
# 2. El subindice que especifica a cual elemento en en array se va a acceder. 
# 
# 
# 
# 

# **Ejemplo**: Crear un arreglo de 10 enteros y asignar a los elementos con subindice 0, 3, 6 los valores de -3, 10, 25 respectivamente.

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ArraysExamples4 {\n    public static void main(String[] args) {\n        final int TAM = 10;\n        int [] mes = new numbers[TAM];\n        numbers[0] = -3;  // Acceso al elemento con subindice 0 para asignarle el valor de 3\n        numbers[3] = 10;  // Acceso al elemento con subindice 0 para asignarle el valor de 3\n        numbers[6] = 26;  // Acceso al elemento con subindice 0 para asignarle el valor de 3\n    }\n}')


# **Ejemplo**: Simule y comprenda el siguiente fragmento de código.

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ArraysExamples3 {\n    public static void main(String[] args) {\n        float s;\n        int [] mes = new int[6];\n        float salarios[];\n        salarios = new float[13];\n        mes[4] = 2;\n        s = salarios[mes[4]*3];\n    }\n}')


# ## Procesamiento del contenido de un arreglo ##
# El procesamiento de los elementos de un array (lectura o escritura) se hace de a uno a la vez. Asi por ejemplo, si se tiene un arreglo de 5 elementos, será necesario ingresar 5 los elementos al array uno por uno. Esto mismo aplica para mostrar el contenido de un array. A continuación se muestran 3 escenarios basicos en donde se hace esto:
# 
# **Escenario 1**: Cuando se entran elementos a una array:
# 
# ```java
# // code
# ```
# 
# **Escenario 2**: Cuando se muestran elementos de un array:
# 
# ```java
# // code
# ```
# **Escenario 3**: Cuando se procesan los elementos de un array:
# 
# ```java
# grossPay = hours[3] * payRate;
# ```
# 
# ```java
# int[] score = {7, 8, 9, 10, 11};
# ++score[2]; // Pre-increment operation
# score[4]++; // Post-increment operation
# ```
# 
# 

# **Ejemplo 1**: Este programa muestra y despliega los valores almacenados en los elementos de un arreglo
# (** Programa tomado del libro de Gaddis (Starting Out Java early objects))
# 
# ```java
# import java.util.Scanner;   // Needed for Scanner class
# 
# /**
#    This program shows an array being processed with loops.
# */
# 
# public class ArrayDemo2
# {
#    public static void main(String[] args)
#    {
#       final int EMPLOYEES = 3;           // Number of employees
#       int[] hours = new int[EMPLOYEES];  // Array of hours
#       
#       // Create a Scanner object for keyboard input.
#       Scanner keyboard = new Scanner(System.in);
# 
#       System.out.println("Enter the hours worked by " +
#                          EMPLOYEES + " employees.");
# 
#       // Get the hours for each employee.
#       for (int index = 0; index < EMPLOYEES; index++)
#       {
#          System.out.print("Employee " + (index + 1) + ": ");
#          hours[index] = keyboard.nextInt();
#       }
# 
#       System.out.println("The hours you entered are:");
# 
#       // Display the values entered.
#       for (int index = 0; index < EMPLOYEES; index++)
#          System.out.println(hours[index]);
#    }
# }     
# ```

# ## Inicialización de un arreglo ##
# 
# Java permite inicializar los elementos de un arreglo cuando este es creado. Para esto lo que se hace es crear el arreglo y pasarle un serie de valores separados por coma y entre llaves conocida como **lista de inicialización**. A continuación se muestran algunos ejemplos:
# 
# #### Ejemplo 1 ####
# 
# ```java
# int numeros[] = {10, 20, 30, 40, 50, 60};
# int[]nms = {3, 4, 5}
# char c[] = {'L','u','i','s'};
# 
# ```
# 
# #### Ejemplo 2 ####
# 
# ```java
# int[] days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
# 
# final int ENE = 31, FEB = 28, MAR = 31, ABR = 30, MAY = 31,
#           JUN = 30, JUL = 31, AGO = 31, SEP = 30, OCT = 31,
#           NOV = 30, DIC = 31;
# 
# int meses[] = {ENE, FEB, MAR, ABR, MAY, JUN, JUL, AGO, SEP, OCT, NOV, DIC};
# ```
# 
# #### Ejemplo 3 ####
# A veces para facilitar la claridad es bueno inicializar un array empleando multiples lineas:
# 
# ```java
# double[] coins = { 0.05,
#                    0.1,
#                    0.25,
#                    0.5,
#                    1.0 };
# ```
# 

# ### Tamaño de los arreglos, atributo length ###
# 
# Java considera cada arreglo como un **objeto** que, además de tener capacidad para almacenar elementos, dispone del atributo **length** el cual contiene el numero de elementos que tiene el array. Por ejemplo:
# 
# ```java
# double [] v = new double[15];
# System.out.print(v.length);    // Muestra en pantalla 15 (numero de elementos del array v)
# ```

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ArraysExample2 {\n    public static void main(String[] args) {\n        ArraysExample2 example = new ArraysExample2();  // Por que se uso ???\n        double [] v = new double[4];\n        double rSum = 0;\n        for (int i = 0; i < v.length; i++) {\n            v[i] = i;\n            System.out.print(v[i] + " ");\n        }\n        System.out.println();\n        rSum = example.suma(v);  // Por que se uso ???\n        System.out.println("Resultado suma: " + rSum);\n    }\n    \n    double suma (double[] w) {\n      double s = 0.0;\n      for (int i = 0; i < w.length; i++)\n        s += w[i];\n      return s;\n    }\n}')


# ## Verificación del índice de un arreglo ##
# En el siguiente fragmento de código se muestra proteger un vector de un error por indice fuera de rango
# 
# ```java
# int datos(double a[])
# {
#   int n;
#   System.out.println("Entrada de datos, cuantos elementos: ? ");
#   n = entrada.nextInt();
#   if (n > a.length)
#     return 0;
#   for (int i = 0; i < n; i++)
#     a[i]= entrada.nextDouble();
#   return 1;
# }
# ```
# 

# ### Ejercicio 10.1 ###
# El programa escrito a continuación lee NUM enteros en un arreglo,
# multiplica los elementos del arreglo y visualiza el producto.
# 
# **Solución**:
#     
# ```java
# import java.util.Scanner;
# 
# class Inicial {
#     public static void main(String [] a) {
#         final int NUM = 10;
#         Scanner entrada = new Scanner(System.in);
#         int []nums= new int[NUM];
#         int total = 1;
#         
#         System.out.println("Por favor, introduzca " + NUM + " datos");
#         for (int i = 0; i < NUM; i++) {
#             nums[i] = entrada.nextInt();
#         }
#         
#         System.out.print("\nLista de números: ");
#         for (int i = 0; i < NUM; i++) {
#             System.out.print(" " + nums[i]);
#             total *= nums[i];
#         }
#         
#         System.out.println("\nEl producto de los números es " + total);
#     }
# }
# ```    

# ### Copia de arreglos ###

# Observe el siguiente fragmendo de codigo:

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class CopyExample2 {\n    public static void main(String[] args) {\n        double [] r, w;\n        r = new double[11];\n        w = new double[15];\n        for (int j = 0; j < r.length; j++) {\n            r[j] = (double) 2*j-1;\n        }\n        // asignación del arreglo r a w\n        w = r;\n        r[3] = 4;\n        w[4] = -6;\n    }\n}')


# Ahora, observe el siguiente codigo. ¿En que se diferencia respecto al anterior?

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class CopyExample1 {\n    public static void main(String[] args) {\n        double [] r, w;\n        r = new double[11];\n        w = new double[11];\n        for (int j = 0; j < r.length; j++) {\n            r[j] = (double) 2*j-1;\n        }\n        // asignación del arreglo r a w\n        for (int j = 0; j < r.length; j++) {\n            w[j] = r[j];\n        }\n        r[3] = 4;\n        w[4] = -6;\n    }\n}')


# ## Metodo arraycopy ##
# 
# **Sintaxis**:
# 
# ```java
# System.arraycopy (arreglo Origen, inicioOrigen, arreglo Destino, inicioDestino, numElementos)
# ```
# 
# **Donde**:
# * **arreglo Origen**: nombre del arreglo que se va a copiar.
# * **inicioOrigen**: posición del arreglo origen donde se inicia la copia.
# * **arreglo Destino**: nombre del arreglo en el que se hace la copia.
# * **inicioDestino**: es la posición del arreglo destino donde empieza la copia.
# * **numElementos**: número de elementos del arreglo origen que se van a copiar.

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class CopyExample3 {\n    public static void main(String[] args) {\n        double [] r, w;\n        r = new double[11];\n        w = new double[11];\n        for (int j = 0; j < r.length; j++) {\n            r[j] = (double) 2*j-1;\n        }\n        // asignación del arreglo r a w\n        System.arraycopy (r, 0, w, 0, r.length);\n        r[3] = 4;\n        w[4] = -6;\n    }\n}')


# ### Ejercicio 10.2 ###
# Definir dos arreglos de tipo double, v y w con 15 y 20 elementos respectivamente; 
# en el primero se guardan los valores de la función e^(2*x - 1); el segundo inicializa cada elemento al ordinal del elemento; después se copian los 10 últimos
# elementos de v a partir del elemento 11 de w; por ultimo, se escriben los
# elementos de ambos arreglos.
# 
# **Solución**:
#     
# ```java
# public class CopiArreglo
# {
#     public static void main(String [] a)
#     {
#         final int N = 15;
#         final int M = 20;
#         double [] v = new double[N];
#         double [] w = new double [M];
#         double x = 1.0;
# 
#         for (int i = 0; i < N; x+=0.2,i++) {
#             v[i] = Math.exp(2 * x - 1);
#         }
# 
#         for (int i = 0; i < M; i++) {
#             w[i] = (double) i;
#         }
# 
#         // Se imprimen los elementos del vector v
#         System.out.println("\n Valores del vector v");
#         for (int i = 0; i < N; i++) {
#             System.out.print(v[i] + " ");
#         }
# 
#         // Es realizada la copia de v a w
#         System.arraycopy(v, (N-1)-10 +1, w, 10, 10);
# 
#         // Se imprimen los elementos del vector w
#         System.out.println("\n Valores del vector w");
#         for (int i = 0; i < M; i++) {
#             System.out.print(w[i] + " ");
#         }
#     }
# }
# ```  

# ### Bucle for each para recorrido de arreglos y colecciones ###

# In[ ]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Bucle {\n    public static void main(String[] args) {\n        int sumA = 0, sumB = 0;\n        int [] a = {1,2,3};\n        int [] b = {4,5,6};\n        \n        // Forma tradicional\n        for (int i = 0; i < a.length; i++) {\n            System.out.print(a[i] + " ");\n            sumA += a[i];\n        }\n        System.out.print("\\nsumA = " + sumA + "\\n\\n");\n        // Forma for each\n        for (int num:b) {\n            System.out.print(num + " ");\n            sumB += num;\n        }\n        System.out.print("\\nsumB = " + sumB + "\\n");\n    }\n}')


# In[ ]:





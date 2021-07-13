#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip3 install tutormagic')
get_ipython().run_line_magic('load_ext', 'tutormagic')


# In[5]:


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# # Entrada y salida en java

# Las operaciones de entrada y salida son importantes por que permiten la interacción entre el programa y el usuario. Para este caso, la salida la asociaremos a la pantalla y la entrada la asociaremos al teclado.

# ## Salida en java
# 
# ### 1. Recordando la salida en Python
# 
# En python la instrucción para mostrar datos en pantalla es la función ```print```, esta, desde el punto de vista mas basico, tiene la siguiente sintaxis:
# 
# ```python
# print("Lista de mensajes y variables separados por coma")
# ```
# 
# ### 2. Salida en pantalla en Java
# 
# El dispositivo de salida estándar suele ser un monitor. En Java la salida en el dispositivo de salida estándar se efectúa empleando el objeto de salida estándar ```System.out```. El objeto ```System.out``` tiene acceso a dos métodos, ```print``` y ```println```, para dar salida a una cadena en el dispositivo de salida estándar.
# 
# La forma general empleada para mostrar algo en consola se muestra a continuación:
# 
# ```java
# System.out.printf(FormatString, ArgList);
# ```
# 
# Donde:
# * **FormatString**: String que contiene texto y/o espeficidadores de formato especiales.
# * **ArgList**: Es una lista de argumentos adicionales que seran formateados de acuerdo a los especificadores de formato listadoa en el argumento pasado como ```FormatString```.
# 
# Es importante aclarar sintaxis anterior tambien aplica al método ```println```. La diferencia entre los metodos ```print``` y ```println``` radica en que el último método agrega un enter al final de la cadena desplegada en la pantalla.
# 
# Para comprender como es la salida en pantalla en java, realicemos una comparación con el caso de python mediante una serie de ejemplos.

# **Ejemplo 1**: Dado el siguiente código python:

# In[14]:


print("Adios mundo cruel")


# ¿Como es su implementacion en java?

# In[15]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ExampleIO1 {\n    public static void main(String[] args) {\n        System.out.println("Adios mundo cruel");\n    }\n}')


# **Ejemplo 2**: Dado el siguiente código python:

# In[16]:


print(29/4)
print("Hola que tal?")
print(12)
print("4 + 7")
print(4 + 7)
print('A')
print("4 + 7 = " + str(4 + 7))   # print("4 + 7 =",(4 + 7)) 
print(2 + 3*5)
print("Hola \nque tal?")


# La implementación en java es: 

# In[17]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ExampleIO2 {\n    public static void main(String[] args) {\n        System.out.println("Adios mundo cruel");\n        System.out.println(29/4);\n        System.out.println("Hola que tal?");\n        System.out.println(12);\n        System.out.println("4 + 7");\n        System.out.println(4 + 7);\n        System.out.println(\'A\');\n        System.out.println("4 + 7 = " + (4 + 7));\n        System.out.println(2 + 3*5);\n        System.out.println("Hola \\nque tal?");\n    }\n}')


# **Ejemplo 3**: Dado el siguiente código python:

# In[18]:


print("Hola que tal. ", end = "")
print("Mi nombre es Bon, James Bon.")


# La implementación en código java se muestra a continuación:

# In[20]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ExampleIO3 {\n    public static void main(String[] args) {\n        System.out.print("Hola que tal. ");                     // Metodo print (no hay cambio de linea)\n        System.out.println("Mi nombre es Bon, James Bon.");     // Metodo println  \n    }\n}')


# #### Caracteres especiales
# 
# La siguiente tabla muestra algunas secuencias de escape las cuales permiten controlar la salida mostrada en pantalla.
# 
# |Simbolo|Secuencia de escape |Descripción|
# |:---|:---|:---|
# |```\n``` | Nueva línea | El cursor se mueve al inicio de la siguiente línea |
# |```\t``` |Tabulador | El cursor se mueve a la siguiente parada del tabulador |
# |```\b``` |Espacio de retroceso | El cursor se mueve un espacio a la izquierda |
# |```\r``` |Retorno | El cursor se mueve al inicio de la línea actual (no a la siguiente línea) |
# |```\\``` |Diagonales invertidas | Se imprime una diagonal inversa |
# |```\'``` |Comilla simple | Se imprime una comilla simple |
# |```\"``` |Comilla doble | Se imprimen comillas dobles |
# 
# 

# **Ejemplo 4**: Analice y comprenda la salida arrojada por el siguiente programa en java:

# In[22]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ExampleIO4 {\n    public static void main(String[] args) {\n        System.out.println("Hello " + "World");\n        System.out.println("The value is: " + 5);\n        System.out.println("The value is: " + value);\n        System.out.println();\n        System.out.print("These are our top sellers:\\n");\n        System.out.print("\\tComputer games\\n\\tCoffee\\n ");\n        System.out.println("\\tAspirin");\n        System.out.println();\n        System.out.println("We can join a string to " +\n                           "a number like this: " + 5);\n        System.out.println();\n        System.out.println("The following will be printed " +\n                           "in a tabbed format: " +\n                           "\\n\\tFirst = " + 5 * 6 + ", " +\n                           "\\n\\tSecond = " + (6 + 4) + "," +\n                           "\\n\\tThird = " + 16.7 + "."); \n    }\n}')


# #### Formateando la salida
# 
# Recordemos la sintaxis de uso asociada a las funciones ```print``` y ```println```
# 
# ```java
# System.out.printf(FormatString, ArgList);
# ```
# 
# Mediante el formateo de una salida, se puede obtener un mayor control sobre lo que se quiere mostrar a la salida. Antes de entrar en detalle a hablar del tema, observe las siguiente figuras:
# 
# ![print1](io_basica/print1.jpg)
# 
# ![print2](io_basica/print2.jpg)
# 
# ![print3](io_basica/print3.jpg)
# 
# ![print4](io_basica/print4.jpg)
# 
# Si observa con detenimiento, hay una porción de la cadena que contiene el signo de **%** seguido de unos caracteres (Cerrado en circulo en las figuras anteriores), a esta se le conoce como **especificador de formato y control**. Un especificador de formato para uso general, carácter y tipos numéricos tiene la siguiente sintaxis:
# 
# ```java
# %[argument_index$][flags][width][.precision]conversion
# ```
# 
# Sobre la sintaxis anterior tenemos:
# * Las expresiones entre corchetes son opcionales. Es decir, pueden o no aparecer en un especificador de formato.
# * La opción **```argument_index```** es un número entero (decimal), que indica la posición del argumento en la lista de argumentos. 
# * La opción **```flags```** es un conjunto de caracteres que modifica el formato de salida. El conjunto de banderas válidas depende de la conversión.
# * La opción **```width```** es un número entero (decimal), que indica el número mínimo de caracteres que se escriben en la salida.
# * La opción **```precision```** es un número entero (decimal) que normalmente se usa para restringir el número de caracteres. El comportamiento específico depende de la conversión.
# * La **```conversion```** requerida es de un carácter que indica cómo se debe formatear el argumento. El conjunto de conversiones válidas para un argumento dado depende del tipo de datos del argumento. La siguiente tabla muestra algunos de los caracteres empleados para conversión:
# 
# |Caracter de conversion|Descripción|
# |:---|:---|
# |```s```|Cadena de caracteres|
# |```c```|Carácter sencillo |
# |```d```|Entero en formato de decimal |
# |```e```|Punto flotante en formato en notación científica |
# |```f```|Punto flotante en formato en decimal|
# 
# Los siguientes ejemplos permiten entender el siguificado del formateo anteriormente expuesto:

# **Ejemplo 5**:

# In[25]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ExampleIO5 {\n    public static void main(String[] args) {\n        double horas = 34.45;\n        double tarifa = 15.00;\n        double tolerancia = 0.01000;\n        System.out.println("Notacion decimal fija:");\n        System.out.printf("horas = %.2f, tarifa = %.2f, pago = %.2f," + \n                          " tolerancia = %.2f\\n\\n", horas, tarifa, horas * tarifa, tolerancia);\n        System.out.println("Notacion cientifica:");\n        System.out.printf("horas = %e, tarifa = %e, pago = %e, \\n" + \n                           "tolerancia = %e\\n",horas, tarifa, horas * tarifa, tolerancia);\n    }\n}')


# **Ejemplo 6**:

# In[28]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ExampleIO6 {\n    public static void main(String[] args) {\n        final double PI = 3.14159265;\n        double radio = 12.67; \n        double altura = 12.00;\n        \n        System.out.println("Dos cifras decimales: ");\n        System.out.printf("radio = %.2f, "\n                          + "altura = %.2f, volumen = %.2f, "\n                          + "PI = %.2f\\n\\n", radio, altura,PI * radio * radio * altura, PI);\n        \n        System.out.println("Tres cifras decimales: ");\n        System.out.printf("radio = %.3f, "\n                          + "altura = %.3f, volumen = %.3f, "\n                          + "PI = %.3f\\n\\n", radio, altura,PI * radio * radio * altura, PI);\n        \n        System.out.println("Cuatro cifras decimales: ");\n        System.out.printf("radio = %.4f, "\n                          + "altura = %.4f, volumen = %.4f, "\n                          + "PI = %.4f\\n\\n", radio, altura,PI * radio * radio * altura, PI);\n        \n        System.out.println("Diferentes cifras decimales: ");\n        System.out.printf("radio = %.1f, "\n                          + "altura = %.2f, volumen = %.5f, "\n                          + "PI = %.4f\\n\\n", radio, altura,PI * radio * radio * altura, PI);\n    }\n}')


# **Ejemplo 7**:

# In[31]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ExampleIO7 {\n    public static void main(String[] args) {\n        int num = 96;\n        double tasa = 15.50;\n        System.out.println("123456789012345");\n        System.out.printf("%5d \\n", num); \n        System.out.printf("%5.2f \\n", tasa); \n        System.out.printf("%5d%6.2f \\n", num, tasa);\n        System.out.printf("%5d%6.2f \\n", num, tasa);\n    }\n}')


# **Ejemplo 8**:

# In[32]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ExampleIO8 {\n    public static void main(String[] args) {\n        int num = 763; \n        double x = 658.75; \n        String str = " Programa Java.";\n        System.out.println("1234567890123456789" + \n                           "01234567890"); \n        System.out.printf("%5d%7.2f%15s\\n", num, x, str); \n        System.out.printf("%15s%6d%9.2f\\n", str, num, x); \n        System.out.printf("%8.2f%7d%15s\\n", x, num, str); \n        System.out.printf("num = %5d\\n", num); \n        System.out.printf("x = %10.2f\\n", x); \n        System.out.printf("str = %15s\\n", str); \n        System.out.printf("%10s%7d\\n", "Programa No.", 4);\n    }\n}')


# **Ejemplo 9**:

# In[34]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class ExampleIO8 {\n    public static void main(String[] args) {\n        int num = 763; \n        double x = 658.75; \n        String str = "Programa Java."; \n        System.out.println("1234567890123456789" + "01234567890"); \n        System.out.printf("%-5d%7.2f%-15s *** \\n", num, x, str); \n        System.out.printf("%-15s%-6d%-9.2f *** \\n", str, num, x); \n        System.out.printf("%-8.2f%-7d%-15s *** \\n", x, num, str); \n        System.out.printf("num = %-5d ***\\n",num); \n        System.out.printf("x = %-10.2f ***\\n", x); \n        System.out.printf("str = %-15s ***\\n", str); \n        System.out.printf("%-10s%-7d ***\\n", "Programa No.", 4);\n    }\n}')


# ## Entrada en Java
# 
# Pedimos disculpas. Sección en construcción...

# ## Referencias 
# 
# * https://learn.oracle.com/ols/course-list/40805
# * https://developer.ibm.com/es/languages/java/tutorials/j-introtojava1/
# * https://developer.ibm.com/es/languages/java/tutorials/j-perry-writing-good-java-code/
# * https://developer.ibm.com/es/languages/java/tutorials/java-language-constructs-1/
# * https://codelabs.developers.google.com/
# * https://developers.google.com/classroom/quickstart/java
# * https://developers.google.com/edu/python/introduction
# * http://docs.oracle.com/javase/tutorial/
# * https://docs.oracle.com/javase/tutorial/tutorialLearningPaths.html
# * https://education.oracle.com/es/learning-explorer

# In[ ]:





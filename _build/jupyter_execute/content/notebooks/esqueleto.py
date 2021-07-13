#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip3 install tutormagic')
get_ipython().run_line_magic('load_ext', 'tutormagic')


# In[3]:


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# # Estructura de un programa en Java

# Como punto de partida vamos a aprender a codificar un programa en java mediante la comparación con un programa en python tal y como se muestran en la siguientes secciones

# ## Estructura de un programa en python
# 
# Supongase que se desea realizar un programa en python que imprima en pantalla la frase ```Hola mundo!!!```. A continuación se muestra el codigo que realiza esto:

# In[4]:


get_ipython().run_cell_magic('tutor', '-k', 'print("Hola mundo")')


# ## Estructura de un programa en Java
# 
# En Java, las cosas cambian un poco. A continuación se muestra la forma como se haria el mismo programa anterior empleando lenguaje java

# In[15]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class HolaMundo {\n    public static void main(String[] args) {\n        System.out.println("Hola mundo!!!");        \n    }\n}')


# **Observaciones importantes**:
# 1. La unidad básica de un programa en Java es una clase (```class```).
# 2. Cada clase contiene uno o mas metodos.
# 3. La sintaxis basica de una clase (por ahora) se muestra a continuación:
# 
# ```java
# import instrucciones si las hay
# 
# public class NombreClase {
#   constantes nombradas y/o declaraciones de flujo de objetos
#   public static void main(String[] args) {
#     declaracion de variables
#     instrucciones
#   }
# }
# ```

# ## Ejemplos
# 
# 1. Dado el siguiente programa en python:

# In[18]:


get_ipython().run_cell_magic('tutor', '-k', 'print("Mi primer programa en Java.");\nprint("La suma de 2 y 3 =",5);\nprint("7 + 8 = " + str(7 + 8));')


# A continuación se muestra su codificación en Java, cuya clase se llama ```ASimpleJavaProgram```

# In[19]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\n//**********************************************************\n// Este es un programa simple en Java. Presenta tres lineas\n// de texto, incluyendo la suma de dos numeros.\n//**********************************************************\npublic class ASimpleJavaProgram {\n    public static void main(String[] args) {\n        System.out.println("Mi primer programa en Java.");\n        System.out.println("La suma de 2 y 3 = " + 5);\n        System.out.println("7 + 8 = " + (7 + 8));\n    }\n}')


# ## Elementos de un programa en java
# 
# Java es un **lenguaje de programación** y como tal poseee conjunto de reglas, símbolos y palabras especiales utilizadas para
# construir programas. 

# ### 1. Comentarios
# 
# Un **comentario** es una parte del código que puede ser usada con diversos propósitos, generalmente explicativos, y que no tienen ninguna incidencia en la ejecución del código ni son procesados por el compilador. Existen dos tipos de comentarios:
# 1. **Comentarios de una sola linea**:
# 
# ```java
# //Esto es un comentario de una sola línea      
# ```
# 
# 2. **Comentarios de varias lineas**:
# 
# ```java
# /* Esto es un comentario
# de más de
# una línea */      
# ```

# ### 2. Palabras reservadas (palabras clave)
# 
# Son palabras que no se pueden redefinir dentro de algún programa para un proposito distinto para el que fueron hechas. Algunas son:
# 
# ```java
# int, float, double, char, void, public, static, throws, return
# ```
# 

# ### 3. Variables
# Una variable es un espacio en memoria, especificado a la hora de escribir un programa en cualquier lenguaje de programación, que tiene un nombre, y que puede tener una información conocida o desconocida, denominada valor. 
# 
# Cuando se declara una variable en java (a diferencia de python) se debe especificar el tipo de dato tal y como se muestra a continuación:
# 
# ```java
# tipo nombreVariable <= Valor inicial>;  // Sintaxis de declaracion de una variable.
# ```
# 
# Tal y como se muestra entre los simbolos ```<``` y ```>```, la inicialización de una variable es opcional. Un ejemplo de una declaración de variables se muestra a continuación:
# 
# ```java
# int sumando;
# boolean estaActivado;
# double promedio;
# ```
# 
# Notesé que en el caso anterior, las variables no fueron inicializadas y por lo tanto sus valores iniciales serán desconocidos. A continuación se muestran algunos casos donde las variables son inicializadas:
# 
# ```java
# byte dividendo = 47;
# char sexo = 'f';
# boolean estaEncendido = false;  
# ```
# 
# * **Nota importante**: Toda variable antes de ser usada debe haber sido previamente declarada:
# 
# ```java
# float peso;
# peso = 84;
# ```
# 
# Si no se respeta lo anterior, se arrojará un error.
# 
# 
# Veamos mas sobre los diferentes tipos de datos manejados en java.
#     
# #### Tipos de Datos Primitivos
# 
# En Java, a la hora de declarar variables, contamos con ocho tipos de datos primitivos, más el tipo ```String```, que podemos considerar un tipo de dato especial. Estos se resumen a continuación:
# 
# |Categoria|Tipo de dato en java|
# |:---|:---|
# |Entero|```byte, short, int, long```|
# |Real|```float, double```|
# |Boleano|```boolean```|
# 
# Finalmente, el tipo de datos ```char```  puede almacenar un solo carácter. De hecho, una cadena de caracteres en Java, de tipo ```String``` es, internamente, un arreglo o array de caracteres (```char```), como veremos posteriormente.
# 
# En la siguiente tabla se muestra la lista de los tipos de datos primitivos en Java, incluyendo el tamaño que ocupan las variables de cada tipo de memoria, el rango que pueden tomar los valores de cada tipo y un ejemplo de cómo se escribe un valor para su asignación a dicha variable, lo que se denomina literal.
# 
# |Tipo|	Tamaño|	Rango|	Literal (ejemplo)|
# |:---|:---|:---|:---|
# |```byte```|8 bit	|$[-128 , 127]$| ```100```|
# |```short```|16 bit	|$[-32768 , 32767]$| ```10000```|
# |```long```|64 bit	|$[-2^{63} , 2^{63}-1]$| ```100000l```  ó ```100000L```|
# |```float```|32 bit	||```4.25f```  ó ```4.25f```|
# |```double```|64 bit || ```42.5``` ó ```42.5d``` ó ```42.5D``` ó ```4.25e1```|
# |```boolean```|1 bit |```true``` / ```false```|```false```|
# |```char```|16 bit	|[```'\u0000'``` , ```'\uffff'```]| ```'a'```|
# 
# 

# ### 4. Operadores
# 
# La siguiente tabla resume los principales operadores en java:
# 
# |Tipo de operadores|Operadores|
# |:---|:---|
# |Aritmeticos|```+```, ```-```, ```*```, ```/```, ```%```|
# |Relacionales|```>```, ```<```, ```>=```, ```<=```, ```!=```,```==```|
# |Logicos|```|```, ```&```, ```!```|
# 
# A continuación se muestran algunos programas ejemplo:

# **Ejemplo 1**: Programa que muestra algunas operaciones con numeros enteros.

# In[20]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example1 {\n    public static void main(String[] args) {\n        System.out.println("2 + 5 = " + (2 + 5));\n        System.out.println("13 + 89 = " + (13 + 89));\n        System.out.println("34 - 20 = " + (34 - 20));\n        System.out.println("45 - 90 = " + (45 - 90));\n        System.out.println("2 * 7 = " + (2 * 7));\n        System.out.println("5 / 2 = " + (5 / 2));\n        System.out.println("14 / 7 = " + (14 / 7));\n        System.out.println("34 % 5 = " + (34 % 5));\n        System.out.println("4 % 6 = " + (4 % 6));\n    }\n}')


# **Ejemplo 2**: Programa que muestra algunas operaciones con numeros de punto flotante.

# In[21]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example2 {\n    public static void main(String[] args) {\n        System.out.println("5.0 + 3.5 = " + (5.0 + 3.5));\n        System.out.println("3.0 + 9.4 = " + (3.0 + 9.4));\n        System.out.println("16.4 - 5.2 = " + (16.4 - 5.2));\n        System.out.println("4.2 * 2.5 = " + (4.2 * 2.5));\n        System.out.println("5.0 / 2.0 = " + (5.0 / 2.0));\n        System.out.println("34.5 / 6.0 = " + (34.5 / 6.0));\n        System.out.println("34.5 % 6.0 = " + (34.5 % 6.0));\n        System.out.println("34.5 / 6.5 = " + (34.5 / 6.5));\n        System.out.println("34.5 % 6.5 = " + (34.5 % 6.5));\n    }\n}')


# **Ejemplo 3**: Programa que muestra algunas operaciones relacionales

# In[23]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example3 {\n    public static void main(String[] args) {  \n        System.out.println("1 == 2: " + (1 == 2));\n        System.out.println("1 != 2: " + (1 != 2));\n        System.out.println("1 > 2: " + (1 > 2));\n        System.out.println("1 < 2: " + (1 < 2));\n        System.out.println("1 >= 2: " + (1 >= 2));\n        System.out.println("1 <= 2: " + (1 <= 2));\n    }\n}')


# **Ejemplo 4**: La siguiente tabla muestra la equivalencia entre los operadores logicos en python con los operadores logicos de Java:
# 
# |Operador Lógico en Python|Operador Lógico en Java|Observaciones|
# |:---|:---|:---|
# |```or```|```|```|Solo falsa cuando los dos operandos son falsos|
# |```and```|```&```|Solo verdadera cuando los dos operandos son verdaderos|
# |```not```|```!```|La salida tiene el valor logico contrario al valor logico de la entrada|

# In[29]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example4 {\n    public static void main(String[] args) {\n        System.out.println("----------- Operador or (|) -----------");\n        System.out.println(false + " | " + false + " = " + (false | false));\n        System.out.println(false + " | " + true + " = " + (false | true));\n        System.out.println(true + " | " + false + " = " + (true | false));\n        System.out.println(true + " | " + true + " = " + (true | true));\n        System.out.println("----------- Operador and (&) -----------");\n        System.out.println(false + " & " + false + " = " + (false & false));\n        System.out.println(false + " & " + true + " = " + (false & true));\n        System.out.println(true + " & " + false + " = " + (true & false));\n        System.out.println(true + " & " + true + " = " + (true & true));\n        System.out.println("----------- Operador not (!) -----------");\n        System.out.println("!" + false + " = " + !(false));\n        System.out.println("!" + true + " = " + !(true));\n    }\n}')


# #### Operaciones abreviadas
# 
# La siguiente tabla muestra los operadores escritos en forma abreviada:
# 
# |Operador |Ejemplo | Equivalente | Valor de la variable despues de la operación |
# |:---|:---|:---|:---|
# |```+=```|```x += 5;```|```x = x + 5;```|Valor anterior de ```x``` mas ```5```|
# |```-=```|```y -= 2;```|```y = y - 2;```|Valor anterior de ```y``` menos ```2```|
# |```*=```|```z *= 2;```|```z = z * 10;```|Valor anterior de ```z``` multiplicado por ```10```|
# |```/=```|```a /= b;```|```a = a / b;```|Valor anterior de ```a``` divido por ```b```|
# |```%=```|```c %= 3;```|```c = c % 3;```|Residuo de la division entre elvalor anterior de ```c``` y ```3```|
# 
# #### Operadores de incremento y decremento
# 
# Estos operadores permiten de manera abreviada incrementar o disminuir el valor de una variable en ```1```. La siguiente tabla permite comprender su funcionamiento:
# 
# |Nombre|Operador|Significado|
# |:---|:---|:---|
# |Pre-incremento|```++variable```|```variable = variable + 1```|
# |Post-incremento|```variable++```|```variable = variable + 1```|
# |Pre-decremento|```--variable```|```variable = variable - 1```|
# |Post-incremento|```variable--```|```variable = variable - 1```|

# In[7]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class IncDec {\n    public static void main(String[] args) {\n        int i = 0, j = 0;\n        System.out.println("i = " + i + ", j = " + j);  // i = 0, j = 0\n        i++;\n        j--;\n        System.out.println("i = " + i + ", j = " + j); // i = 1, j = -1\n        ++i;\n        --j;\n        System.out.println("i = " + i + ", j = " + j); // i = 2, j = -2\n    }\n}')


# Como se puede ver en el ejemplo anterior, tanto un incremento como un decremento de una variable implica la modificación de esta en 1. El efecto real de cuando una operacion es pre o post se ve cuando hay una asignación en la variable tal y como se muestra en la siguiente tabla:
# 
# |Operación|Significado|Observaciones|
# |:---|:---|:---|
# |```j = ++i```|```i = i + 1``` <br> ```j = i```|Incremento primero, asignación despues|
# |```j = i++```|```j = i``` <br> ```i = i + 1```|Asignación primero, incremento despues|
# |```j = --i```|```i = i - 1``` <br> ```j = i```|Decremento primero, asignación despues|
# |```j = i--```|```j = i``` <br> ```i = i - 1```|Asignación primero, decremento despues|

# In[10]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class IncDec2 {\n    public static void main(String[] args) {\n        int i = 0, j = 0;\n        System.out.println("i = " + i + ", j = " + j);  // i = 0, j = 0\n        System.out.println("j = ++i ");\n        j = ++i;\n        System.out.println("i = " + i + ", j = " + j);  // i = 1, j = 1\n        System.out.println("j = i++ ");\n        j = i++;\n        System.out.println("i = " + i + ", j = " + j);  // i = 2, j = 1\n        System.out.println("j = --i ");\n        j = --i;\n        System.out.println("i = " + i + ", j = " + j);  // i = 1, j = 1\n        System.out.println("j = i-- ");\n        j = i--;\n        System.out.println("i = " + i + ", j = " + j);  // i = 0, j = 1\n    }\n}')


# **Pregunta**: Suponga que se tienen las siguientes instrucciones:
# 
# ```java
# a = 5;
# b = 2 + (++a);
# ```
# 
# ¿Cuales son los valores finales de ```a``` y ```b```?

# #### Prioridad y asociatividad
# 
# En la siguiente tabla, podemos observar una lista de los operadores básicos en el lenguaje Java y su precedencia. En la tabla los operadores están por orden de precedencia de arriba abajo y de izquierda a derecha, de mayor a menor precedencia.
# 
# |Operadores	|Precedencia|
# |:---|:---|
# |Postfix|```expr++``` ```expr--```|
# |Unitario|```++expr``` ```--expr``` ```+expr``` ```-expr```  ```~```  ```!```|
# |Multiplicativo|```*``` ```/``` ```%```|
# |Aditivo|```+``` ```-```|
# |Shift|```>>``` ```<<``` ```>>>```|
# |Relacional (lógico)|```<``` ```>``` ```<=``` ```>=``` ```instanceof```|
# |Igualdad (lógico)|```==``` ```!=```|
# |Bitwise AND|```&```|
# |Bitwise exclusive OR|```^```|
# |Bitwise OR|```|```|
# |AND lógico|```&&```|
# |OR lógico|```||```|
# |Ternario|```? :```|
# |Asignación|```=``` ```+=``` ```-=``` ```*=``` ```/=``` ```%=``` ```&=``` ```^=``` ```|=``` ```<<=``` ```>>=``` ```>>>=```|

# ### 5. Expresiones, Sentencias y Bloques
# 
# * **Expresiones**: Una expresión se compone de variables, literales (valores), llamadas a métodos y operadores. A continuación se muestran algunos ejemplos de expresiones:
# 
# ```java
# peso/(estatura*estatura)
# a + b + c*(d - 3)    
# (x + y)/z - 4
# (edad >= 3) & (edad <= 10)
# ```
# 
# * **Sentencia**: En Java, a una oración en el lenguaje natural. Define una instrucción que damos usando el lenguaje. En Java las sentencias terminan en punto y coma (```;```). La siguiente tabla muestra diferentes tipos de sentencias:
# 
# |Tipos de sentencias |	Ejemplos|
# |:---|:---|
# |Expresiones de asignación	|```temperatura = 28;```|
# |Uso de operadores de incremento	|```temperatura++;```|
# |Invocación de métodos |```System.out.println("Hace calor!!");```|
# |Expresiones de creación de objetos | ```Avion unAvion = new Avion(); ```|
# |Sentencia de declaración | ```float nota = 2.9;```|
# |Sentencias de control de flujo | ```Las veremos posteriormente ```|
# 
# * **Bloques**: Un bloque es un conjunto de cero o más sentencias encerradas entre llaves (```{}```), y están permitidos en cualquier lugar que se permita una sola sentencia. Los bloques suelen delimitar las sentencias condicionales y de control de flujo (como los ciclos).
# 
# ```java
# { 
#     // Bloque
#     instruccion1;
#     instruccion2;
#     ...
#     instruccionN;
# }
# ```
# 
# A continuación se muestra un bloque de código con dos instrucciones:
# 
# ```java
# {
# 	int c = 1.4 + 1.6;
# 	System.out.println("La nota es: " + c);
# }      
# ```

# **Ejemplo 5**: A continuación se muestra un ejemplo que ilustra varias expresiones.

# In[30]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example5 {\n    public static void main(String[] args) {\n        System.out.println("3 / 2 + 5.0 = " + (3 / 2 + 5.0));\n        System.out.println("15.6 / 2 + 5 = " + (15.6 / 2 + 5));\n        System.out.println("4 + 5 / 2.0 = " + (4 + 5 / 2.0));\n        System.out.println("4 * 3 + 7 / 5 - 25.5 = " + (4 * 3 + 7 / 5 - 25.5));\n    }\n}')


# **Ejemplo 6**: El siguiente ejemplo muestra algunas operaciones con variables.

# In[31]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example6 {\n    public void main(string[] args) {\n        double i = 50.0;\n        double k = i + 50.0;\n        double j = k + 1;\n        System.out.println("j es " + j + " y k es " + k);\n    }\n}')


# **Ejemplo 7**: El siguiente calcula el area de un circulo de radio 20 haciendo uso de expresiones y variables.

# In[32]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example7 {\n    public static void main(String[] args) {\n        double radius; \n        double area;\n        \n        radius = 20;\n        area = radius * radius * 3.14159;\n        System.out.println("El area del circulo de " + radius + " es " + area);\n    }\n}')


# ### 6. Conversión de tipos (casting)
# 
# Por **casting** hacemos referencia a una conversion de datos. Existen dos tipos de casting: 
# * **coverción de tipo implícita**: Se da cuando un valor de un tipo de datos se trata automáticamente como otro tipo de datos. Por ejemplo cuando se evalua una expresión aritmética si el operador tiene operandos mezclados, el valor entero se trata como un valor de punto flotante con la parte decimal de cero. Por ejemplo:
# 
# ```java
# int x = 3;
# double y = 2.3, z;
# z = x + y;  // x es convertida de manera automatica a un dato tipo double antes de operar
# ```
# 
# * **Conversión explícita**: Java proporciona la conversión de tipo implícita mediante el uso de un **operador de casting** el cual tiene la siguiente forma:
# 
# ```java
# (nombreTipoDato) expresion
# ```
# 
# Si se hiciera el ejemplo anterior empleando el operador de casting se tendria el siguiente fragmento de código:
# 
# ```java
# int x = 3;
# double y = 2.3, z;
# z = (double)x + y;  // x es convertida de manera explicita haciendo un casting
# ```

# **Ejemplo 8**: A continuación se muestra el resultado de varios casting 

# In[35]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example8 {\n    public static void main(String[] args) {\n        System.out.println("(int)(7.9) = " + (int)(7.9));\n        System.out.println("(int)(3.3) = " + (int)(3.3));\n        System.out.println("(double)(25) = " + (double)(25));\n        System.out.println("(double)(5 + 3) = " + (double)(5 + 3));\n        System.out.println("(double)(15) / 2 = " + ((double)(15) / 2));\n        System.out.println("(double)(15 / 2) = " + ((double)(15 / 2)));\n        System.out.println("(int)(7.8 + (double)(15) / 2) = " + ((int)(7.8 + (double)(15) / 2)));\n        System.out.println("(int)(7.8 + (double)(15 / 2)) = " + ((int)(7.8 + (double)(15 / 2))));\n        System.out.println("(int)(\'A\') = " + (int)(\'A\'));\n        System.out.println("(char)(65) = " + (char)(65));\n        System.out.println("(int)(\'8\') = " + (int)(\'8\'));\n        System.out.println("(char)(56) = " + (char)(56));\n    }\n}')


# ### 7. Constantes
# Una constante es una localización de memoria cuyo contenido no se permite que cambie durante la ejecución de un programa. La forma tipica de definir una constante en Java se hace con la palabra reservada ```final``` tal y como se muestra a continuación:
# 
# ```java
# final dataType IDENTIFICADOR = valor;
# ```
# 
# A continuación se muestran algunos ejemplos:
# 
# ```java
# final double CENTIMETROS_POR_PULGADA = 2.54;
# final int NUM_DE_ESTUDIANTES = 20;
# final char ESPACIO = ' ';
# final double PAGO_SALARIO = 15.75;
# ```
# 
# Por convención las constantes se declaran con mayusculas.

# ### 8. String en java
# 
# Una **cadena de caracteres** es una secuencia de caracteres de cualquier tipo. En el caso de Java, las cadenas de caracteres se definen empleando la clase **String**.
# 
# Internamente, una variable del tipo **String**  contiene un arreglo (o array) de caracteres, es decir, de variables tipo **char**. Supongamos que ejecutamos la siguiente instruccion:
# 
# ```java
# String cadena;
# cadena ="Hola mundo";
# ```
# 
# Entonces el arreglo de caracteres equivalente será:
# 
# ![string](esqueleto/string.jpg)
# 
# En Java, el tipo **String**  no es un tipo de datos primitivo, sino una clase y por lo tanto tendrá atributos y métodos. Para conocer en detalle sobre esta clase, puede consultar el siguiente link [Class String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html) en el [API de Java](https://docs.oracle.com/javase/8/docs/).
# 
# Por ahora, sin entrar a profundizar en un String como clase, nos vamos a limitar a ver algunos aspectos de utilidad para lo que necesitamos. 
# 
# #### Declararación de Strings
# 
# Para declarar un string se emplea la siguiente sintaxis:
# 
# ```java
# String stringName <= initValue>;
# ```
# 
# Como se puede observar anteriormente, la inicialización de un String es opcional. Veamos algunos ejemplos
# 
# ```java
# /* Declaración sin inicializar */
# String inquilino1;             // Declaracion
# inquilino1 = "Ramon Valdez";   // Asignacion
# 
# /* Declaración inicializando */
# String inquilino2 = "Ramon Valdez"; // Declaracion e inicializacion
# ```
# 
# #### Operador + en los Strings
# 
# El operador ```+``` se emplea para concatenar strings (de manera similar a python). A continuación se muestran algunos ejemplos de uso:
# 
# ```java
# int value = 10;
# String str1 = "Hello " + "World";
# String str2, str3, str4;
# str2 = "The value is: " + 5;
# str3 = "The value is: " + value;
# str4 = "The value is: " + '\n' + 5);
# ```
# 
# A diferencia de python, en Java, la concatenación de Strings permite manejar varios tipos de datos. Por ejemplo:
# 
# ```java
# int a = 3, b = 4, c;
# String str = "a + b = " + a + " + " + b + " = " + (a + b));
# ```
# 
# Veamos algunos ejemplos.

# **Ejemplo 9**

# In[5]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example9 {\n    public static void main(String[] args) {\n        String nombre, nombreCompleto;\n        String apellido = "Pérez";\n        nombre = "Pepito";\n        nombreCompleto = nombre + " " + apellido;\n        System.out.println(nombreCompleto); // Imprime Pepito Pérez   \n    }\n}')


# **Ejemplo 10**

# In[9]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Example10 {\n    public static void main(String[] args) {    \n        int manzanas = 20;\n        String mensaje = "Hoy vendimos " + manzanas + " manzanas.";\n        System.out.println(mensaje);\n        System.out.println("Este es un ensayo " +\n                   "que usa + para escribir un mensaje largo " +\n                   "en varias lineas.");\n\n        System.out.println("The following will be printed " +\n                   "in a tabbed format: " +\n                   "\\n\\tFirst = " + 5 * 6 + ", " +\n                   "\\n\\tSecond = " + (6 + 4) + "," +\n                   "\\n\\tThird = " + 16.7 + "."); \n    }\n}')


# ## Sobre los identificadores
# 
# A la hora de nombrar las variables en Java (esto incluye nombres de variables, arreglos y objetos) se debe tener en cuenta lo siguiente:
# * Los nombres de variables en Java son **case-sensitive**, es decir, distinguen entre mayúsculas y minúsculas.
# * El nombre de una variable puede ser un identificador alfanumérico que empiece por una letra, el signo ```$```  o guion bajo (```_```). No se permiten espacios en blanco.
# * Se recomiendan palabras auto-descriptivas que no sean una palabra reservada del lenguaje (que se pueden conocer en la referencia de Java).
# * Para el nombrado de variables, se recomienda la notación camel-case, es decir: Si el nombre consta de una sola palabra, dicha palabra se escribe toda en minúsculas, si son dos o más palabras, se escribe la primera palabra toda en minúsculas, y las palabras subsecuentes, en minúscula, pero con la primera letra en mayúscula, así:  frecuencia, telefono, direccionResidencia, cambioTraseroActual.
# 
# ### Convenciones en java
# 
# * Los nombres de las variables deben comenzar con una letra minúscula y luego cambiar al título en mayúsculas. Ejemplo:
# 
# ```java
# int caTaxRate;
# ```
# 
# * Los nombres de las clases deben estar en mayúsculas y minúsculas. Sin embargo, a diferencia de las variables primitivas empezaran en mayuscula:
# 
# ```java
# public class BigLittle {
#    // Codigo de la clase...
# }
# ```
# 
# Finalmente, una regla general para nombrar variables y clases es que, con algunas excepciones, es que sus nombres tienden a ser sustantivos o frases nominales. Para mas información sobre las concenciones de nombrado puede consultar el link [Naming Conventions](http://java.sun.com/docs/codeconv/html/CodeConventions.doc8.html).

# ## Actividad de refuerzo
# 
# Analizar los codigos propuestos a continuación (tomados del siguiente [link](http://pythontutor.com/java.html#mode=edit)):

# In[12]:


get_ipython().run_cell_magic('tutor', '-l java -k', 'public class Variables {\n   public static void main(String[] args) {\n      String me = "me";\n      String you = "you";\n      String tmp = me;\n      me = you;\n      you = tmp;\n\n      int x = 5;\n      int y = 10;\n      int t = x;\n      x = y;\n      y = t;\n   }\n}')


# In[11]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Strings {\n   public static void main(String[] args) { \n      String a = "Hello, world!";\n      String b = "Hello, world!!".substring(0, 13);\n      String c = "Hello, ";\n      c += "world!";\n      String d = "Hello, w"+"orld!"; // constant expr, interned\n      String e = a.substring(0, 13);\n      System.out.println((a == b) + " " + a.equals(b));\n      System.out.println((a == c) + " " + a.equals(c));\n      System.out.println((a == d) + " " + a.equals(d));\n      System.out.println((a == e) + " " + a.equals(e));\n   }\n}')


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





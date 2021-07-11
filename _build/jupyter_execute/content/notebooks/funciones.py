#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip3 install tutormagic')
get_ipython().run_line_magic('load_ext', 'tutormagic')


# # Funciones en java #

# ## Formato general de un metodo ##
# 
# La forma general de un metodo en java se muestra a continuación
# 
# ```java
# return_type method_name( parameter_list ) 
# { 
#     declarations and statements... 
# } 
# ```
# 

# ### Ejemplo 1 ###
# 
# Codificar un metodo en java que permita calcular el cuadrado de un numero entero. Siga el formato general para ello:
# 
# **Solución**:
# A continuación se muestra la función en java:
# 
# ```java
# public static int square( int i ) { 
#    return i*i; 
# } 
# ```
# 
# **Donde:**
# * **Nombre del método**: square
# * **Tipo de dato retornado**: int
# * **Lista de parametros**: int i
# * **Expresión retornada**: i*i
# * **Sentencia de retorno**: return i*i
# 

# ## Invocación de un método ##
# 
# A continuación se muestra la forma de invocar un método:
# 
# ```java
# return_datatype variable = method_name( parameter_list ); 
# ```

# ### Ejemplo 2 ###
# 
# Invoque la función ```square``` definida en el **ejemplo 1** para calcular el valor del cuadrado de 10. Asigne este resultado a una variable entera llamada ``result``
# 
# **Solución**:
# 
# ```java
# int result = 5 * square( 10 ); // result is 5 * 100 = 500 
# ```

# ### Ejemplo 3 ###
# Hacer un programa que calcule todos los cuadrados de los numeros entre 1 y 10 empleando la funcion ```square```
# 
# **Solucion**: A continuación se muestra el programa completo y listo para ejecutarse, observe bien la parte asociada a la definición de la función y a la invocación de esta.

# In[3]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Math { \n    \n    /* Definicion de la funcion square */\n    public static int square( int i ) { \n        return i*i; \n    } \n    \n    public static void main( String[] args ) { \n        for( int i=1; i<=10; i++ ) { \n            System.out.println( "i=" + i + ", i*i=" + square( i ) /*invocacion de la funcion*/ ); \n        } \n    } \n} ')


# ## Funciones que no retornan ##
# 
# No toda función retorna valores una vez que es invocada. Para indicar esto en la definición de la función se coloca la palabra clave ```void``` tal y como se muestra en el siguiente elemplo.
# 
# ### Ejemplo 4 ###
# Realizar una función que imprima en pantalla el numero que se le pasa como argumento.
# 
# **Solución**: Notese el empleo de ```void``` en la parte del retorno de la función:
# 
# 
# ```java
# public static void printNumber( int n ) { 
#    System.out.println( "El numero es " + n ); 
# }
# ```
# 
# Como el metodo anterior no retorna ningun valor en la invocación no es necesario usar una variable a la cual se lleve un valor retornado, pues en el caso, no lo hay. El siguiente ejemplo clarifica esto.
# 
# ### Ejemplo 5 ###
# 
# Invocar la función print number de modo para visualizar el valor de 10 el cual previamente es asignado a una variable entera llamada n.
# 
# **Solución**: Notese que en la invocacación el resultado de la información no se lleva a nada.
# 
# ```java
# int n = 10; 
# printNumber( n ); // Note the result in not assigned to anything 
# ```
# 
# 

# ### Ejemplo 6 ###
# Codificar los siguiente métodos para los cuales se muestra la respectiva cabecera:
# 1. **square**: Función que calcula el cuadrado de un número.
# 
#     ```java
#     public static int square( int n )
#     ```
# 
# 2. **cube**: Función que calcula el cubo de un número.
# 
#     ```java
#     public static int cube( int n )
#     ```
#     
# 3. **toThePower**: Función que calcula la potencia cualquiera de un número.
# 
#     ```java
#     public static int toThePowe( int n, int power )
#     ```
# 
# 4. **factorial**: Calcula el factorial de un numero.
# 
#     ```java
#     public static int factorial( int n ) 
#     ```
# 5. **showNumber**: Funcón que imprime el resultado de una operación.
# 
#      ```java
#     public static void showNumber( String operation, int n )
#     ```
# 
# Una vez haya codificado los metodos anteriores haga las siguientes pruebas imprimiendo (para lo cual deberá hacer uso de la función ```showNumber```) en el metodo principal lo siguiente:
# 1. El cuadrado del numero 5
# 2. El cubo del numero 5
# 3. El numero 5 elevado a la potencia 4.
# 4. El factorial de 5.
# 
# **Solución**: A continuación se muestra la solución del programa anterior:

# In[4]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\npublic class Math2 { \n    \n    public static int square( int n ) { \n        return n*n; \n    } \n    public static int cube( int n ) { \n        return n*n*n; \n    } \n \n    public static int toThePower( int n, int power ) { \n        int result=n; \n        for( int i=0; i<power; i++ ) { \n            result *= n; \n        } \n        return result; \n    } \n\n    public static int factorial( int n ) { \n        int result = n; \n        for( int i=n-1; i>0; i-- ) { \n            result *= i; \n        } \n        return result; \n    } \n     \n    public static void showNumber( String operation, int n ) { \n        System.out.println( "The result of the " + operation + " is " + n );  \n    } \n    \n    public static void main( String[] args ) { \n        int a = 5;\n        showNumber( "Square", square( a ) ); \n        showNumber( "Cube", cube( a ) ); \n        showNumber( "To The Power", toThePower( a, 4 ) ); \n        showNumber( "Factorial", factorial( a ) ); \n    } \n} ')


# ## Pendiente ##
# 1. Scope.
# 2. Overloading.
# 3. Recursion.

# In[ ]:





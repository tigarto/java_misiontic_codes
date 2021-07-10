#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tigarto/TdeA/blob/master/Vector.ipynb)

# In[1]:


get_ipython().system('pip3 install tutormagic')
get_ipython().run_line_magic('load_ext', 'tutormagic')


# # Clase Vector # 

# La clase Vector se encuentra en el paquete java.util:
# * Tiene un comportamiento similar a un arreglo unidimensional
# * Guarda objetos o referencias de cualquier tipo, crece dinámicamente, sin necesidad de tener que programar operaciones adicionales; el arreglo donde almacena los elementos es de tipo Object.
# 
# La siguiente figura muestra los principales miembros de la clase ```Vector``` de los cuales analizaremos unos cuantos:
# 
# ![clase_vector](Vector.jpg)
# 

# ## Creación de un vector ##
# 
# Se utiliza el operador new de igual forma que se crea cualquier objeto; la clase Vector dispone de diversos constructores los cuales son:
# * **Vector()**: Crea un vector por defecto con una capacidad inicial de 10.
# * **Vector(int size)**: Crea un vector cuya capacidad inicial es especificada por **size**.
# * **Vector(int size, int incr)**: Crea un vector cuya capacidad inicial es de **size** y su incremento es especificado por **incr**. Este especifica el numero de elementos a asignar cada vez que un vector crece.
# * **Vector(Collection c)**: Crea un vector que contiene los elemtos de una colección **c**.
# 
# **Ejemplos**: A continuación se crean algunos objetos tipo Vector:
# 
# ```java
# Vector v1 = new Vector();
# Vector v2 = new Vector(100);
# Vector v3 = new Vector(v2);// v3 contiene los mismo elementos que v2
# ```

# ### Ejemplo de creación de un vector ###
# A continuación se crean algunos objetos tipo Vector usando los constructores anteriormente mostrados

# In[13]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\nimport java.util.Vector;\n\npublic class VectorTest {\n    public static void main(String[] args) {\n      Vector v1 = new Vector();        // v1 tiene un tamaño por default de 10\n      System.out.println("capacidad de v1: " + v1.capacity());  \n      Vector v2 = new Vector(4);       // v2 tiene un tamaño de 4\n      System.out.println("capacidad de v2: " + v2.capacity());    \n      Vector v3 = new Vector(v2);      // v3 tiene un tamaño de 4 (tamaño de v1)\n      System.out.println("capacidad de v3: " + v3.capacity());\n      Vector v4 = new Vector(6,2);     // v4 tiene un tamaño de 6 pero puede crecer 2 elementos mas\n      System.out.println("capacidad de v4: " + v4.capacity());\n        \n    }\n}')


# ## Metodos de la clase vector ##

# ## Inserción de elementos ##
# 
# Hay diferentes métodos para insertar o añadir elementos al vector; los elementos que insertan deben ser objetos, no pueden ser datos de tipos primitivos como int, char, etc. A continuación se muestran algunos métodos de inserción:
# 1. Añade el objeto después del último elemento del vector: 
# 
# ```java
# boolean add (Object ob)
# ```
# Si el elemento es exitosamente agregado al Vector retorna true, de clo contrario retorna false.
# 
# **Ejemplo**:
# 
# ```java
# Vector v = new Vector(); 
# v.add(1); 
# v.add(2); 
# ```
# 
# 2. Inserta un elemento en la posición especificada el Vector
# 
# ```java
# void add(int index, Object obj) 
# ```
# 
# 3. Añade el objeto después del último elemento del vector incrementando su tamaño por 1.
# 
# ```java
# void addElement(Object ob)
# ```
# 
# 4. Inserta el objeto en la posición p; los elementos posteriores a p se desplazan.
# 
# ```java
# void insertElementAt(Object ob, int p) 
# ```
# 
# Cuando se crea el vector con un tipo concreto, el elemento que se inserta ha de ser de ese tipo, o de uno derivado:
# 
# ```java
# Vector<String> vc = new Vector<String>();
# vc.add("Jueves"),
# vc.addElement (new Integer(12)); // error de tipo
# ```

# ### Probando los metodos anteriormente mostrados ###
# 
# 

# **Prueba del metodo**: ```boolean add (Object ob)```

# In[4]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\nimport java.util.Vector;\n\npublic class VectorTest {\n    public static void main(String[] args) {      \n      Vector v = new Vector(4);      \n      v.add(1);\n      v.add("Jajaja");\n      System.out.println("vector: " + v);\n      v.add("pfff");\n      v.add(2);\n      System.out.println("vector: " + v);\n      v.add(3);\n      System.out.println("vector: " + v);\n    }\n}')


# **Prueba del metodo**: ```void add(int index, Object obj)```

# In[18]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\nimport java.util.Vector;\n\npublic class VectorTest {\n    public static void main(String[] args) {      \n      Vector v = new Vector(4,2);   \n      System.out.println("capacidad del vector: " + v.capacity());\n      System.out.println("vector: " + v);\n      v.add(0,"jaja");\n      System.out.println("capacidad del vector: " + v.capacity());  \n      System.out.println("vector: " + v);\n      v.add(1,1);\n      System.out.println("capacidad del vector: " + v.capacity());  \n      System.out.println("vector: " + v);\n      v.add(2,"xxx");\n      System.out.println("capacidad del vector: " + v.capacity());  \n      System.out.println("vector: " + v);\n      v.add(3,"zzz");\n      System.out.println("capacidad del vector: " + v.capacity());\n      System.out.println("vector: " + v);\n      v.add(4,"zzz");\n      System.out.println("capacidad del vector: " + v.capacity());  \n      System.out.println("vector: " + v);\n      v.add(2,-23);\n      System.out.println("capacidad del vector: " + v.capacity());\n      System.out.println("vector: " + v);\n\n    }\n}')


# **Prueba del metodo**: ```void addElement(Object ob)```

# In[16]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\nimport java.util.Vector;\n\npublic class VectorTest {\n    public static void main(String[] args) {      \n      Vector v = new Vector(4);      \n      System.out.println("Capacidad de v: " + v.capacity());\n      System.out.println("Tamaño de v: " + v.size());\n      System.out.println("vector: " + v);\n      v.addElement(1);     // 1\n      System.out.println("Capacidad de v: " + v.capacity());\n      System.out.println("Tamaño de v: " + v.size());\n      System.out.println("vector: " + v);\n      v.addElement("zzzz");  // "zzzz"\n      v.addElement(2.3f);    // 2.3f\n      System.out.println("Capacidad de v: " + v.capacity());\n      System.out.println("Tamaño de v: " + v.size());\n      System.out.println("vector: " + v);\n      v.addElement(-3.21);   // -3.21\n      v.addElement(\'w\');     // \'w\'\n      System.out.println("Capacidad de v: " + v.capacity());\n      System.out.println("Tamaño de v: " + v.size());\n      System.out.println("vector: " + v);  \n    }\n}')


# **Prueba del metodo**: insertElement(Object ob, int p) 

# In[24]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\nimport java.util.Vector;\n\npublic class VectorTest {\n    public static void main(String[] args) {      \n      Vector v = new Vector(4,3);\n      v.insertElementAt(0,0);\n    }\n}')


# **Probando los distintos metodos**:
# 
# ```java
# import java.util.Vector;
# 
# public class VectorTest {
#     
#     public static void main(String[] args) {
#         // TODO code application logic here
#         Vector v1 = new Vector(4);
#         Vector v2 = new Vector(3,2);
#         System.out.println("Capacidad v1: " + v1.capacity());
#         System.out.println("v1: " + v1);
#         System.out.println("Capacidad v2: " + v2.capacity());
#         System.out.println("v2: " + v2);
#         v1.add("abc");
#         v1.add("cde");
#         v1.add(1);
#         v2.addAll(v1);
#         v2.add(-2.3f);
#         v2.addElement(4);
#         System.out.println("Capacidad v1: " + v1.capacity());
#         System.out.println("v1: " + v1);
#         System.out.println("Capacidad v2: " + v2.capacity());
#         System.out.println("v2: " + v2);
#         v1.insertElementAt(100, 0);
#         v2.insertElementAt(100, 4);
#         System.out.println("Capacidad v1: " + v1.capacity());
#         System.out.println("v1: " + v1);
#         System.out.println("Capacidad v2: " + v2.capacity());
#         System.out.println("v2: " + v2);
#         
#     }   
# }
# ```
# 
# **Salida**:
# 
# ```
# Capacidad v1: 4
# v1: []
# Capacidad v2: 3
# v2: []
# Capacidad v1: 4
# v1: [abc, cde, 1]
# Capacidad v2: 5
# v2: [abc, cde, 1, -2.3, 4]
# Capacidad v1: 4
# v1: [100, abc, cde, 1]
# Capacidad v2: 7
# v2: [abc, cde, 1, -2.3, 100, 4]
# ```

# ## Acceso a un elemento ##
# 
# Se accede a un elemento del vector por la posición que ocupa; los métodos de acceso devuelven el elemento con el tipo Object, entonces puede ser necesario realizar una conversión al tipo del objeto.
# 1. Devuelve el elemento cuya posición es p:
# 
# ```java
# Object elementAt(int p); 
# ```
# 
# 2. Devuelve el elemento cuya posición es p:
# 
# ```java
# Object get(int p);
# ```
# 
# 3. Devuelve el número de elementos:
# 
# ```java
# int size(); 
# ```
# 

# ## Eliminar un elemento ##
# 
# Un elemento se puede eliminar de distintas formas, una de ellas es por la posición que ocupa en el índice, a partir de esa posición el resto de elementos del vector se mueven una posición a la izquierda disminuyendo el número de elementos; otra forma es transmitir el objeto que se desea retirar del vector; también hay métodos de la clase para eliminar todos los elementos de una colección.
# 
# 1. Elimina elemento índice y el resto se reenumera:
# 
# ```java
# void removeElementAt(int indice);
# ```
# 
# 2. Elimina la primera aparición de op; devuelve true si realiza la eliminación.
# 
# ```java
# boolean removeElement (Object op);
# ```
# 
# 3. Elimina los elementos que están en gr.
# 
# ```java
# void removeAll(Collection gr);
# ```
# 
# 4. Elimina todos los elementos.
# 
# ```java
# void removeAllElements();
# ```

# ## Busqueda ##
# 
# Los diversos métodos de búsqueda de Vector devuelven la posición de la primera ocurrencia del objeto buscado, o bien verdadero-falso según el resultado de la búsqueda.
# 
# 1. Verifica si el vector contiene a op devolviendo true lo encuentra
# 
# ```java
# boolean contains(Object op);
# ```
# 
# 2. Devuelve la (primera si hay varias) posición en la que se encuentra op. En caso de no encontrarse op en el vector el valor retornado es -1. 
# 
# ```java
# int indexOf(Object op);
# ```
# 

# **Ejemplo**: Utilizar un vector para guardar números racionales

# In[3]:


get_ipython().run_cell_magic('tutor', '-l java -k', '\nimport java.util.Vector;\n\nclass Racional { \n  private int x, y;\n  public Racional(int x, int y) {\n    this.x = x;\n    this.y = y;\n  }\n  public void mostrar() {\n    System.out.println(x + "/" + y);\n  }\n}\n\npublic class VectorNumero {\n  static final int N = 3;\n  public static void main(String[] args) {\n    Vector num = new Vector();\n    for(int i = 1; i <= N; i++) {\n      Racional q;\n      q = new Racional(3 * i, 3 * i % 7 + 1);\n      num.addElement(q);    \n    }\n    // recuperación de los elementos\n    int k;\n    k = num.size(); // número de elementos\n    for (int i = 0; i < N; i++) {\n      Racional q;\n      q = (Racional)num.elementAt(i);\n      q.mostrar();\n    }  \n  }\n}')


# En el siguiente [enlace](https://www.geeksforgeeks.org/java-util-vector-class-java/) se encuentran ejemplos utiles para aterrizar conceptos.

# ## Referencias ##
# 1. https://docs.oracle.com/javase/8/docs/api/java/util/Vector.html
# 2. https://www.tutorialspoint.com/java/util/java_util_vector.htm
# 3. https://www.geeksforgeeks.org/java-util-vector-class-java/

# In[ ]:





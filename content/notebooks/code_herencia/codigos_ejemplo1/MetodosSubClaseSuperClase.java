/*
Ejemplo tomado del libro: Programación en Java. Del analisis al diseño de programas (D. s. Malik)

Capitulo 10.
*/

public class MetodosSubClaseSuperClase {
  public static void main(String[] args) {
    Rectangulo miRectangulo1 = new Rectangulo(); 
    Rectangulo miRectangulo2 = new Rectangulo(8, 6); 
    Caja miCaja1 = new Caja(); 
    Caja miCaja2 = new Caja(10, 7, 3); 
    System.out.println("miRectangulo1: "
                       + miRectangulo1); 
    System.out.println("Area de miRectangulo1: "
                       + miRectangulo1.area()); 
    System.out.println("miRectangulo2: "
                       + miRectangulo2); 
    System.out.println("Area de miRectangulo2: "
                       + miRectangulo2.area()); 
    System.out.println("miCaja1: " + miCaja1); 
    System.out.println("Area superficial de miCaja1: "
                       + miCaja1.area());
    System.out.println("Linea 15: Volumen de miCaja1: "
                       + miCaja1.volumen());
    System.out.println("miCaja2: " + miCaja2);
    System.out.println("Area superficial de miCaja2: "
                       + miCaja2.area());
    System.out.println("Volumen de miCaja2: "
                       + miCaja2.volumen()); 
  }
}
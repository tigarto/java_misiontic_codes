/*
Ejemplo tomado del libro: Programación en Java. Del analisis al diseño de programas (D. s. Malik)

Capitulo 10.
*/

public class Rectangulo { 
    private double longitud;
    private double ancho;
    
    public Rectangulo() {
      longitud = 0;
      ancho = 0;
    }
    public Rectangulo(double l, double a) {
      setDimension(l, a);
    }
    
    public void setDimension(double l, double a)  {
      if (l >= 0)
        longitud = l;
      else
        longitud = 0;
      if (a >= 0)
        ancho = a;
      else
        ancho = 0;
    }
    
    public double getLongitud() {
      return longitud;
    }
    
    public double getAncho() {
      return ancho;
    }
    
    public double area() {
      return longitud * ancho;
    }
  
    public double perimetro() {
      return 2 * (longitud + ancho);
    }
  
    public String toString() {
      return ("Longitud = " + longitud + "; Ancho = " + ancho);
    }
  }
  
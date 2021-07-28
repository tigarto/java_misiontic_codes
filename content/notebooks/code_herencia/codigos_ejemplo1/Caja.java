/*
Ejemplo tomado del libro: Programación en Java. Del analisis al diseño de programas (D. s. Malik)

Capitulo 10.
*/

public class Caja extends Rectangulo {
    private double altura; 
    
    public Caja() {
      //La definicion es como se da abajo
      super();
      altura = 0;
    }
    
    public Caja(double l, double a, double h) {
      //La definicion es como se da abajo
      super(l, a);
      altura = h;
    }
    
    public void setDimension(double l, double a, double h) {
      //Establece la longitud, el ancho y la altura de la caja La definicion es como se da abajo
      super.setDimension(l, a);
      if (h >= 0) {
        altura = h;
      }
      else {
        altura = 0;
      }
    }
    
    public double getAltura() {
      return altura;
    }
    
    public double area() {
      //Retorna el area superficial
      //La definicion es como se da abajo
      return 2 * (getLongitud() * getAncho() + 
            getLongitud() * altura + 
            getAncho() * altura);
    }
    
    public double volumen() {
      //Retorna el volumen
      //La definicion es como se da abajo
      return super.area()*altura;
    }
    
    public String toString() {
      //Retorna longitud, ancho y altura de la caja como
      //una cadena. La definicion es como se da abajo.
      return super.toString() //recupera longitud y ancho
      + "; Height = " + altura;
    }
  }
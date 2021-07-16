import java.util.Scanner;

public class ArticuloIVA {
    public static void main(String[] args) {
        // Variables
        final float IVA = 0.19f;
        float imp = 0;
        float precioBase;
        float precioNeto;

        // Objeto tipo Scanner
        Scanner in = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner

        // Entrada de datos
        System.out.print("Ingrese el precio del articulo: ");
        precioBase = in.nextFloat();    

        // Calculo del impuesto y el precio neto
        if (precioBase >= 1000000) {
            imp = IVA*precioBase;
            precioNeto = preciBase + imp;
        }
        // Despliegue de los resultados
        System.out.println();
        System.out.println("******** Colilla de pago ********");
        System.out.println("+ Subtotal -> " + precioBase);
        System.out.println("+ Impuesto -> " + imp);
        System.out.println("---------------------------------");
        System.out.println("+    Total -> " + precioNeto);
        System.out.println("*********************************");
    }
}

import java.util.Scanner;

public class FinDeSemana {
    public static void main(String[] args) {
        // Variables
        byte dia;

        // Objeto tipo Scanner
        Scanner input = new Scanner(System.in);  // Declaracion de un objeto (llamado teclado) de la clase Scanner

        //Ingreso de la nota numerica
        System.out.print("Ingrese el numero del dia: ");
        
        dia = input.nextByte();

        // Validación de la nota numerica y obtencion de la nota en letras dependiendo la tabla
        switch (dia) {
            case 1:               
            case 2:                
            case 3:                
            case 4:                
            case 5:
                System.out.println("Dia de la semana");
                break;                
            case 6:
            case 7:
                System.out.println("Dia del fin de semana");
                break;
            default:
                System.out.println("Dia invalido");
        }
    }
}

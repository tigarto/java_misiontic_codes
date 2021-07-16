import java.util.Scanner;

public class DiaSemana {
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
                System.out.println("Lunes");
                break;
            case 2:
                System.out.println("Martes");
                break;
            case 3:
                System.out.println("Miercoles");
                break;
            case 4:
                System.out.println("Jueves");
                break;                
            case 5:
                System.out.println("Viernes");
                break;                
            case 6:
                System.out.println("Sabado");
                break;                
            case 7:
                System.out.println("Domingo");
                break;
            default:
                System.out.println("Dia invalido");
        }
    }
}

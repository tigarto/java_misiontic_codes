// Fig. 10.6: EmpleadoPorHoras.java
// La clase EmpleadoPorHoras extiende a Empleado.

public class EmpleadoPorHoras extends Empleado
{
private double sueldo; // sueldo por hora
private double horas; // horas trabajadas por semana

// constructor con cinco argumentos
public EmpleadoPorHoras( String nombre, String apellido, String nss,
double sueldoPorHoras, double horasTrabajadas )
{
super( nombre, apellido, nss );
establecerSueldo( sueldoPorHoras ); // valida y almacena el sueldo por horas
establecerHoras( horasTrabajadas ); // valida y almacena las horas trabajadas
} // fin del constructor de EmpleadoPorHoras con cinco argumentos

// establece el sueldo
public void establecerSueldo( double sueldoPorHoras )
{
sueldo = ( sueldoPorHoras < 0.0 ) ? 0.0 : sueldoPorHoras;
} // fin del método establecerSueldo

// devuelve el sueldo
public double obtenerSueldo()
{
return sueldo;
} // fin del método obtenerSueldo

// establece las horas trabajadas
public void establecerHoras( double horasTrabajadas )
{
horas = ( ( horasTrabajadas >= 0.0 ) && ( horasTrabajadas <= 168.0 ) ) ?
horasTrabajadas : 0.0;
} // fin del método establecerHoras

// devuelve las horas trabajadas
public double obtenerHoras()
{
return horas;
} // fin del método obtenerHoras

// calcula los ingresos; sobrescribe el método abstracto ingresos en Empleado
public double ingresos()
{
if ( obtenerHoras() <= 40 ) // no hay tiempo extra
return obtenerSueldo() * obtenerHoras();
else
return 40 * obtenerSueldo() + ( obtenerHoras() - 40 ) * obtenerSueldo() * 1.5;
} // fin del método ingresos

// devuelve representación String de un objeto EmpleadoPorHoras
public String toString()
{
return String.format( "empleado por horas: %s\n%s: $%,.2f; %s: %,.2f",
super.toString(), "sueldo por hora", obtenerSueldo(),
"horas trabajadas", obtenerHoras() );
} // fin del método toString
} // fin de la clase EmpleadoPorHoras


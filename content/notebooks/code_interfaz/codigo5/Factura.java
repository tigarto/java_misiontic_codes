// Fig. 10.12: Factura.java
// La clase Factura implementa a PorPagar.

public class Factura implements PorPagar
{
private String numeroPieza;
private String descripcionPieza;
private int cantidad;
private double precioPorArticulo;

// constructor con cuatro argumentos
public Factura( String pieza, String descripcion, int cuenta,
double precio )
{
numeroPieza = pieza;
descripcionPieza = descripcion;
establecerCantidad( cuenta ); // valida y almacena la cantidad
establecerPrecioPorArticulo( precio ); // valida y almacena el precio por artículo
} // fin del constructor de Factura con cuatro argumentos

// establece el número de pieza
public void establecerNumeroPieza( String pieza )
{
numeroPieza = pieza;
} // fin del método establecerNumeroPieza

// obtener número de pieza
public String obtenerNumeroPieza()
{
return numeroPieza;
} // fin del método obtenerNumeroPieza

// establece la descripción
public void establecerDescripcionPieza( String descripcion )
{
descripcionPieza = descripcion;
} // fin del método establecerDescripcionPieza

// obtiene la descripción
public String obtenerDescripcionPieza()
{
return descripcionPieza;
} // fin del método obtenerDescripcionPieza

// establece la cantidad
public void establecerCantidad( int cuenta )
{
cantidad = ( cuenta < 0 ) ? 0 : cuenta; // cantidad no puede ser negativa
} // fin del método establecerCantidad

// obtener cantidad
public int obtenerCantidad()
{
return cantidad;
} // fin del método obtenerCantidad

// establece el precio por artículo
public void establecerPrecioPorArticulo( double precio )
{
precioPorArticulo = ( precio < 0.0 ) ? 0.0 : precio; // valida el precio
} // fin del método establecerPrecioPorArticulo

// obtiene el precio por artículo
public double obtenerPrecioPorArticulo()
{
return precioPorArticulo;
} // fin del método obtenerPrecioPorArticulo
9 // devuelve representación String de un objeto Factura
public String toString()
{
return String.format( "%s: \n%s: %s (%s) \n%s: %d \n%s: $%,.2f",
"factura", "numero de pieza", obtenerNumeroPieza(), obtenerDescripcionPieza(),
"cantidad", obtenerCantidad(), "precio por articulo", obtenerPrecioPorArticulo() );
} // fin del método toString

// método requerido para realizar el contrato con la interfaz PorPagar
public double obtenerMontoPago()
{
return obtenerCantidad() * obtenerPrecioPorArticulo(); // calcula el costo total
} // fin del método obtenerMontoPago
} // fin de la clase Factura

![Tec de Monterrey](../../images/logotecmty.png)
# Compañía de Transporte

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    edad = int(input("Ingresa tu edad: "))
    # Escribe el código adecuado para completar el programa
    # Para pedir el dato de la idetificación oficial emplea este mensaje:
    # "¿Tienes identificación oficial? (s/n): "



if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema
Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, África, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:
<table >
 <thead >
        <tr>
            <th >Zona</th>
            <th >Ubicación</th>
            <th >Costo/gramo</th>
        </tr>
    </thead>
   <Body>
     <tr >
            <td>1</td>
            <td>América del Norte</td>
            <td>24.00 dlls</td>
     </tr>
     <tr>
            <td>2</td>
            <td>América Central</td>
            <td>20.00 dlls</td>
        </tr>
        <tr  >
            <td>3</td>
            <td>América del Sur</td>
            <td>21.00 dlls</td>
        </tr>
        <tr  >
            <td>4</td>
            <td>Europa</td>
            <td>12.00 dlls</td>
        </tr>
        <tr  >
            <td>5</td>
            <td>Asia</td>
            <td>16.00 dlls</td>
        </tr>
        <tr  >
            <td>6</td>
            <td>África</td>
            <td>24.00 dlls</td>
        </tr>
   </Body>
</table>
<br>Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realice un programa que utilice funciones para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega poner INCORRECTO. El rechazo también se  aplica si se pone una zona no valida. 
</p>
<h2>Entrada</h2>
dos números el cual es el peso y la zona 
<h2>Salida</h2>
el precios del paquete enviado  o la  palabra INCORRECTO según sea el caso

<h2>Ejemplo1</h2>
<h3>Entradar</h3>
<br>2500.00
<br>1
<h3>Salida</h3>
<br>60000.0

<h2>Ejemplo2</h2>
<h3>Entradar</h3>
<br>20000.00
<br>1
<h3>Salida</h3>
<br>INCORRECTO

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `python -m pytest --tb=short -v`,
subela a tu repositorio en GitHub, con el proceso de commit + push.

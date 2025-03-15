# Bash

<p align="center"><img src ="../images/bash.png" width="450"/></p>


## Shells en Linux
Linux ofrece varios tipos de shells, entre los cuales destacan:

- **Bourne Shell** (`sh`)
- **C Shell** (`csh`)
- **Korn Shell** (`ksh`)
- **TC Shell** (`tcsh`)
- **Bourne Again Shell** (`bash`)
- **Z Shell** (`zsh`)

**Bash** es el shell más popular y ampliamente utilizado en sistemas Linux. Combina características del Korn Shell y C Shell, cumpliendo con el estándar IEEE POSIX P1003.2/ISO 9945.2 Shell and Tools.

## Sintaxis Básica de Bash
- Utiliza el alfabeto latino, dígitos arábigos, símbolos de puntuación y algunas palabras clave.
- Los scripts deben comenzar con `#!/bin/bash` para indicar que son ejecutables bajo Bash.
- Las instrucciones terminan con un salto de línea o un punto y coma `;`.

## Variables en Bash
- Las variables se almacenan como cadenas de texto por defecto, aunque se pueden usar en operaciones aritméticas.
- No es necesario declarar las variables antes de asignarles un valor.
- Las cadenas con espacios o caracteres especiales deben ir entre comillas:
  - Comillas dobles (`""`): permiten la expansión de variables.
  - Comillas simples (`''`): evitan la expansión de variables.
- Ejemplo:
  ```bash
  nombre="Francisco"
echo "Hola, $nombre!"
  ```

## Variables de Entorno
- Existen dos tipos principales:
    - **Variables Locales:** solo disponibles en el entorno actual del script.
    - **Variables de Entorno:** accesibles por todo el sistema y visibles mediante el comando `env`.

- Variables comunes:
    - `PATH`: Directorios donde se buscan los comandos.
    - `HOME`: Directorio personal del usuario.
    - `USER`, `LOGNAME`: Nombre del usuario actual.
    - `PWD`: Directorio de trabajo actual.
    - `SHELL`: Ruta del shell actual.
    - `LANG`: Configuración regional del sistema.

## Variables Especiales en Bash
- `$0`: Nombre del script.
- `$1-$9`: Parámetros posicionales.
- `$#`: Cantidad de parámetros pasados.
- `$*` y `$@`: Todos los parámetros.
- `$?`: Estado de salida del último comando.
- `$$`: ID del proceso actual.
- `$!`: ID del último proceso en segundo plano.

## Sustitución de Comandos
- Para almacenar la salida de un comando en una variable:
  ```bash
  fecha=$(date)
echo "La fecha actual es: $fecha"
  ```

## Evaluación Aritmética
- Bash soporta operaciones aritméticas con:
  - `let`
  - `$[expresion]`
  - `$((expresion))`
- Nota: Bash no soporta operaciones de punto flotante directamente.

  ```bash
  a=5
  b=3
  suma=$((a + b))
echo "La suma es $suma"
  ```

## Estructuras Condicionales
- Condicionales básicas:
  ```bash
  if [ $a -gt $b ]; then
    echo "$a es mayor que $b"
elif [ $a -eq $b ]; then
    echo "$a es igual a $b"
else
    echo "$a es menor que $b"
fi
  ```

- Operadores de Comparación:
  - **Cadenas:** `=`, `!=`, `-n` (no vacío), `-z` (vacío).
  - **Números:** `-eq`, `-ne`, `-gt`, `-lt`, `-ge`, `-le`.
  - **Archivos:** `-f` (archivo regular), `-d` (directorio), `-r` (lectura), `-w` (escritura), `-x` (ejecución).

## Bucles y Estructuras de Control
- **For Loop:**
  ```bash
  for archivo in /etc/*; do
    echo "$archivo"
done
  ```
- **While Loop:**
  ```bash
  contador=0
  while [ $contador -lt 5 ]; do
    echo "Contador: $contador"
    contador=$((contador+1))
done
  ```
- **Until Loop:**
  ```bash
  until [ $contador -eq 0 ]; do
    echo "Contador: $contador"
    contador=$((contador-1))
done
  ```
- **Case Statement:**
  ```bash
  read -p "Introduce una opción (y/n): " opcion
  case $opcion in
    y|Y) echo "Has elegido sí";;
    n|N) echo "Has elegido no";;
    *) echo "Opción no válida";;
esac
  ```

## Arreglos en Bash
```bash
miArray=(manzana naranja platano)
echo ${miArray[1]} # Imprime "naranja"
```
- Para recorrer:
  ```bash
  for fruta in "${miArray[@]}"; do
    echo "$fruta"
done
  ```

## Operaciones con Cadenas
- Longitud de una cadena:
  ```bash
  echo ${#miVariable}
  ```
- Extracción de subcadena:
  ```bash
  echo ${miVariable:2:4}
  ```
- Reemplazo:
  ```bash
  echo ${miVariable/manzana/pera}
  ```

## Funciones en Bash
```bash
mi_funcion() {
  echo "Hola desde una función!"
}
mi_funcion
```

## Expresiones Regulares
- Para verificar si una cadena contiene números:
  ```bash
  if [[ $var =~ [0-9]+ ]]; then
    echo "Contiene números"
  fi
  ```

## Casos de Estudio
1. **Contar líneas en un archivo:**
   ```bash
   i=1
   while read linea; do
     echo "$i : $linea"
     i=$((i+1))
   done < archivo.txt
   ```
2. **Verificar existencia de un archivo:**
   ```bash
   if [ -f "archivo.txt" ]; then
     echo "El archivo existe"
   fi
   ```
3. **Mostrar información del sistema:**
   ```bash
   echo "Fecha: $(date)"
   echo "Tiempo de actividad: $(uptime)"
   ```

## Recursos Recomendados
- [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/)
- [Linux Shell Scripting Tutorial](https://www.shellscript.sh/)
- [Documentación POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/)

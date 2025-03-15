# Linux

<p align="center"><img src ="../images/linux.png" width="250"/></p>


## Conceptos Clave

### ¿Qué es un Sistema Operativo?
Un sistema operativo (SO) es un software que gestiona los recursos del hardware y proporciona servicios a los programas de aplicación. Linux es un SO de tipo Unix, conocido por su estabilidad y seguridad.

### Historia y Evolución de Linux
- Linux fue creado en **1991** por **Linus Torvalds** como un proyecto personal.
- Basado en el sistema operativo **Unix**, Linux fue desarrollado como una alternativa de código abierto.
- Con el tiempo, se convirtió en el sistema operativo más utilizado en servidores, supercomputadoras, dispositivos IoT y sistemas embebidos.
- La comunidad de desarrollo es global y colaborativa, con distribuciones (distros) que adaptan Linux a diferentes necesidades.

### Familia de Sistemas Linux
- **Distribuciones Basadas en Debian**: Ubuntu, Linux Mint, Kali Linux.
- **Distribuciones Basadas en RedHat**: Fedora, CentOS, RHEL.
- **Distribuciones Basadas en Arch**: Arch Linux, Manjaro.
- **Distribuciones Basadas en Slackware**: Slackware, Salix.
- Cada distribución varía en facilidad de uso, enfoque y herramientas disponibles.

### ¿Por qué Elegir Linux?
- **Código Abierto**: Libre para usar, modificar y distribuir.
- **Seguridad**: Menos vulnerable a virus y ataques.
- **Estabilidad y Rendimiento**: Ideal para servidores y entornos de alto rendimiento.
- **Flexibilidad**: Adaptable para distintas necesidades y dispositivos.
- **Comunidad Activa**: Gran cantidad de foros, documentación y soporte colaborativo.

### Estructura de Directorios en Linux
- `/` - Directorio Raíz.
- `/bin/` - Comandos esenciales.
- `/sbin/` - Comandos del sistema para administradores.
- `/home/` - Directorios personales de los usuarios.
- `/var/` - Archivos variables, como logs.
- `/etc/` - Archivos de configuración del sistema.
- `/tmp/` - Archivos temporales.
- `/usr/` - Archivos de usuario, como aplicaciones y documentación.

### Comandos Esenciales
- `ls` - Lista los archivos de un directorio.
- `cd` - Cambia de directorio.
- `mkdir` - Crea un nuevo directorio.
- `rm` - Elimina archivos o directorios.
- `sudo` - Ejecuta comandos con privilegios de administrador.
- `man <comando>` - Muestra el manual del comando.

### Instalación y Ejecución de Programas
- **Debian/Ubuntu**: `sudo apt update && sudo apt install <paquete>`
- **Fedora/RedHat**: `sudo dnf install <paquete>`
- **Arch Linux**: `sudo pacman -S <paquete>`
- Para ejecutar un programa: `./programa` (si tiene permisos de ejecución).

### Pipes y Redirección de Entrada/Salida
- **Pipes (`|`)**: Conectan la salida de un comando con la entrada de otro.
  - Ejemplo: `ls | grep "archivo"`
- **Redirección (`>`, `>>`)**: Direccionan la salida a un archivo.
  - Ejemplo: `echo "Hola" > saludo.txt`

### Gestión de Usuarios y Grupos
- `useradd` - Crear un nuevo usuario.
- `passwd` - Cambiar contraseña de un usuario.
- `usermod` - Modificar un usuario existente.
- `groupadd` - Crear un nuevo grupo.
- `chown` - Cambiar la propiedad de un archivo.

### Permisos y Propiedad de Archivos
- Cada archivo tiene tres tipos de permisos: **lectura (r), escritura (w) y ejecución (x)**.
- Modificar permisos: `chmod 755 archivo`
- Cambiar propietario: `chown usuario:grupo archivo`
- Ver permisos: `ls -l`



## Conclusión
Linux es un sistema operativo poderoso, flexible y seguro, ideal tanto para usuarios principiantes como para administradores de sistemas. Conocer su historia, estructura y comandos básicos es esencial para desenvolverse en entornos informáticos modernos. Dominar Linux no solo mejora las habilidades técnicas, sino que también abre puertas a oportunidades en el ámbito de la tecnología y la administración de sistemas.

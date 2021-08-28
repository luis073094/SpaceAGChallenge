## Instalacion
1. Crear una instancia con Ubuntu en AWS EC2

2. Conectarse via SSH y ejecutar:
```bash
    sudo apt install apt-transport-https ca-certificates curl software-properties-common gnupg-agent
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu `lsb_release -cs` test"
    sudo apt update
    sudo apt install docker-ce
```

3. Conectarse por FTP y subir el proyecto

4. Via SSH ir a la carpeta donde se encuentra el archivo Dockerfile y ejecutar
```bash
    sudo docker-compose build
    sudo docker-compose up
```

5. Testear!
## SpaceAG Challenge

### Servicio en produccion

* Ruta API: [http://ec2-3-128-198-18.us-east-2.compute.amazonaws.com/v1/field_workers/](http://ec2-3-128-198-18.us-east-2.compute.amazonaws.com/v1/field_workers/)

* Ruta GraphQL: [http://ec2-3-128-198-18.us-east-2.compute.amazonaws.com/graphql](http://ec2-3-128-198-18.us-east-2.compute.amazonaws.com/graphql)

### Instalacion
1. Crear una instancia con Ubuntu en AWS EC2

2. Conectarse via SSH y ejecutar:
```bash
    sudo apt install apt-transport-https ca-certificates curl software-properties-common gnupg-agent
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu `lsb_release -cs` test"
    sudo apt update
    sudo apt install docker-ce
```

3. Conectarse via FTP y subir el proyecto

4. Via SSH ir a la carpeta donde se encuentra el archivo Dockerfile y ejecutar
```bash
    sudo docker-compose build
    sudo docker-compose up
```

5. Testear!


### Ejemplos para GraphQL
```bash
mutation {
  create_worker: createWorker(firstName: "Luis", lastName: "Mundaca", function: "") {
    worker {
 		 id
      firstName
      lastName
      function
      createdAt
    }
  }
}


mutation {
  update_worker: updateWorker(id: "4eef2cc6-60a9-45a6-a01d-18a661b4a1d8",
    firstName: "Plastic", lastName: "Plastic2", function: "Harvest") {
    worker {
 		 id
      firstName
      lastName
      function
      createdAt
    }
  }
}


mutation {
  partial_update_worker: partial_updateWorker(id: "4eef2cc6-60a9-45a6-a01d-18a661b4a1d8",
    input: {firstName: "Plastic33"}
  ) {
    worker {
      id
      firstName
      lastName
      function
      createdAt
    }
  }
}


mutation {
  delete_worker: deleteWorker(id: "aa8d3b04-4283-4146-97aa-936796fcc692") {
    response
  }
}
```
# [UT02](./index.md)

## Ejercicio paso a paso
```
PR0200: Entorno de producción de desarrollo contenerizado 

1.- Ejecutamos en la terminal de Powershell docker network create shared_network para crear la red externa shared_network, si ya la teniamos nos da error, sino nos saldrá algo como: 1bfa47323e55e9f2e3221b7de4c53b5147cc7c3dfbde87fc84b62eccf250dc06 

2.- Ahora vamos a OdooDesarrollo con cd "C:\Users\leonb\OdooDesarrollo" y ejecutamos notepad docker-compose.yml y en la ventana de bloc de notas que nos sale le ponemos el compose.yml que nos dio el profesor modificado para tener 4 servicios: 2 de postgres y dos de odoo. 

3.- Levantamos los contenedores con docker compose up –d.  

4.- Vamos a http://localhost:8070 http://localhost:8096
```

## compose.yml
```
version: "3.9"

services:

  postgres_dev:
    image: postgres:14
    container_name: postgres_dev
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: odoo
      POSTGRES_PASSWORD: odoo
    volumes:
      - "C:/Users/leonb/OdooDesarrollo/OdooDesarrollo/dataPG:/var/lib/postgresql/data"
    networks:
      - shared_network

  odoo_dev:
    image: odoo:16
    container_name: odoo_dev
    depends_on:
      - postgres_dev
    environment:
      HOST: postgres_dev
      USER: odoo
      PASSWORD: odoo
    ports:
      - "8070:8069"
    volumes:
      - "C:/Users/leonb/OdooDesarrollo/OdooDesarrollo/volumesOdoo/addons:/mnt/extra-addons"
      - "C:/Users/leonb/OdooDesarrollo/OdooDesarrollo/volumesOdoo/filestore:/var/lib/odoo/filestore"
      - "C:/Users/leonb/OdooDesarrollo/OdooDesarrollo/volumesOdoo/sessions:/var/lib/odoo/sessions"
    command: --dev=all
    networks:
      - shared_network

  postgres_prod:
    image: postgres:14
    container_name: postgres_prod
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: odoo
      POSTGRES_PASSWORD: odoo
    networks:
      - shared_network

  odoo_prod:
    image: odoo:16
    container_name: odoo_prod
    depends_on:
      - postgres_prod
    environment:
      HOST: postgres_prod
      USER: odoo
      PASSWORD: odoo
    ports:
      - "8096:8069"
    volumes:
      - "C:/Users/leonb/OdooDesarrollo/OdooDesarrollo/volumesOdoo/addons:/mnt/extra-addons"
    networks:
      - shared_network

networks:
  shared_network:
```

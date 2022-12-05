# GRUPO 25
# Sistema Conversión Cloud - Entorno Tradicional


## Requisitos
- Instalar docker y docker compose
- Instalar Postman


## Pasos para ejecutar el sistema
- git clone https://github.com/J8A9902/DSN-Equipo-ERLJ.git
- cd DSN-Equipo-ERLJ
- docker-compose up --build o docker-compose up --build -d (para segundo planno) 
- docker ps, esto para validar los contenedores en ejecución, los cuales deben ser:
  - auth-microservice
  - auth-database
  - tasks-microservice
  - tasks-database
  - redis
  - nginx
  
![image](https://user-images.githubusercontent.com/98363516/197398728-af1a24bc-a930-4762-97c4-e2756eb06d29.png)


## Pasos para obtener las colecciones de postman
- Abrir Postman
- Ir a la pestaña Collections
- Click en Import

![image](https://user-images.githubusercontent.com/98363516/197397742-65ae4aa5-1e99-4cec-a8a8-7794a08076a8.png)

- Importar desde la carpeta DSN-Equipo-ERLJ/postman
![image](https://user-images.githubusercontent.com/98363516/197397653-e6adf3b2-ea6f-4821-af34-d1fd2e725063.png)

- CLick en import
- Ir Environments y activar Nginx Environment
- En Environments, cambiar los environmets de nginx (Nginx Environment) si así se desea(por defecto funcionan)< 
## Requirements

- docker
- node.js

## Back-end setup

1. Build and up the docker container

```bash
docker-compose -f local.yml up --build
```

2. In a new bash, create the first super user

```bash
docker-compose run --rm django python manage.py createsuperuser
```

3. The server is now running and you can access to Django Admin with your credentials: http://localhost:8000/api/admin/

## Front-end setup

1. Go to folder `FrontEnd`

2. Install dependecies

```
npm install -- or -- yarn install
```

3. Run the application

```
npm run dev -- or -- yarn dev
```

4. The application is now running and you can access to the page at http://localhost:5173/. Important: The back-end must be running at this point.

## Postman setup

From root folder, download the file `innovatica.postman_collection.json`, and import it into Postman

## Video references

See folder `Videos` for a quick view of the application running

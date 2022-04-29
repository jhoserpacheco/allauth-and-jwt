# Re-estructuración de proyecto acorde a la arquitectura

Se re-estructuro el microservicio de tal forma que se adecuara a la arquitectura planteada para el sistema

![Actual componente en la Arquitectura](https://github.com/Sachica/allauth-and-jwt/blob/master/readme_imgs/this_component.PNG)

De esta forma se definieron los siguientes modulos:

## user_module
Responsable de la administración de usuarios, necesaria la previa autenticación(JWT)

### Endpoints
#### CRUD Endpoints http://127.0.0.1:8000/users/api/v1/user/
```json
    "GET": {
        "Listado":        "/users/api/v1/user/",
        "Buscar por id":  "/users/api/v1/user/{id}/"
    },
    "POST": {
        "Crear":          {"/users/api/v1/user/", RequestBody(JSON)}
    },
    "PUT": {
        "Actualizar":     {"/users/api/v1/user/", RequestBody(JSON)}
    },
    "DELETE": {
        "Eliminar":       {"/users/api/v1/user/{id}/"}
    }
```
#### Custom Endpoints http://127.0.0.1:8000/users/api/v1/u/
```json
{
    "GET": {
        "Ver perfil":     "/users/api/v1/u/profile/"
    }
}
```

## auth_module
Responsable de la autenticación de usuarios y manejo de JWT
#### AUTH Endpoints http://127.0.0.1:8000/users/api/v1/auth/
```json
    "POST": {
        "Verificar token":    {"/users/api/v1/auth/token/verify/", RequestBody(JSON)},
        "Refrescar token":    {"/users/api/v1/auth/token/refresh/", RequestBody(JSON)}
    }
```

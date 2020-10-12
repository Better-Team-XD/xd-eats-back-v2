# XD Eats backend

[![flask badge](https://img.shields.io/badge/flask-1.1.2-blue)](https://pypi.org/project/Flask/)
[![pymongo badge](https://img.shields.io/badge/PyMongo-3.11.0-green)](https://pypi.org/project/pymongo/)

## Project Description

Backend of XD Eats application (Python version). We gathered data from [przepisy.pl](https://www.przepisy.pl/) just to fill database. We used webscraping script for this purpose<br>
[Link](https://github.com/Better-Team-XD/hacknarok-script) to webscraping script <br>
[Link](https://github.com/Better-Team-XD/hacknarok-back) to original Java version <br>
[Link](https://github.com/Better-Team-XD/hacknarok-web) to frontend

## API
### Add recipe into system

```http
POST http://localhost:5000/api/v1/recipes
```
Headers:
| Key | Value | Description |
| :--- | :--- | :--- |
| `password` | `string` | **Required**. Password to system defined in password.py |
| `Content-Type` | `application/json` | **Required**.|

Example body:
```javascript
{
    "category": "Śniadanie",
    "imageUrl": "https://s3.przepisy.pl/przepisy3ii/img/variants/800x0/owsianka.jpg",
    "ingredients": [
        "Płatki owsiane",
        "Mleko 2%",
        "Jabłka",
        "Suszone morele",
        "Rodzynki",
        "Orzechy włoskie",
        "Cynamon do smaku"
	],
    "name": "Owsianka",
    "url": "https://www.przepisy.pl/przepis/owsianka"
}
```

Return message:
```javascript
{
    "content": null,
    "message": "5f848f6f94e64fb9148236e7",  //id of added recipe
    "status": "SUCCESS"
}
```

### Get all recipes from system

```http
GET http://localhost:5000/api/v1/recipes
```

Return message

```javascript
{
    "content": [
        {
            "_id": "5f50db95c4783da430c1eb80",
            "category": "Śniadanie",
            "imageUrl": "https://s3.przepisy.pl/przepisy3ii/img/variants/800x0/owsianka.jpg",
            "ingredients": [
                "Płatki owsiane",
                "Mleko 2%",
                "Jabłka",
                "Suszone morele",
                "Rodzynki",
                "Orzechy włoskie",
                "Cynamon do smaku"
            ],
            "name": "Owsianka",
            "url": "https://www.przepisy.pl/przepis/owsianka"
        },
        {
            "_id": "5f50dbe0c4783da430c1eb8b",
            "category": "Śniadanie",
            "imageUrl": "https://s3.przepisy.pl/przepisy3ii/img/variants/800x0/placki-owsiane.jpg",
            "ingredients": [
                "Olej",
                "Oliwa z oliwek",
                "Pieprz",
                "Jajko",
                "Sól",
                "Mąka",
                "Posiekana natka pietruszki",
                "Płatki owsiane",
                "Posiekany szczypiorek",
                "Kefir",
                "Mąka kukurydziana"
            ],
            "name": "Placki owsiane",
            "url": "https://www.przepisy.pl/przepis/placki-owsiane"
        },
        .
        .
        .
    ],
    "message": "data loaded",
    "status": "SUCCESS"
}
```

### Get all ingredients from system

```http
GET http://localhost:5000/api/v1/ingredients
```

Return message
```javascript
{
    "content": [
        {
            "_id": "5f50db95c4783da430c1eb79",
            "name": "Płatki owsiane"
        },
        {
            "_id": "5f50db95c4783da430c1eb7a",
            "name": "Mleko"
        },
        {
            "_id": "5f50db95c4783da430c1eb7b",
            "name": "Jabłka"
        },
        {
            "_id": "5f50db95c4783da430c1eb7c",
            "name": "Suszone morele"
        },
        .
        .
        .
        
    ],
    "message": "data loaded",
    "status": "SUCCESS"
}

```

### Get recipes based on provided ingredients

This endpoint returns 6 recipes which contain at leat one recipe from provided ingredients, sorted by "missing" field descending. 

```http
POST http://localhost:5000/api/v1/matches
```

Headers:
| Key | Value | Description |
| :--- | :--- | :--- |
| `Content-Type` | `application/json` | **Required**.|

Example body:

```javascript
{
	"category": "Śniadanie",    //Available categories: "Śniadanie", "Obiad", "Kolacja"
	"ingredients": [
		"Ser żółty",
		"Mleko"
	]
}
```

Return message (simmilar to get recipes  return message):

```javascript
{
    "content": [
        {
            "category": "Śniadanie",
            "imageUrl": "https://s3.przepisy.pl/przepisy3ii/img/variants/800x0/omlet-z-szynka-i-warzywami.jpg",
            "ingredients": [
                "Plastry szynki",
                "Przyprawa w mini kostkach pietruszka knorr",
                "Jajka",
                "Papryka",
                "Świeżo mielony czarny pieprz",
                "Mleko",
                "Masło"
            ],
            "missing": 6,           // number of missing ingredients
            "name": "Omlet z szynką i warzywami",
            "url": "https://www.przepisy.pl/przepis/omlet-z-szynka-i-warzywami"
        },
        {
            "category": "Śniadanie",
            "imageUrl": "https://s3.przepisy.pl/przepisy3ii/img/variants/800x0/omlet-po-meksykansku.jpg",
            "ingredients": [
                "Jajka",
                "Mleko",
                "Przyprawa w mini kostkach smażona cebula knorr",
                "Czerwona papryka",
                "Cebula dymka",
                "Świeża kolendra",
                "Ser żółty",
                "Papryczka chili"
            ],
            "missing": 6,         // number of missing ingredients
            "name": "Omlet po meksykańsku",
            "url": "https://www.przepisy.pl/przepis/omlet-po-meksykansku"
        },
        .
        .
        .
    ]
    "message": "data loaded",
    "status": "SUCCESS"
}
        
```

## Contributors :hamburger:
<table>
  <tr>
    <td align="center"><a href="https://github.com/kraleppa"><img src="https://avatars1.githubusercontent.com/u/56135216?s=460&u=359e017d16c70a31d3bdb086172308cc6f045acf&v=4" width="100px;" alt=""/><br /><sub><b>Krzysztof Nalepa</b></sub></a><br /></td>
    </td>
  </tr>
</table>  

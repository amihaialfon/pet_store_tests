
class Config:
    BASE_URL = "http://petstore.swagger.io/v2"
    HEADERS = {"Content-Type": "application/json"}
    NEW_PET = {
        "id": 12345,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Rex",
        "photoUrls": [
            "https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Friendly"
            }
        ],
        "status": "available"
    }

# Product catalogue
This product catalogue is based on a store product/category model.

## Usage
All of the categories will have the format
```json
{
"message": "Short name of the category at hand",
"data": "Returned data from the request"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all categories
***Definition***

`GET /categories`

**Response**
- `200 OK` on success
```json
[
  {
    "id": "fast-food",
    "name": "Fast food items"
  },
  {
    "id": "womens-clothes",
    "name": "Women's clothes"
  }
]
```

### Adding a new category
***Definition***

`POST /categories`

**Arguments**
- `"id":string` a globally unique name of the category
- `"name":string` a name which would be displayed on the website

If a category already exists with said id then the category will be overwritten.

**Response**
- `201 Created` on success
```json
 {
    "id": "men",
    "name": "Men's clothes"
 }
```

### Display only one category

`GET /category/<id>`

**Response**
- `404 Not Found` if the category does not exist
- `200 OK` on success

```json
 {
    "id": "men",
    "name": "Men's clothes"
 }
```

### Delete a category
**Definition**

`DELETE /categories/<id>`

**Response**
- `404 Not Found` if the category does not exist
- `204 No Content` if the deletion was successful

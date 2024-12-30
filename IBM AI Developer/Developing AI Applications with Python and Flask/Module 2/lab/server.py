from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/")
def index():
   return {
      "message" : "Hello, World!"
   }

@app.route("/no_content")
def no_content():
   """return 'No content found' with a status of 204
   
   Returns:
      string: No content found
      status code: 204
   """
   return {"message": "No content found"}, 204

@app.route("/exp")
def index_explicit():
   """Return a successful response with message "Hello, World!""
   
   Returns:
      resp: response object containing message "Hello, World!" and status code 200
   """
   resp = make_response(
      {"message" : "Hello, World!"}
   )
   resp.status_code = 200

   return resp

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404
    

@app.route('/name_search')
def name_search():
   # Get the query parameter 'name'
   name = request.args.get('q')

   # Check if 'name' is provided

   if not name:
      # If 'name' is not provided, return a JSON response with a 400 Bad Request status code
      return {"message": "Invalid input parameter"}, 422
   
   
   for person in data:

         # Check if the first name or last name of the person matches the query parameter 'name'
         if person['first_name'].lower() == name.lower():
            # If a match is found, return a JSON response with the person's data
            return person
           
   # If the for loop fails to match a person, return a 404 response
   return {"message": "Person not found"}, 404
      
@app.route('/count', methods=['GET'])
def count():
   """Returns the number of people in the database

   Returns:
      json response: number of people in the database
   """

   return {"data count": len(data)}, 200

@app.route('/person/<uuid:unique_identifier>', methods=['GET'])
def find_by_uuid(unique_identifier):
    """Finds a person by their unique identifier (UUID)

    Args:
        unique_identifier (str): UUID of the person

    Returns:
        json response: person data if found, or error message if not found
    """

    for person in data:
        if person['id'] == str(unique_identifier):
            return person

    return {"message": "Person not found"}, 404

@app.route('/person/<uuid:unique_identifier>', methods=['DELETE'])
def delete_by_uuid(unique_identifier):
    """Removes a person by their unique identifier (UUID)

    Args:
        unique_identifier (str): UUID of the person

    Returns:
        json response: success message if deleted, or error message if not found
    """

    for i, person in enumerate(data):
        if person['id'] == str(unique_identifier):
            data.pop(i)
            return {"message": f"Person with ID {unique_identifier} deleted"}, 200

    return {"message": "Person not found"}, 404

@app.route("/person", methods=["POST"])
def add_by_uuid():
    
   person = request.get_json()

   if not person:
       return {"mesage": "Invalid input parameter"}, 422
   
   data.append(person)
   return {"message": "Person added successfully"}, 200

@app.errorhandler(404)
def api_not_found(error):
    return {"message": str(error)}, 404
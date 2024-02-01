from flask import Flask, jsonify #importing necessary modules
import requests


app = Flask(__name__)

CAT_API_URL = "https://api.thecatapi.com/v1/images/search" #URL for fetching an image

@app.route('/randomcat', methods=['GET']) #binding the function to the '/randomcat'
def get_random_cat():
    try:
        response = requests.get(CAT_API_URL) #sending a GET request to the cat API
        data = response.json() #parsing the JSON response
        image_url = data[0]['url'] #extracting the URL of the cat image from the response
        return jsonify({'image_url': image_url}) #returning the cat image URL in JSON format

    except Exception as e: #handling exceptions
        return jsonify({'error': str(e)}), 500 #returning an error message with status code 500 Internal Server Error


if __name__ == '__main__':
    app.run(debug=True) #running th FLask application in debug mode
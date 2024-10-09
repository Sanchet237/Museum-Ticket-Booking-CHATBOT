from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot import get_chatbot_response


app = Flask(__name__,template_folder='payment')
CORS(app)  # Enable CORS for all routes

def calculate_price(people_data):
    total_price = 0
    for person in people_data:
        if person.lower() == 'india' or person.lower() == 'indian':
            total_price += 20  # Price for Indian citizens
        else:
            total_price += 500  # Price for non-Indian citizens
    return total_price

# Home route that accepts query parameters
@app.route('/')
def home():
    number_of_people = request.args.get('number_of_people', 1, type=int)
    nationality = request.args.get('nationality', 'India')
    
    # Create a list with repeated nationality based on the number of people
    people_data = [nationality] * number_of_people
    
    # Calculate total price
    total_price = calculate_price(people_data)

    # Pass the calculated data to the HTML template
    return render_template('index.html', number_of_people=number_of_people, nationality=nationality, total_price=total_price)


@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data.get('message')
    
    response = get_chatbot_response(user_input, "user1")
    return jsonify({'response': response})






if __name__ == "__main__":
    app.run(debug=True)

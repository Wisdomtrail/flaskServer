from flask import Blueprint, jsonify, request
import requests
import os

controller_routes = Blueprint('controller_routes', __name__)
SPOONACULAR_BASE_URL = 'https://api.spoonacular.com/recipes'
SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY')


@controller_routes.route('/recipes/complexSearch', methods=['GET'])
def get_recipes():
    # Get query parameters from the request
    query = request.args.get('query', default='pasta', type=str)
    max_fat = request.args.get('maxFat', default=25, type=int)
    number = request.args.get('number', default=2, type=int)

    # Construct the Spoonacular API URL
    api_url = f"{SPOONACULAR_BASE_URL}/complexSearch?query={query}&maxFat={max_fat}&number={number}&apiKey={SPOONACULAR_API_KEY}"

    try:
        # Make the API request
        response = requests.get(api_url)

        # If response is successful (status code 200), return the data
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                'offset': data['offset'],
                'number': data['number'],
                'results': data['results'],
                'totalResults': data['totalResults']
            })
        else:
            return jsonify({'error': 'Unable to fetch data from Spoonacular API'}), 500

    except requests.exceptions.RequestException as e:
        # Log the error if there is an issue with the request
        app.logger.error(f"Error while requesting data from Spoonacular API: {e}")
        return jsonify({'error': str(e)}), 500


@controller_routes.route('/recipes/<int:recipe_id>/similar', methods=['GET'])
def get_similar_recipes(recipe_id):
    # Construct the Spoonacular API URL to fetch similar recipes
    api_url = f"{SPOONACULAR_BASE_URL}/{recipe_id}/similar?apiKey={SPOONACULAR_API_KEY}"

    try:
        # Make the API request to get similar recipes
        response = requests.get(api_url)

        # If response is successful (status code 200), return the data
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                'similar_recipes': data
            })
        else:
            return jsonify({'error': 'Unable to fetch similar recipes from Spoonacular API'}), 500

    except requests.exceptions.RequestException as e:
        # Log the error if there is an issue with the request
        app.logger.error(f"Error while requesting similar recipes from Spoonacular API: {e}")
        return jsonify({'error': str(e)}), 500


@controller_routes.route('/ingredients/substitutes', methods=['GET'])
def get_ingredient_substitutes():
    # Get the ingredient name from the query parameters
    ingredient_name = request.args.get('ingredientName', type=str)
    
    if not ingredient_name:
        return jsonify({'error': 'Please provide an ingredient name'}), 400

    # Construct the Spoonacular API URL for ingredient substitutes
    api_url = f"https://api.spoonacular.com/food/ingredients/substitutes?ingredientName={ingredient_name}&apiKey={SPOONACULAR_API_KEY}"

    try:
        # Make the API request to get ingredient substitutes
        response = requests.get(api_url)

        # If response is successful (status code 200), return the data
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                'ingredient': ingredient_name,
                'substitutes': data.get('substitutes', []),
                'message': data.get('message', 'No substitutes found.')
            })
        else:
            return jsonify({'error': 'Unable to fetch ingredient substitutes from Spoonacular API'}), 500

    except requests.exceptions.RequestException as e:
        # Log the error if there is an issue with the request
        app.logger.error(f"Error while requesting ingredient substitutes from Spoonacular API: {e}")
        return jsonify({'error': str(e)}), 500


@controller_routes.route('/recipes/<int:recipe_id>/information', methods=['GET'])
def get_recipe_information(recipe_id):
    # Construct the Spoonacular API URL for recipe information
    api_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={SPOONACULAR_API_KEY}"

    try:
        # Make the API request to get recipe information
        response = requests.get(api_url)

        # If response is successful (status code 200), return the data
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Unable to fetch recipe information from Spoonacular API'}), 500

    except requests.exceptions.RequestException as e:
        # Log the error if there is an issue with the request
        app.logger.error(f"Error while requesting recipe information from Spoonacular API: {e}")
        return jsonify({'error': str(e)}), 500


@controller_routes.route('/recipes/queries/analyze', methods=['GET'])
def analyze_recipe_query():
    # Get the query parameter from the request
    query = request.args.get('q', type=str)
    
    if not query:
        return jsonify({'error': 'Please provide a query to analyze'}), 400

    # Construct the Spoonacular API URL for analyzing the recipe query
    api_url = f"https://api.spoonacular.com/recipes/queries/analyze?q={query}&apiKey={SPOONACULAR_API_KEY}"

    try:
        # Make the API request to analyze the recipe query
        response = requests.get(api_url)

        # If response is successful (status code 200), return the data
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Unable to analyze recipe query from Spoonacular API'}), 500

    except requests.exceptions.RequestException as e:
        # Log the error if there is an issue with the request
        app.logger.error(f"Error while analyzing recipe query from Spoonacular API: {e}")
        return jsonify({'error': str(e)}), 500


@controller_routes.route('/mealplanner/generate', methods=['GET'])
def generate_meal_plan():
    # Get the timeFrame parameter from the query (defaults to 'day' if not provided)
    time_frame = request.args.get('timeFrame', 'day')

    # Construct the Spoonacular API URL for generating a meal plan
    api_url = f"https://api.spoonacular.com/mealplanner/generate?timeFrame={time_frame}&apiKey={SPOONACULAR_API_KEY}"

    try:
        # Make the API request to generate the meal plan
        response = requests.get(api_url)

        # If response is successful (status code 200), return the data
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Unable to generate meal plan from Spoonacular API'}), 500

    except requests.exceptions.RequestException as e:
        # Log the error if there is an issue with the request
        app.logger.error(f"Error while generating meal plan from Spoonacular API: {e}")
        return jsonify({'error': str(e)}), 500


@controller_routes.route('/recipes/<int:recipe_id>/analyzedInstructions', methods=['GET'])
def get_analyzed_instructions(recipe_id):
    # Construct the Spoonacular API URL for fetching analyzed instructions
    api_url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey={SPOONACULAR_API_KEY}"

    try:
        # Make the API request to get analyzed instructions
        response = requests.get(api_url)

        # If response is successful (status code 200), return the data
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Unable to fetch analyzed instructions from Spoonacular API'}), 500

    except requests.exceptions.RequestException as e:
        # Log the error if there is an issue with the request
        app.logger.error(f"Error while requesting analyzed instructions from Spoonacular API: {e}")
        return jsonify({'error': str(e)}), 500

@controller_routes.route('/food/jokes/random', methods=['GET'])
def get_random_food_joke():
    # Construct the Spoonacular API URL for a random food joke
    api_url = f"https://api.spoonacular.com/food/jokes/random?apiKey={SPOONACULAR_API_KEY}"

    try:
        # Make the API request to get a random food joke
        response = requests.get(api_url)

        # If response is successful (status code 200), return the joke data
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Unable to fetch a random food joke from Spoonacular API'}), 500

    except requests.exceptions.RequestException as e:
        # Log the error if there is an issue with the request
        app.logger.error(f"Error while requesting random food joke from Spoonacular API: {e}")
        return jsonify({'error': str(e)}), 500

# Django REST Framework Sample Project - README

This is a sample Django REST Framework project that includes two basic API views: "two_sum" and "contact". The "two_sum" API receives two integer numbers as parameters and returns their sum as a JSON response. The "contact" API returns a basic contact object in JSON format.

## Prerequisites

To run this project, you need to have Python 3 installed on your computer. [https://www.python.org/downloads/](https://www.python.org/downloads/).

## Installation

1.  Clone this repository:


`git clone https://github.com/Mohammad-SS/cbno.git` 

2.  Create and activate a virtual environment:

shell

    python3 -m venv venv
    source venv/bin/activate

` 

3.  Install the dependencies:

`$ pip install -r requirements.txt` 

4.  You can rewrite environment files in .env file in the root of proejct

## Usage

To run the project, execute the following command in the terminal:

`$ python manage.py runserver` 

Then, open your web browser and go to `http://localhost:8000/`. You should see the API root page with links to the two views.

### API URLs

-   **/api/two_sum/**: Returns the sum of two integers x and y as a JSON response.
-   **/api/contact/**: Returns a basic contact object in JSON format.

## Testing

To run the tests, execute the following command in the terminal:

`$ python manage.py test` 

This will run all the tests in the `tests.py` file and display the results in the terminal.

## Conclusion

This is a simple Django REST Framework project that shows how I start a basic API project .
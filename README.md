# NFC URL Redirection Flask App

This Flask application provides an API for managing NFC tags and their associated URLs. It allows updating the configurable URL for a specific NFC tag ID, adding a list of NFC IDs with matching URLs, and handling NFC tag redirection.

## Prerequisites

To run this application, you need the following:

- Python 3.x installed on your machine.
- The Flask package installed. You can install it using `pip install flask`.
- An SQLite database file named `nfc_data.db` placed in the same directory as the script. This file will be automatically created if it doesn't exist.

## Installation and Setup

1. Clone or download the repository to your local machine.

2. Install the required dependencies by running the following command in your terminal or command prompt:

   ```shell
   pip install flask

3. Run the Flask application by executing the following command in the project directory:

   ```shell
    python app.py

    The application will start running on http://localhost:5000.

## API Endpoints
1. Update URL for a Specific NFC Tag ID
    Endpoint: /update_url
    Method: POST

    Update the configurable URL for a specific NFC tag ID.

    Request body (JSON):
    nfc_tag_id: The ID of the NFC tag to update.
    url: The new URL to associate with the NFC tag.
    Example Request:

    ```json
    curl -X POST -H "Content-Type: application/json" -d '{"nfc_tag_id": "0001", "url": "https://example.com"}' http://localhost:5000/update_url

    Response:

    - If the update is successful, the response will be URL updated successfully.
    - If the NFC tag ID is not found, the response will be NFC tag not found.

2. Add a List of NFC IDs with Matching URLs
    Endpoint: /add_nfc_ids
    Method: POST

    Add a list of NFC IDs with their matching URLs.

    Request body (JSON):
    nfc_ids: A dictionary where the keys are NFC tag IDs and the values are the corresponding URLs.
    Example Request:

    ```json
    curl -X POST -H "Content-Type: application/json" -d '{"nfc_ids": {"0002": "https://example.com", "0003": "https://another-example.com"}}' http://localhost:5000/add_nfc_ids

    Response:

    - If the addition is successful, the response will be NFC IDs added successfully.

3. NFC Tag Redirection
    Endpoint: /redirect/<nfc_tag_id>
    Method: GET

    Handle NFC tag redirection. When a user visits this endpoint with an NFC tag ID, it redirects them to the associated URL.

    <nfc_tag_id>: The ID of the NFC tag.
    Example Request:

    Open the following URL in a web browser:
    ```bash
    http://localhost:5000/redirect/0001

    Response:

    - If the NFC tag ID is found, the user is redirected to the associated URL.
    - If the NFC tag ID is not found, the response will be NFC tag not found.

4. Home Route
    Endpoint: /
    Methods: GET, POST

    This is the home route that displays the index.html page. It provides a form to enter an NFC ID and submit it for redirection. If the request method is POST, it redirects the user to the NFC tag redirection endpoint with the entered NFC ID.

    Example Request:

    Open the following URL in a web browser:
    ```arduino
    http://localhost:5000/

    Response:

    - If the request method is GET, the index.html page is rendered, displaying a form to enter an NFC ID.
    - If the request method is POST and a valid NFC ID is entered, the user is redirected to the associated URL.
    - If the request method is POST and the entered NFC ID is not found, the response will be NFC tag not found.

## Conclusion
This Flask application provides a simple API for managing NFC tags and their associated URLs. It allows updating URLs, adding new NFC tags with URLs, and handling NFC tag redirection. By following the provided API endpoints and examples, you can easily integrate this functionality into your own NFC tag management system.

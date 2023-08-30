# Weather App using React Frontend and Django Backend

This repository contains a Weather App that provides real-time weather information using React for the frontend and Django for the backend. The backend serves as an API to fetch weather data from a third-party source, and the frontend presents this data to the user in a user-friendly graphical interface.

## Features

* User-friendly interface to search and display weather information for a specific location.
* Real-time weather data fetched from a reliable third-party API.
* Responsive design that works well on both desktop and mobile devices.

## Technologies Used

### Frontend

* React: A popular JavaScript library for building user interfaces.
* Axios: A promise-based HTTP client for making API requests.
* Material-UI: A UI component library that provides pre-designed components for a consistent and modern look.

### Backend

* Django: A high-level Python web framework that simplifies backend development.
* Django Rest Framework (DRF): A powerful toolkit for building Web APIs in Django applications.

## Installation and Setup

Frontend

1. Navigate to the `frontend_dir directory:` `cd frontend_dir`.
2. Install the dependencies: `npm install`.
3. Start the development server: `npm start`.
4. The frontend will be accessible at `http://localhost:3000`.
5. Backend
6. Navigate to the `backend_dir` directory: `cd backend_dir`.
7. (Optional) Create a virtual environment: `python -m venv venv`.
8. Activate the virtual environment:

   * On Windows: `venv\Scripts\activate`
   * On macOS and Linux: `source venv/bin/activate`
9. Install the required packages: `pip install -r requirements.txt`.
10. Apply migrations to set up the database: `python manage.py migrate`.
11. Start the Django development server: `python manage.py runserver`.
12. The backend API will be accessible at `http://localhost:8000/api`.

## Configuration

### Frontend

* The frontend configuration can be found in the `frontend/src/config.js` file. You can modify the API base URL if needed.

### Backend

* The backend settings can be found in the `backend_dir/backend/settings.py` file. Configure the database, allowed hosts, and other settings as required.

## Usage

1. Access the Weather App frontend by opening a web browser and navigating to `http://localhost:3000`.
2. Enter a location in the search bar to retrieve real-time weather information.

## Credits

* This Weather App uses weather data from a third-party API (mention the API source and provide a link).

## Demo

Check out the live version of the project [here](http://54.197.97.97/).

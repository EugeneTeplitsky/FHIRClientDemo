# FHIR Client Service

This is a demo Python Flask application that serves as a client service for interacting with a FHIR (Fast Healthcare Interoperability Resources) server. It provides a set of RESTful API endpoints for creating and retrieving FHIR resources such as patients, observations, medications, and conditions.

## Prerequisites

Before running the application, make sure you have the project prerequisites installed:
```
pip install -r requirements.txt
```

## Configuration

The application requires certain configuration settings to be set up before running. These settings are stored in a `.env` file. Create a file named `.env` in the project root directory and provide the following configuration variables:

```
APP_ID=your_app_id
API_BASE=your_fhir_server_base_url
APP_SECRET=your_app_secret
REDIRECT_URI=your_redirect_uri
```

Replace `your_app_id`, `your_fhir_server_base_url`, `your_app_secret`, and `your_redirect_uri` with the appropriate values for your FHIR server and application setup.

## Running the Application

To run the application locally, execute the following command in the project root directory:

```
flask run --debug
```

The application will start running on `http://localhost:5000`.

## API Endpoints

The application provides the following API endpoints:

### Patient

- `GET /patient/<patient_id>`: Retrieve a patient by ID.
- `POST /patient`: Create a new patient.

### Observation

- `GET /observation/<observation_id>`: Retrieve an observation by ID.
- `POST /observation`: Create a new observation.

### Medication

- `GET /medication/<medication_id>`: Retrieve a medication by ID.
- `POST /medication`: Create a new medication.

### Condition

- `GET /condition/<condition_id>`: Retrieve a condition by ID.
- `POST /condition`: Create a new condition.

## FHIR Compliance

This application aims to comply with the FHIR v4 specification. It uses the `fhirclient` library to interact with the FHIR server and handle FHIR resources.

## Error Handling

The application handles common error scenarios, such as resource not found (404 error). When a requested resource is not found, the application returns an appropriate error response in JSON format.
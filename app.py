from flask import Flask, jsonify, request, redirect
from fhirclient import client
from fhirclient.models import patient, observation, medication, condition
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Configure the FHIR client settings
settings = {
    'app_id': os.getenv('APP_ID'),
    'api_base': os.getenv('API_BASE'),
    'app_secret': os.getenv('APP_SECRET'),
    'redirect_uri': os.getenv('REDIRECT_URI')
}

# Initialize the FHIR client
smart = client.FHIRClient(settings=settings)


@app.route('/', methods=['GET'])
def index():
    return redirect(smart.authorize_url, code=302)


@app.route('/patient/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    # Retrieve a patient by ID
    patient_instance = patient.Patient.read(patient_id, smart.server)

    if patient_instance is None:
        return jsonify({'error': 'Patient not found'}), 404

    # Convert the patient to a JSON-serializable format
    patient_data = patient_instance.as_json()

    return jsonify(patient_data)


@app.route('/patient', methods=['POST'])
def create_patient():
    # Create a new patient
    patient_data = request.json

    # Create a new Patient instance from the received data
    patient_instance = patient.Patient(patient_data)

    # Save the patient to the FHIR server
    patient_instance.create(smart.server)

    return jsonify({'message': 'Patient created successfully', 'patient_id': patient_instance.id})


@app.route('/observation', methods=['POST'])
def create_observation():
    # Create a new observation
    observation_data = request.json

    # Create a new Observation instance from the received data
    observation_instance = observation.Observation(observation_data)

    # Save the observation to the FHIR server
    observation_instance.create(smart.server)

    return jsonify({'message': 'Observation created successfully', 'observation_id': observation_instance.id})


@app.route('/observation/<observation_id>', methods=['GET'])
def get_observation(observation_id):
    # Retrieve an observation by ID
    observation_instance = observation.Observation.read(observation_id, smart.server)

    if observation_instance is None:
        return jsonify({'error': 'Observation not found'}), 404

    # Convert the observation to a JSON-serializable format
    observation_data = observation_instance.as_json()

    return jsonify(observation_data)


@app.route('/medication', methods=['POST'])
def create_medication():
    # Create a new medication
    medication_data = request.json

    # Create a new Medication instance from the received data
    medication_instance = medication.Medication(medication_data)

    # Save the medication to the FHIR server
    medication_instance.create(smart.server)

    return jsonify({'message': 'Medication created successfully', 'medication_id': medication_instance.id})


@app.route('/medication/<medication_id>', methods=['GET'])
def get_medication(medication_id):
    # Retrieve a medication by ID
    medication_instance = medication.Medication.read(medication_id, smart.server)

    if medication_instance is None:
        return jsonify({'error': 'Medication not found'}), 404

    # Convert the medication to a JSON-serializable format
    medication_data = medication_instance.as_json()

    return jsonify(medication_data)


@app.route('/condition', methods=['POST'])
def create_condition():
    # Create a new condition
    condition_data = request.json

    # Create a new Condition instance from the received data
    condition_instance = condition.Condition(condition_data)

    # Save the condition to the FHIR server
    condition_instance.create(smart.server)

    return jsonify({'message': 'Condition created successfully', 'condition_id': condition_instance.id})


@app.route('/condition/<condition_id>', methods=['GET'])
def get_condition(condition_id):
    # Retrieve a condition by ID
    condition_instance = condition.Condition.read(condition_id, smart.server)

    if condition_instance is None:
        return jsonify({'error': 'Condition not found'}), 404

    # Convert the condition to a JSON-serializable format
    condition_data = condition_instance.as_json()

    return jsonify(condition_data)


if __name__ == '__main__':
    app.run()

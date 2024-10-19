# Cannabis Strain Recommendation Service

## Overview

The Cannabis Strain Recommendation Service is a web application that provides users with personalized cannabis strain recommendations based on their preferences. Utilizing machine learning techniques, this service leverages a dataset of cannabis strains to suggest the most suitable options for users based on their input.

## Features

- User-friendly interface to input preferences using sliders.
- Real-time recommendations of cannabis strains based on user input.
- Detailed strain information including name, type, description, and THC level.

## Tech Stack

- **Backend:** Flask
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas
- **Deployment:** Docker
- **Web Technologies:** HTML, CSS

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Docker (for containerization)

### Installation

1. Clone the repository:
git clone https://github.com/yourusername/strain-recom-service.git

2. Create and activate a virtual environment:
cd strain-recom-service
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install the required packages:
pip install -r requirements.txt

4. (Optional) Run tests to ensure everything is working correctly:
python -m unittest discover

### Running the Application

To run the Flask application:
python app.py
Visit http://127.0.0.1:5000 in your browser to access the application.

### Running with Docker

To build and run the application using Docker:

Build the Docker image:
docker build -t strain-recom-service .

Run the Docker container:
docker run -p 5000:5000 strain-recom-service

Visit http://127.0.0.1:5000 in your browser to access the application.

### Running with Docker Compose

Start the application using Docker Compose:
docker-compose up

Access the application at http://127.0.0.1:5000.
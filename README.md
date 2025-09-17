# WellnessTrack

WellnessTrack is a FastAPI-based application designed to provide wellness insights.

## Features

- **Lab Report Analysis**: Upload lab reports in PDF or image formats to extract health data using OCR and generate lifestyle-oriented wellness insights.
- **Meal Scanning**: Upload meal images to analyze nutritional content using AI models.
- **API Endpoints**:
  - `/lab_report_analysis`: Accepts lab report files and returns analyzed health data.
  - `/api/v1/analyze-food`: Accepts meal images and returns nutritional evaluation.

## Installation

1. Clone the repository:

   ```bash
   git clone your-repository-url
   cd WellnessTrack
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate      # On Unix or MacOS
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

Run the FastAPI application using Uvicorn:

```bash
python main.py
```

The API will be available at `http://127.0.0.1:8080`.

## API Documentation

FastAPI automatically generates interactive API docs:

- Swagger UI: `http://127.0.0.1:8080/docs`
- ReDoc: `http://127.0.0.1:8080/redoc`

### Endpoints

#### Lab Report Analysis

- **POST** `/lab_report_analysis`
- **Description**: Upload a lab report file (PDF or image) for analysis.
- **Request**: Multipart file upload.
- **Response**: JSON containing the file name and extracted report text with wellness insights.

#### Meal Scanning

- **POST** `/api/v1/analyze-food`
- **Description**: Upload a meal image for nutritional analysis.
- **Request**: Multipart file upload.
- **Response**: JSON containing nutritional information such as calories, protein, carbs, and fats.

## Project Structure

- `main.py`: Application entry point and route registration.
- `app/api/v1/endpoints/`: API route handlers for lab reports and meal scanning.
- `app/services/`: Business logic including OCR, graph processing, and meal analysis.
- `app/schemas/`: Pydantic models for request and response validation.
- `app/config.py`: Configuration and environment variable management.
- `app/utils/`: Utility functions such as file handling and logging.

## License

[Specify your license here]

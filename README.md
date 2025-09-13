# Medical Lab Report Analysis

A Python-based lab report analysis system that extracts, analyzes, and provides wellness insights from medical lab reports using OCR and LLMs.

## Features

- **OCR Integration**: Extracts text from lab report PDFs and images
- **Automated Analysis**: Processes lab values and identifies abnormal results
- **Wellness Insights**: Provides concise, actionable lifestyle recommendations
- **Structured Output**: Generates standardized JSON reports
- **Graph-based Processing**: Uses LangGraph for structured workflow management

## Project Structure

```
├── app/
│   ├── api/              # FastAPI endpoints
│   ├── config/          # Configuration settings
│   ├── model/           # Data models
│   ├── schemas/         # Pydantic schemas
│   ├── services/        # Business logic
│   │   ├── lab_report/  # Lab report processing
│   │   ├── graph/       # Graph processing
│   │   ├── llms/        # LLM integration
│   │   ├── nodes/       # Graph nodes
│   │   ├── ocr/         # OCR processing
│   │   └── state/       # State management
│   └── utils/           # Helper functions
├── config/              # Configuration files
├── logs/               # Application logs
├── notebook/           # Research notebooks
└── temp_data/         # Temporary data storage
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Roksana18cse04/WellnessTrack.git
cd WellnessTrack
```

2. Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix/MacOS:
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Environment Setup:
   Create a `.env` file in the root directory with:

```env
OPENAI_API_KEY=your_openai_api_key
```

## Running the Application

### 1. Process Lab Reports

```python
# Import required modules
from app.services.lab_report.ocr.ocr import OCR
from app.services.lab_report.llms.onenai_llm import OpenAILLM
from app.services.lab_report.graph.graph import LabReportGraph

# Initialize OCR
ocr = OCR()

# Process image/PDF
# For images:
text = ocr.process_image("temp_data/report_img.png")
# For PDFs:
# text = ocr.process_pdf("temp_data/cbc_report.pdf")

# Initialize LLM
llm_model = OpenAILLM()
llm = llm_model.get_llm_model()

# Setup and run graph
graph = LabReportGraph(model=llm)
graph_builder = graph.setup_graph()

# Process the extracted text
result = graph_builder.invoke({
    "report_text": text
})

# Get the analyzed report with insights
print(result["output"])
```

### API Endpoints

The system provides RESTful API endpoints for:

- Uploading lab reports
- Processing reports
- Retrieving analysis results

### Graph Processing

The system uses a graph-based workflow:

1. OCR Node: Extracts text from documents
2. Classification Node: Identifies report type and structure
3. Analysis Node: Processes lab values
4. Insight Node: Generates wellness recommendations

## Development

### Adding New Features

1. Create new nodes in `app/services/nodes/`
2. Update graph configuration in `app/services/graph/`
3. Add corresponding API endpoints in `app/api/`

### Testing

```bash
pytest tests/
```

## Logging

Logs are stored in the `logs` directory with daily rotation.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FastAPI for the web framework
- LangChain for LLM integration
- LangGraph for workflow management

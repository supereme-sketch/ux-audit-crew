# UX Audit Crew

An AI-powered UX audit system that analyzes Figma prototypes using a team of specialized agents.

## Features

- Comprehensive UX analysis using multiple specialized agents
- Detailed reports with severity levels and effort estimates
- ROI calculations and implementation roadmaps
- Web interface for easy access
- Configurable analysis parameters

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Figma access token (for private prototypes)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ux-audit-crew
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key
FIGMA_ACCESS_TOKEN=your_figma_access_token  # Optional, for private prototypes
```

## Usage

### Web Interface

1. Start the web server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:8080
```

3. Enter your Figma URL and click "Run Audit"

### Command Line

Run an audit directly from the command line:
```bash
python ux_audit_crew.py "https://www.figma.com/file/your-prototype-url"
```

## Deployment

### Deploying to Render.com (Free)

1. Create a Render account at https://render.com

2. Create a new Web Service:
   - Connect your GitHub repository
   - Select "Python" as the environment
   - The build command and start command will be automatically detected from `render.yaml`

3. Add your environment variables in Render's dashboard:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `FIGMA_ACCESS_TOKEN`: Your Figma access token (optional)

4. Deploy! Your app will be available at `https://your-app-name.onrender.com`

### Deploying to Other Platforms

The application can also be deployed to:
- Heroku
- Google Cloud Run
- AWS Elastic Beanstalk
- DigitalOcean App Platform

Contact the maintainers for specific deployment instructions for these platforms.

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `FIGMA_ACCESS_TOKEN`: Your Figma access token (optional)
- `PORT`: Web server port (default: 8080)
- `HOST`: Web server host (default: localhost)

### Customizing Agents

You can customize the agents by modifying the agent classes in `ux_audit_crew.py`:

- Adjust severity levels
- Modify effort estimates
- Add new evaluation criteria
- Customize report structure

## Report Structure

The audit report includes:

1. Executive Summary
2. Impact Analysis
3. Quick Wins Section
4. Detailed Findings
5. Implementation Roadmap
6. ROI Calculator
7. Before/After Recommendations
8. Follow-up Plan

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details

## Support

For support, please open an issue in the GitHub repository. 
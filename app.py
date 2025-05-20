from flask import Flask, render_template, request, jsonify
from ux_audit_crew import run_ux_audit
from config import settings, validate_settings
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        if not data or 'figmaUrl' not in data:
            return jsonify({'error': 'Figma URL is required'}), 400
        
        figma_url = data['figmaUrl']
        if not figma_url.startswith('https://www.figma.com/'):
            return jsonify({'error': 'Invalid Figma URL'}), 400
        
        # Run the audit and get individual reports
        result = run_ux_audit(figma_url)
        
        # Parse the result to extract individual reports
        try:
            # Try to parse as JSON first
            reports = json.loads(result)
        except json.JSONDecodeError:
            # If not JSON, create a basic structure
            reports = {
                'summary': result,
                'heuristic': 'Heuristic evaluation not available',
                'accessibility': 'Accessibility review not available',
                'responsive': 'Responsive design analysis not available',
                'copy': 'UX copy analysis not available',
                'visual': 'Visual hierarchy review not available',
                'interaction': 'Interaction pattern analysis not available'
            }
        
        return jsonify({'reports': reports})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    validate_settings()
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port) 
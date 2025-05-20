from flask import Flask, render_template, request, jsonify
from ux_audit_crew import run_ux_audit
from config import settings, validate_settings

app = Flask(__name__)

# Validate settings on startup
try:
    validate_settings()
except ValueError as e:
    print(f"Configuration Error: {e}")
    exit(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audit', methods=['POST'])
def audit():
    try:
        figma_url = request.json.get('figma_url')
        if not figma_url:
            return jsonify({'error': 'Figma URL is required'}), 400
        
        # Run the audit
        result = run_ux_audit(figma_url)
        return jsonify({'result': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=True
    ) 
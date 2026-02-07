#!/usr/bin/env python3
"""
Gemini Deep Research Engine - Backend Server
Handles API calls to bypass CORS restrictions
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Supported Gemini models
GEMINI_MODELS = [
    "gemini-1.5-flash-latest",
    "gemini-1.5-flash",
    "gemini-pro"
]

@app.route('/api/gemini', methods=['POST'])
def call_gemini():
    """
    Proxy endpoint for Gemini API calls
    """
    try:
        data = request.json
        prompt = data.get('prompt')
        api_key = data.get('api_key')
        
        if not prompt or not api_key:
            return jsonify({'error': 'Missing prompt or api_key'}), 400
        
        # Try each model until one works
        for model in GEMINI_MODELS:
            url = f"https://generativelanguage.googleapis.com/v1/models/{model}:generateContent?key={api_key}"
            
            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }],
                "generationConfig": {
                    "temperature": 0.7,
                    "topK": 40,
                    "topP": 0.95,
                    "maxOutputTokens": 8192
                },
                "safetySettings": [
                    {
                        "category": "HARM_CATEGORY_HARASSMENT",
                        "threshold": "BLOCK_NONE"
                    },
                    {
                        "category": "HARM_CATEGORY_HATE_SPEECH",
                        "threshold": "BLOCK_NONE"
                    }
                ]
            }
            
            response = requests.post(url, json=payload, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                
                # Extract text from response
                if (result.get('candidates') and 
                    len(result['candidates']) > 0 and
                    result['candidates'][0].get('content') and
                    result['candidates'][0]['content'].get('parts') and
                    len(result['candidates'][0]['content']['parts']) > 0):
                    
                    text = result['candidates'][0]['content']['parts'][0]['text']
                    return jsonify({
                        'success': True,
                        'text': text,
                        'model': model
                    })
            
            # Log error and try next model
            print(f"Model {model} failed: {response.status_code}")
            if response.status_code != 200:
                print(f"Error: {response.text}")
        
        return jsonify({'error': 'All models failed'}), 500
        
    except Exception as e:
        print(f"Server error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/wikipedia', methods=['GET'])
def fetch_wikipedia():
    """
    Fetch Wikipedia data
    """
    try:
        query = request.args.get('q')
        if not query:
            return jsonify({'error': 'Missing query parameter'}), 400
        
        url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json&origin=*&srlimit=5"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get('query') and data['query'].get('search'):
            snippets = [item['snippet'].replace('<span class="searchmatch">', '').replace('</span>', '') 
                       for item in data['query']['search']]
            return jsonify({
                'success': True,
                'data': ' | '.join(snippets)
            })
        
        return jsonify({'success': True, 'data': 'No Wikipedia data found.'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/duckduckgo', methods=['GET'])
def fetch_duckduckgo():
    """
    Fetch DuckDuckGo data
    """
    try:
        query = request.args.get('q')
        if not query:
            return jsonify({'error': 'Missing query parameter'}), 400
        
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        text = data.get('AbstractText') or data.get('Abstract') or 'No DuckDuckGo summary available.'
        
        return jsonify({
            'success': True,
            'data': text
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    """
    Health check endpoint
    """
    return jsonify({
        'status': 'online',
        'message': 'Gemini Research Backend Server',
        'endpoints': [
            '/api/gemini (POST)',
            '/api/wikipedia (GET)',
            '/api/duckduckgo (GET)'
        ]
    })

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 GEMINI RESEARCH BACKEND SERVER")
    print("=" * 60)
    print("Server starting on http://localhost:5000")
    print("\nAvailable endpoints:")
    print("  POST /api/gemini - Call Gemini API")
    print("  GET  /api/wikipedia?q=query - Fetch Wikipedia")
    print("  GET  /api/duckduckgo?q=query - Fetch DuckDuckGo")
    print("\nPress Ctrl+C to stop")
    print("=" * 60)
    
    app.run(debug=True, port=5000, host='0.0.0.0')

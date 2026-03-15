# Vercel API route for serverless Flask app
import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_app import app as flask_app

def handler(request, context):
    """Vercel Python handler"""
    return flask_app(request.environ, lambda status, headers: None)

def handler(request):
    \"\"\"Fallback Vercel handler - delegates to web_app.vercel_handler\"\"\"
    try:
        from web_app import vercel_handler
        return vercel_handler(request)
    except ImportError:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "text/plain"},
            "body": "Main app handler at web_app.py not ready."
        }
    except Exception as e:
        import traceback
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "text/plain"},
            "body": f"Fallback Error: {str(e)}\n\n{traceback.format_exc()}"
        }

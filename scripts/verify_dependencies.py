import sys

try:
    import fastapi
    import uvicorn
    import pydantic
    import httpx
    print('SUCCESS: All dependencies installed.')
    sys.exit(0)
except ImportError as e:
    print(f'FAILURE: Missing dependency - {e}')
    sys.exit(1)
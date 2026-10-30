import sys
import subprocess

def verify_environment():
    try:
        import fastapi
        import uvicorn
        import pydantic
        import httpx
        print('Environment OK: All dependencies found.')
        return True
    except ImportError as e:
        print(f'Environment Error: {e}')
        return False

if __name__ == '__main__':
    if not verify_environment():
        sys.exit(1)
    sys.exit(0)
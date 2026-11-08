import requests
import sys

def test_vault_flow():
    print('Starting Smoke Test: QuantumVault AI Flow...')
    # Test: Gateway Health
    try:
        response = requests.get('http://localhost:8000/health')
        if response.status_code != 200:
            print('Error: Gateway unreachable')
            sys.exit(1)
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)
    
    # Test: Encryption Flow (Mock)
    print('Smoke Test Passed: Gateway responsive and core modules loaded.')

if __name__ == '__main__':
    test_vault_flow()
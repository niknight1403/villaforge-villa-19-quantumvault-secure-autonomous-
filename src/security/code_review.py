import os
import subprocess

def run_code_review():
    # Run security-focused code review
    subprocess.run(['python', '-m', 'bandit', '-r', 'src/security'], check=True)

if __name__ == '__main__':
    run_code_review()
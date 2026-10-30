all:
	python3 scripts/pre_flight_guard.py

test:
	python3 scripts/pre_flight_guard.py

setup:
	pip install -r requirements.txt

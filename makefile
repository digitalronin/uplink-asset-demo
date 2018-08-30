# Install the Python SDK in a python virtual environment, so we can have
# multiple different versions, if necessary.
install-python-sdk:
	virtualenv ./venv
	./venv/bin/pip install git+https://github.com/adjoint-io/uplink-sdk-python

# Run this in a separate window (it generates a ton of log spam. Ignore it.
run-docker:
	docker run -it -p 8000:8000 -p 8545:8545 --name uplink --rm uplinkdlt/uplink:latest

# Start an uplink console on the docker container
console:
	docker exec -it uplink /usr/bin/uplink console

# Start a bash shell on the docker container
shell:
	docker exec -it uplink bash

run-test-script:
	./venv/bin/python test.py  # localhost:8545 is hard-coded

create-accounts:
	./venv/bin/python create_accounts.py | tee accounts.txt


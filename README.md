# Asset demo using Adjoint Uplink

Enable creating and trading shares in a new asset using [Uplink](https://www.adjoint.io/technology/resources) as the
underlying blockchain database and smart contract (workflow) execution
platform.

# Getting started

* Install the python SDK

`make install-python-sdk`

* Start an Uplink node in a separate terminal window

`make run-docker`

## Create an account

`./venv/bin/python create_account.py`

Use the output of this command to configure the private key ('skey') and origin/issuer ('address') in `create_asset.py`

## Create an asset

`./venv/bin/python create_asset.py`


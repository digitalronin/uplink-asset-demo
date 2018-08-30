from uplink import *
from pprint import pprint

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

accounts = rpc.uplink_accounts()

def is_validator(account):
    if 'validator' in account.metadata:
        return account.metadata['validator'] == 'true'

for acct in accounts:
    if not is_validator(acct):
        print(acct.address)
        pprint(acct.metadata)

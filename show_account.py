from uplink import *
from pprint import pprint

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

address = "D6txCVjzYiD4bZ6RoibWSAco1oaqrWh5Zny5UiXYyd9L"

account = rpc.uplink_get_account(address)

pprint(account.metadata)
print("Address: " + account.address)

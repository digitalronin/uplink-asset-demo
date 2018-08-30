from uplink import *

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

print rpc.uplink_blocks()
print rpc.uplink_peers()
print rpc.uplink_accounts()
print rpc.uplink_assets()

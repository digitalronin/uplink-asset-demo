from uplink import *
import binascii

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

pubkey, skey = ecdsa_new()

print("Public key: \n" + binascii.hexlify(pubkey.to_string()))
print("Private key: \n" + binascii.hexlify(skey.to_string()))

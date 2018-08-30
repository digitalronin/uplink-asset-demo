from uplink import *
import binascii

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

def create_account(rpc, name):
    pubkey, skey = ecdsa_new()

    metadata = dict(Name = name)

    txhash, address = rpc.uplink_create_account(
            private_key=skey,
            public_key=pubkey,
            from_address=None,
            metadata=metadata,
            timezone="CET"
            )

    print("Name: " + name)
    print("Account address: " + address)
    print("Public key:")
    print(binascii.b2a_hex(pubkey.to_string()))
    print("Private key:")
    print(binascii.b2a_hex(skey.to_string()))
    print("-------------------\n")

################################

names = ["Alice", "Bob", "Charlie", "David"]

print()
for name in names:
    create_account(rpc, name)

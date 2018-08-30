from uplink import *
import binascii

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

pubkey, skey = ecdsa_new()


metadata = dict(stuff="key", foo="bar", full_name="Some Guy")

new_acct = rpc.uplink_create_account(
        private_key=skey,
        public_key=pubkey,
        from_address=None,
        metadata=metadata,
        timezone="GMT"
        )

print("Public key: \n" + binascii.b2a_hex(pubkey.to_string()))

print("Private key: \n" + binascii.b2a_hex(skey.to_string()))

print("Account")
print(new_acct)

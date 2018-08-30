import binascii
from uplink import *

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

# Get these by running create_account.py and saving its output
skey = binascii.a2b_hex("acdcd6250c82ebe312115192f3881366f98135d0232b3f60dcd64b426fe15dad")
address = "Ajz7ZN1XZVtJ9CqpbqgXWf3Jwa63ULH7JrMRnFXWmWDa"

# TODO: this isn't working
tx_hash, asset_address = rpc.uplink_create_asset(
        private_key=skey,
        origin=address,
        name="My New Asset",
        supply=1000,
        asset_type_nm="Discrete",
        reference="Token",
        issuer=address
)

print(asset_address)

import binascii
from ecdsa import SigningKey, SECP256k1
from uplink import *
from pprint import pprint

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

# Get the values here by running create_accounts.py and saving its output

skey = binascii.a2b_hex("e2414ebf30291242a2709e7dfbb96319e0d0a960bbd0cc8c8e581d6c1b801063")
address = "7259nRaz42NbZSC4o33NimPMedwPsERuzQvJe72ZthK"

privkey = SigningKey.from_string(skey, curve = SECP256k1)

tx_hash, asset_address = rpc.uplink_create_asset(
        private_key=privkey,
        origin=address,
        name="Toyota Prius XV189CF",
        supply=1000,
        asset_type_nm="Discrete",
        reference="Token",
        issuer=address
)

print(asset_address)

# Circulate the asset to the issuer, so that it can be transferred
result = rpc.uplink_circulate_asset(
        private_key=privkey,
        from_address = address,
        amount = 1000,
        asset_address = asset_address
        )

pprint(result)

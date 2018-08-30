import binascii
from ecdsa import SigningKey, SECP256k1
from uplink import *
from pprint import pprint

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

# Get the values here by running create_accounts.py and saving its output

skey = binascii.a2b_hex("e2414ebf30291242a2709e7dfbb96319e0d0a960bbd0cc8c8e581d6c1b801063")
from_address = "7259nRaz42NbZSC4o33NimPMedwPsERuzQvJe72ZthK"

to_address = "AUGirRQFDq7QP6NSqbF2DENqE8Dng31WykcdBj46prw8"

# Get the asset_address from the output of create_asset.py
asset_address = "A3mW3dtstXRiYbiqViTGS2LhCRL6sHxZR7ZkJ6NzE3Ro"

privkey = SigningKey.from_string(skey, curve = SECP256k1)

results = rpc.uplink_transfer_asset(
        private_key   = privkey,
        from_address  = from_address,
        to_address    = to_address,
        balance       = 23,
        asset_address = asset_address
        )

pprint(results)

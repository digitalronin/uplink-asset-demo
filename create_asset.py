import binascii
from ecdsa import SigningKey, SECP256k1
from uplink import *

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

# Get the values here by running create_account.py and saving its output

# public key: "097b8cae449f294ee09497ae2c450414764b95a208f2e7f9f686bcec133fea4e2308a11204cf1090de07175721bc5dce60710ec1b8604ca7bda2a077cbd7b9bd"
skey = binascii.a2b_hex("a1c716d45d3be0364cb169a19b8c5868adc28f3a76fe9254c43af4c00ada7d7a")
address = "4nbxG5q4JX48PEce3k3sXdWyaMqcUP8CjkzspXVHoWKH"

privkey = SigningKey.from_string(skey, curve = SECP256k1)

tx_hash, asset_address = rpc.uplink_create_asset(
        private_key=privkey,
        origin=address,
        name="My New Asset",
        supply=1000,
        asset_type_nm="Discrete",
        reference="Token",
        issuer=address
)

print(asset_address)

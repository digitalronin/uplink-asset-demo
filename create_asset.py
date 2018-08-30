import binascii
from ecdsa import SigningKey, SECP256k1
from uplink import *

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

# Get the values here by running create_accounts.py and saving its output

skey = binascii.a2b_hex("ce7ec550305420d97ddf3b99a7db4e0d42a5b02758dfc16c4f7b26c73d2e03a8")
address = "BGcURyq8kkRAZp8SRwY9ia6Z3Sz1Hn3feYAL3QbBvhjE"

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

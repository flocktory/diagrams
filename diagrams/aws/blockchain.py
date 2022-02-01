# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _AWS


class _Blockchain(_AWS):
    _type = "blockchain"
    _icon_dir = "resources/aws/blockchain"


class BlockchainResource(_Blockchain):
    _icon = "blockchain-resource.png"


class Blockchain(_Blockchain):
    _icon = "blockchain.png"


class ManagedBlockchain(_Blockchain):
    _icon = "managed-blockchain.png"


class QuantumLedgerDatabaseQldb(_Blockchain):
    _icon = "quantum-ledger-database-qldb.png"


# Aliases

QLDB = QuantumLedgerDatabaseQldb

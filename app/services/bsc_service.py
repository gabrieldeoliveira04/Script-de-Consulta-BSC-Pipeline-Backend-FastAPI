from web3 import Web3
from utils.token_abi import TOKEN_ABI


class BSCService:

    def __init__(self, rpc_url: str):
        """
        Inicializa conexão com nó RPC BSC
        """

        self.web3 = Web3(
            Web3.HTTPProvider(rpc_url)
        )

    def is_connected(self):
        """
        Verifica conexão
        """

        return self.web3.is_connected()

    def get_current_block(self):
        """
        Retorna bloco atual
        """

        return self.web3.eth.block_number

    def get_bnb_balance(self, wallet_address: str):
        """
        Consulta saldo BNB nativo
        """

        wallet = Web3.to_checksum_address(
            wallet_address
        )

        balance_wei = (
            self.web3.eth.get_balance(wallet)
        )

        balance_bnb = (
            self.web3.from_wei(
                balance_wei,
                "ether"
            )
        )

        return balance_bnb

    def get_token_balance(
        self,
        wallet_address: str,
        token_address: str
    ):
        """
        Consulta saldo BEP20
        """

        wallet = Web3.to_checksum_address(
            wallet_address
        )

        token = Web3.to_checksum_address(
            token_address
        )

        contract = self.web3.eth.contract(
            address=token,
            abi=TOKEN_ABI
        )

        raw_balance = (
            contract.functions
            .balanceOf(wallet)
            .call()
        )

        decimals = (
            contract.functions
            .decimals()
            .call()
        )

        readable_balance = (
            raw_balance / (10 ** decimals)
        )

        return readable_balance
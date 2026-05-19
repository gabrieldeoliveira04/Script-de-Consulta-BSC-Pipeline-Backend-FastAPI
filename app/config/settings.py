from dotenv import load_dotenv
#importa função que lê .env
import os
#Permite acessar variáveis do ambiente

load_dotenv()
#carrega o arquivo .env para a memória

class Settings:

    RPC_URL = os.getenv(
        "RPC_URL"
    )

    TOKEN_ADDRESS = os.getenv(
        "TOKEN_ADDRESS"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL"
    )

    WALLETS = [

        os.getenv("WALLET_1"),

        os.getenv("WALLET_2"),

        os.getenv("WALLET_3")

    ]


settings = Settings()

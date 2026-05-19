from dotenv import load_dotenv
#importa função que lê .env
import os
#Permite acessar variáveis do ambiente

load_dotenv()
#carrega o arquivo .env para a memória

RPC_URL = os.getenv("RPC_URL")
#Busca variável da url da requisição por nome

WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

TOKEN_ADDRESS = os.getenv("TOKEN_ADDRESS")

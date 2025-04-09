import os
from dotenv import load_dotenv
from huggingface_hub import HfApi, InferenceApi

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializa o cliente Hugging Face
hf_token = os.getenv('HUGGINGFACE_TOKEN')
hf_api = HfApi(token=hf_token)

def get_huggingface_client():
    return hf_api

def get_inference_api(model_id):
    return InferenceApi(repo_id=model_id, token=hf_token) 
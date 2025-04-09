import os
from dotenv import load_dotenv
from supabase import create_client

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializa o cliente Supabase
supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

def get_supabase_client():
    return supabase 
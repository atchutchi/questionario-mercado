from huggingface import get_inference_api

def translate_text(text, from_lang="pt", to_lang="en"):
    """
    Traduz texto usando o modelo Helsinki-NLP/opus-mt
    Args:
        text (str): Texto para traduzir
        from_lang (str): Idioma de origem (padrão: português)
        to_lang (str): Idioma de destino (padrão: inglês)
    Returns:
        str: Texto traduzido
    """
    model_name = f"Helsinki-NLP/opus-mt-{from_lang}-{to_lang}"
    translator = get_inference_api(model_name)
    
    try:
        result = translator(text)
        return result[0]['translation_text']
    except Exception as e:
        print(f"Erro na tradução: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    texto = "Olá, como você está?"
    traducao = translate_text(texto)
    print(f"Texto original: {texto}")
    print(f"Tradução: {traducao}") 
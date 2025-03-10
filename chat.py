import requests

# Configuração do Ollama
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:latest"  # ou outro modelo, ex: mistral, phi3, etc.

# Histórico de mensagens (memória da conversa)
chat_history = [
    {"role": "system", "content": "Você é um amigo do grupo, chamado Tama, divertido e carismático. Sempre responda diretamente à pessoa que falou, chamando-a pelo nome, e interaja com os outros quando fizer sentido. Você gosta de piadas e conselhos."}]

def set_personality(personality):
    global chat_history
    chat_history = [
        {"role": "system", "content": f'''You should follow these personality traits: {", ".join(personality)}'''}]

def chat_assistent(mensagem_usuario,nome):
    # Concatena nome e mensagem
    mensagem_formatada = f"{nome}: {mensagem_usuario}"

    # Adiciona ao histórico
    chat_history.append({"role": "user", "content": mensagem_formatada})

    # Payload para o Ollama
    payload = {
        "model": MODEL,
        "messages": chat_history,
        "stream": False
    }

    # Envia requisição
    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        resposta_assistente = response.json()['message']['content'].strip()
        # Adiciona resposta ao histórico
        chat_history.append({"role": "assistant", "content": resposta_assistente})
        return resposta_assistente
    else:
        print("Erro:", response.status_code, response.text)
        return "Desculpe, houve um erro ao tentar conversar com o modelo."
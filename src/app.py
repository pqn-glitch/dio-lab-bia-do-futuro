import json
import pandas as pd
import requests
import streamlit as st

# CONFIG OLLAMA
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2"  # ou mistral, phi3, etc

# CARREGAR DADOS

perfil = json.load(open('./data/perfil_usuario.json', encoding='utf-8'))
registro = pd.read_csv('./data/registro_alimentar.csv', encoding='utf-8')
planos = json.load(open('./data/planos_treino.json', encoding='utf-8'))
base = json.load(open('./data/base_nutricional.json', encoding='utf-8'))
historico = pd.read_csv('./data/historico_atendimento.csv', encoding='utf-8')

# CRIAR CONTEXTO DO CLIENTE

usuario = perfil[0]

contexto_cliente = {

    "nome": usuario["nome"],
    "idade": usuario["idade"],
    "sexo": usuario["sexo"],

    "altura_cm": usuario["altura_cm"],
    "peso_kg": usuario["peso_kg"],

    "objetivo": usuario["objetivo"],
    "nivel_atividade": usuario["nivel_atividade"],
    "frequencia_treino": usuario["frequencia_treino_atual"],
    "tempo_treino_min": usuario["tempo_disponivel_treino_min"],

    "rotina_trabalho": usuario["rotina_trabalho"],

    "sono_horas": usuario["horas_sono_media"],
    "agua_litros_dia": usuario["consumo_agua_litros_dia"],

    "preferencias": usuario["preferencias_alimentares"],
    "restricoes": usuario["restricoes_alimentares"],

    "historico_saude": usuario["historico_saude"],
    "observacoes": usuario["observacoes"]
}

# FUNÇÃO PARA GERAR CONTEXTO

def criar_contexto_texto(contexto):

    texto = f"""
Cliente: {contexto['nome']}
Idade: {contexto['idade']} anos
Sexo: {contexto['sexo']}

Altura: {contexto['altura_cm']} cm
Peso: {contexto['peso_kg']} kg

Objetivo: {contexto['objetivo']}
Nível de atividade: {contexto['nivel_atividade']}
Frequência de treino: {contexto['frequencia_treino']}
Tempo disponível por treino: {contexto['tempo_treino_min']} minutos

Rotina de trabalho: {contexto['rotina_trabalho']}

Sono médio: {contexto['sono_horas']} horas
Consumo de água: {contexto['agua_litros_dia']} litros/dia

Preferências alimentares: {', '.join(contexto['preferencias'])}

Restrições alimentares: {', '.join(contexto['restricoes']) if contexto['restricoes'] else 'Nenhuma'}

Histórico de saúde: {', '.join(contexto['historico_saude'])}

Observações: {contexto['observacoes']}
"""

    return texto

contexto_texto = criar_contexto_texto(contexto_cliente)

print("\n==============================")
print("CONTEXTO EM TEXTO")
print("==============================")
print(contexto_texto)

# PROMPTS DO AGENTE

SYSTEM_PROMPT = """
Você é o Corpo&Mente, um agente inteligente especializado em saúde, alimentação e treino físico.

Seu objetivo é ajudar o usuário a evoluir de forma sustentável, utilizando exclusivamente os dados disponíveis na base interna do sistema.

Você tem acesso aos seguintes arquivos:
- perfil_usuario.json
- registro_alimentar.csv
- historico_atendimento.csv
- planos_treino.json
- base_nutricional.json

Seu papel é:
- Analisar dados do usuário
- Identificar padrões e inconsistências
- Sugerir ajustes personalizados
- Manter consistência com o objetivo registrado no perfil
- Justificar recomendações com base nos dados

REGRAS OBRIGATÓRIAS:

1. Sempre baseie suas respostas apenas nos dados disponíveis.
2. Nunca invente informações que não estejam na base.
3. Não forneça diagnósticos médicos.
4. Não prescreva medicamentos.
5. Não substitua acompanhamento profissional.
6. Quando não houver dados suficientes, peça mais informações.
7. Sempre explique o motivo da recomendação.
8. Priorize o objetivo registrado no perfil do usuário.
9. Em caso de inconsistência entre dados antigos e recentes, priorize o dado mais recente.
10. Se a solicitação estiver fora do escopo (ex: previsão do tempo), informe educadamente sua limitação.
11. Responda de forma mais sucinta, com no máximo 4 parágrafos.
"""

# INTERAÇÃO OLLAMA

def perguntar(pergunta_usuario):

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto_texto}

PERGUNTA DO USUÁRIO:
{pergunta_usuario}

RESPOSTA:
"""
    
    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return resposta.json()["response"]

# MODO TERMINAL

def rodar_terminal():

    print("Corpo&Mente iniciado (modo terminal)")

    while True:

        pergunta = input("\nDigite sua pergunta (ou 'sair'): ")

        if pergunta.lower() == "sair":
            break

        resposta = perguntar(pergunta)

        print("\nResposta do agente:\n")
        print(resposta)

# MODO STREAMLIT

def rodar_streamlit():

    st.set_page_config(
        page_title="Corpo&Mente AI",
        page_icon="💪",
        layout="centered"
    )

    st.title("💪 Corpo&Mente AI")

    st.write("Assistente inteligente de saúde")

    pergunta = st.text_input("Digite sua pergunta:")

    if st.button("Perguntar"):

        if pergunta:

            with st.spinner("Analisando seus dados..."):
                resposta = perguntar(pergunta)

            st.success("Resposta gerada com sucesso!")

            st.write(resposta)


# EXECUÇÃO

rodar_streamlit()
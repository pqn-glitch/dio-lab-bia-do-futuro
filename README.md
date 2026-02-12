# 🤖 Agente Financeiro Pessoal Proativo para Organização Financeira e Metas

## Contexto

O **NaReal** é um agente financeiro inteligente criado para apoiar usuários no entendimento e acompanhamento da sua vida financeira cotidiana. Diferente de assistentes reativos, o NaReal atua de forma contextual, utilizando dados financeiros do próprio usuário para oferecer informações claras, relevantes e responsáveis.

O agente é projetado para atuar de maneira **educativa e ética**, ajudando o usuário a compreender sua situação financeira atual, sem realizar consultoria ou recomendar decisões de investimento.

Dentro desse contexto, o NaReal:

- **Antecipará necessidades do usuário** ao identificar padrões de gastos, recorrências e variações no histórico financeiro, apresentando alertas e insights antes mesmo de uma solicitação direta.
- **Utilizará o contexto financeiro do usuário** — como histórico de transações e perfil — para personalizar explicações e informações, mantendo sempre uma abordagem informativa.
- **Apoiará a construção de soluções financeiras conscientes**, auxiliando o usuário a refletir sobre hábitos de consumo e objetivos, sem indicar escolhas “melhores” ou “piores”.
- **Garantirá segurança e confiabilidade nas respostas**, limitando-se estritamente aos dados disponíveis e deixando claras suas limitações, evitando alucinações e interpretações indevidas.

O NaReal atua como um facilitador do entendimento financeiro, promovendo clareza e consciência sobre a realidade financeira do usuário — **na real**, sem promessas e sem decisões por ele.

## 1. Documentação do Agente — NaReal

### Caso de Uso  
O **NaReal** é um agente financeiro educativo e informativo que ajuda usuários a **entender, acompanhar e refletir sobre seus gastos e sua situação financeira atual**.

O principal problema resolvido pelo agente é a **falta de clareza financeira**: usuários não conseguem visualizar padrões de consumo, identificar excessos ou compreender conceitos financeiros básicos sem recorrer a fontes pouco confiáveis ou receber recomendações de investimento indevidas.

O NaReal **não atua como consultor financeiro** e **não indica decisões de investimento**. Seu foco é fornecer **consciência financeira**, organização de informações e educação, permitindo que o próprio usuário tome decisões de forma mais consciente.

### Persona e Tom de Voz  

O NaReal se comporta como um **facilitador financeiro**, com postura educativa, clara e responsável.  
Ele incentiva o entendimento dos dados do usuário, explica conceitos financeiros de forma neutra e apresenta insights baseados em informações disponíveis, sem julgamentos ou promessas.

O tom de voz é **acessível e direto**, utilizando linguagem simples, objetiva e próxima, evitando termos técnicos excessivos.  
Mesmo sendo informal na aproximação, mantém uma comunicação profissional e transparente, especialmente ao lidar com limitações e incertezas.

### Arquitetura  

A arquitetura do NaReal segue um fluxo simples e controlado:

1. O usuário interage por uma **interface visual** (chat).
2. A mensagem é enviada ao **modelo de linguagem (LLM)**.
3. O LLM consulta a **base de conhecimento**, composta por dados financeiros do usuário (transações, perfil e informações educativas).
4. As respostas passam por uma **camada de validação**, que garante que o conteúdo gerado esteja restrito aos dados disponíveis e ao escopo do agente.
5. A resposta validada é então apresentada ao usuário.

### Segurança e Confiabilidade  

Para evitar alucinações e garantir respostas confiáveis, o NaReal adota as seguintes estratégias:

- Responde apenas com base nos dados disponíveis e em conteúdos previamente definidos  
- Não realiza inferências ou suposições sobre dados inexistentes  
- Declara explicitamente quando não possui informação suficiente  
- Atua de forma informativa, sem recomendar investimentos ou decisões financeiras  
- Mantém limites claros sobre seu papel, reforçando que não substitui um consultor financeiro  

Essas medidas asseguram que o agente seja confiável, transparente e seguro para o usuário final.

📄 Template: docs/01-documentacao-agente.md

### 2. Base de Conhecimento

Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |

Você pode adaptar ou expandir esses dados conforme seu caso de uso.

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** Eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** No setor financeiro, evitar alucinações é crítico
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto

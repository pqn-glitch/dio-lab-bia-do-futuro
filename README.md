# 🤖 Assistente Pessoal Proativo para Saúde, Alimentação e Treino

## Contexto

Os assistentes virtuais na área de saúde e bem-estar estão evoluindo de simples geradores de dicas genéricas para agentes inteligentes e proativos, capazes de organizar rotinas, estruturar planos e promover constância de forma personalizada.

Neste desafio, o **Corpo&Mente** é idealizado como um assistente de lifestyle que utiliza IA Generativa para:

- Antecipar necessidades relacionadas à alimentação e treino, ao invés de apenas responder perguntas pontuais  
- Personalizar orientações com base na rotina, objetivos e nível do usuário  
- Cocriar projetos pessoais de evolução física e saúde de forma estruturada e sustentável  
- Promover equilíbrio entre estética e saúde, evitando extremismos  
- Garantir segurança e responsabilidade nas orientações, respeitando limites e não substituindo profissionais da saúde  

O foco do Corpo&Mente não é prescrever dietas rígidas ou treinos extremos, mas sim ajudar o usuário a construir hábitos consistentes, inteligentes e alinhados com sua realidade.

## 1. Documentação do Agente

### Caso de Uso
O **Corpo&Mente** é um assistente de saúde integral que ajuda usuários a organizar alimentação diária e treinos físicos de forma estruturada e sustentável.

Ele resolve o problema da desorganização, excesso de informações contraditórias e falta de constância na rotina de saúde.  
O agente auxilia na criação de projetos pessoais de evolução física, promovendo equilíbrio entre saúde e estética sem extremismos.


### Persona e Tom de Voz
O Corpo&Mente se comporta como um guia estratégico e equilibrado, com postura educativa e responsável.

Seu tom é acessível, direto e motivador na medida certa.  
Evita promessas irreais e mantém foco em progresso consistente e sustentável.


### Arquitetura
O fluxo de funcionamento do agente ocorre da seguinte forma:

1. O usuário informa objetivo, rotina e nível atual.
2. A interface envia essas informações ao modelo de linguagem (LLM).
3. O LLM consulta a base de conhecimento contendo dados do usuário e diretrizes gerais de saúde.
4. Uma camada de validação verifica se a resposta está dentro do escopo permitido.
5. A orientação estruturada é enviada ao usuário.

Essa arquitetura garante organização, personalização e controle do escopo das respostas.

### Segurança
Para evitar alucinações e garantir confiabilidade:

- O agente responde apenas com base nas informações fornecidas pelo usuário.
- Não realiza diagnósticos médicos ou prescrições clínicas.
- Declara limitações quando não possui dados suficientes.
- Mantém o escopo restrito a organização alimentar, estrutura de treino e hábitos saudáveis.
- Reforça que não substitui profissionais da saúde.

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md).


### 2. Base de Conhecimento

O agente Corpo&Mente utiliza dados mockados armazenados na pasta data/ para personalizar recomendações de treino, alimentação e hábitos saudáveis.

Os dados são estruturados para permitir acompanhamento evolutivo, personalização de planos e respostas contextualizadas.

Arquivos Utilizados
| Arquivo                   | Formato | Descrição                                             |
| ------------------------- | ------- | ----------------------------------------------------- |
| registro_alimentar.csv    | CSV     | Histórico de refeições e consumo diário do usuário    |
| historico_atendimento.csv | CSV     | Registro de interações anteriores com o agente        |
| perfil_usuario.json       | JSON    | Dados físicos, objetivos e preferências do usuário    |
| planos_treino.json        | JSON    | Estrutura de treinos disponíveis e variações          |
| base_nutricional.json     | JSON    | Base simplificada de alimentos e valores nutricionais |

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md).

### 3. Prompts do Agente

Os prompts definem o comportamento, as regras e os limites de atuação do Corpo&Mente.  
Eles garantem consistência, segurança e alinhamento com o objetivo do usuário.

---

### System Prompt

O System Prompt estabelece:

- O papel do agente como assistente especializado em saúde, alimentação e treino.
- A obrigação de utilizar apenas os dados disponíveis na base interna.
- A proibição de inventar informações ou extrapolar o escopo.
- A restrição de não realizar diagnósticos médicos ou prescrever medicamentos.
- A exigência de justificar recomendações com base no histórico do usuário.

Também define o tom de comunicação:

- Motivador e equilibrado.
- Claro e didático.
- Profissional e acessível.
- Focado em progresso sustentável.

Essa estrutura reduz alucinações e aumenta previsibilidade nas respostas.

---

### Exemplos de Interação

A documentação inclui cenários simulados com:

- Contexto do usuário.
- Pergunta realizada.
- Resposta ideal esperada do agente.

Os exemplos seguem a técnica de *Few-Shot Prompting*, orientando o modelo a:

- Manter padrão de resposta estruturado.
- Justificar recomendações com base em dados.
- Recusar solicitações fora do escopo.
- Solicitar informações adicionais quando necessário.

Isso melhora a robustez e a coerência das interações.

---

### Tratamento de Edge Cases

O agente possui diretrizes claras para situações limite:

- Perguntas fora do escopo são redirecionadas educadamente.
- Solicitações de informações sensíveis são recusadas.
- Pedidos médicos ou clínicos são bloqueados.
- Recomendações sem contexto exigem coleta adicional de dados.

Esse tratamento garante:

- Segurança do usuário.
- Proteção de dados.
- Conformidade ética.
- Controle rigoroso do escopo de atuação.

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)
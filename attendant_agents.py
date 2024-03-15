from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

"""
Criando Guia Rápido para Agentes:
- Pense como um chefe. Trabalhe retroativamente a partir do objetivo e pense em qual funcionário
  você precisa contratar para realizar o trabalho.
- Defina o Capitão da equipe que orientará os outros agentes em direção ao objetivo.
- Defina quais especialistas o capitão precisa se comunicar e delegar tarefas.
  Construa uma estrutura hierárquica descendente da equipe.

Objetivo:
- Criar um itinerário de viagem de 7 dias com planos detalhados por dia,
  incluindo orçamento, sugestões de embalagem e dicas de segurança.

Capitão/Gerente/Chefe:
- ex: Especialista em Viagens

Funcionários/Especialistas a contratar:
- ex: Especialista em Seleção de Cidades
- ex: Guia Turístico Local

Notas:
- Os agentes devem ser orientados por resultados e ter um objetivo claro em mente
  A função é o título do trabalho.
- Os objetivos devem ser acionáveis.
- A história pregressa deve ser o currículo.
"""

class AttendantAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def customer_service_on_whatsApp(self):
        return Agent(
            role="Atendente de Clientes no WhatsApp",
            backstory=dedent("""
                Profissional com experiência em atendimento ao cliente, especialmente em ambientes virtuais como o WhatsApp.
                Habilidade em comunicação eficaz e resolução de problemas para garantir a satisfação do cliente.
                Conhecimento das políticas da empresa e dos produtos/serviços oferecidos para fornecer informações precisas.
            """),
            goal=dedent("""
                Fornecer suporte e assistência aos clientes via WhatsApp, garantindo uma experiência positiva e satisfatória.
                Responder rapidamente às consultas dos clientes, resolver problemas. Manter registros precisos das interações com os clientes e colaborar com a equipe para melhorar continuamente o serviço.
            """),
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT35,
            memory=True,
        )
    
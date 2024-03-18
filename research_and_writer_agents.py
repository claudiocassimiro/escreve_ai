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

class ResearchAndWriterAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    
    def research(self):
        return Agent(
            role='Senior Research Analyst',
            goal='Uncover cutting-edge developments in AI and data science',
            backstory="""You work at a leading tech think tank.
            Your expertise lies in identifying emerging trends.
            You have a knack for dissecting complex data and presenting actionable insights.""",
            verbose=True,
            allow_delegation=False,
            llm=self.OpenAIGPT35,
        )
    
    def writer(self):
        return Agent(
            role='Tech Content Strategist',
            goal='Craft compelling content on tech advancements',
            backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
            You transform complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=True,
            lm=self.OpenAIGPT35,
        )
    
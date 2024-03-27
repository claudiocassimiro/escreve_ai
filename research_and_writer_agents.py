from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai_tools import (
    SerperDevTool,
)

search_tool = SerperDevTool()

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
            role='Analista de Pesquisa Sênior',
            goal='Utilizar expertise avançada em pesquisa e análise para fornecer insights de alta qualidade e soluções eficazes, atendendo às necessidades dos clientes e contribuindo para o crescimento e sucesso da empresa.',
            backstory="""Você trabalha em um think tank líder em tecnologia.
            Sua experiência reside na identificação de tendências emergentes.
            Você tem talento para dissecar dados complexos e apresentar insights acionáveis.""",
            verbose=True,
            tools=[search_tool],
            allow_delegation=False,
            llm=self.OpenAIGPT35,
        )
    
    def writer(self):
        return Agent(
            role='Especialista em Criação de Conteúdo',
            goal='Gerar conteúdo altamente cativante e estratégico para as redes sociais, visando aumentar o engajamento, promover a marca e impulsionar o crescimento do público-alvo da empresa/cliente.',
            backstory="""Você é um renomado estrategista de conteúdo, conhecido por seus artigos perspicazes e envolventes.
            Você transforma conceitos complexos em narrativas convincentes.""",
            verbose=True,
            tools=[search_tool],
            allow_delegation=True,
            lm=self.OpenAIGPT35,
        )
    
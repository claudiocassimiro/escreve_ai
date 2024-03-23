from crewai import Task
from textwrap import dedent

"""
Guia Rápido para Criação de Tarefas:
- Comece com o fim em mente. Identifique o resultado específico que suas tarefas visam alcançar.
- Divida o resultado em tarefas acionáveis, atribuindo cada tarefa ao agente apropriado.
- Certifique-se de que as tarefas sejam descritivas, fornecendo instruções claras e entregáveis esperados.

Objetivo:
- Desenvolver um itinerário detalhado, incluindo seleção de cidades, atrações e conselhos práticos de viagem.

Principais Etapas para Criação de Tarefas:
1 - Identificar o Resultado Desejado: Defina como o sucesso se parece para o seu projeto.
  - Um itinerário de viagem detalhado de 7 dias.

2 - Decomposição de Tarefas: Divida o objetivo em tarefas menores e gerenciáveis que os agentes podem executar.
  - Planejamento do Itinerário: Desenvolver um plano detalhado para cada dia da viagem.
  - Seleção de Cidades: Analisar e escolher as melhores cidades para visitar.
  - Guia Turístico Local: Encontrar um especialista local para fornecer insights e recomendações.

3- Atribuir Tarefas aos Agentes: Relacione tarefas aos agentes com base em seus papéis e expertise.

4 - Modelo de Descrição de Tarefa:
  - Use este modelo como guia para definir cada tarefa em sua aplicação CrewAI.
  - Este modelo ajuda a garantir que cada tarefa seja claramente definida, acionável e alinhada com os objetivos específicos do seu projeto.

Modelo:
    def [nome_tarefa](self, agente, [parâmetros]):
        return Tarefa(descrição=dedent(f'''
        Tarefa: [Forneça um nome ou resumo conciso da tarefa.]
        Descrição: [Descrição detalhada do que se espera que o agente faça, incluindo etapas acionáveis e resultados esperados. Isso deve ser claro e direto, delineando as ações específicas necessárias para concluir a tarefa.]

        **Parâmetros**:
        - [Parâmetro 1]: [Descrição]
        - [Parâmetro 2]: [Descrição]
        ... [Adicione mais parâmetros conforme necessário.]

        **Observação**: [Seção opcional para incentivos ou estímulo para um trabalho de alta qualidade. Isso pode incluir dicas, contexto adicional ou motivações para incentivar os agentes a entregar seu melhor trabalho.]

        '''), agente=agente)
"""

class ResearchAndWriterTasks:
    def __init__(self, user_writing_format, theme_to_search):
        self.user_writing_format = user_writing_format
        self.theme_to_search = theme_to_search

    def __tip_section(self):
        return "Lembre-se de fazer o seu MELHOR TRABALHO e você vai ganhar uma comissão de US$ 10.000."

    def research_theme(self, agent):
        return Task(description=dedent(f'''
                **Tarefa**: Faça uma análise abrangente de {self.theme_to_search}.
                **Descrição**: Identifique as principais tendências, tecnologias inovadoras e possíveis impactos no setor.

                **Nota**: {self.__tip_section}
            '''),
            agent=agent,
            expected_output="Relatório de análise completo em bullet points",
      )
    
    def write_post(self, agent):
        return Task(description=dedent(f'''
                **Tarefa**: Usando os insights fornecidos e as seguintes amostras: {self.user_writing_format}, extraia pontos que identificam o estilo de escrita do usuario, sem levar em consideração palavras usadas nas amostras. Após isso, desenvolva uma postagem de blog envolvente que destaque o {self.theme_to_search}.
                **Descrição**: Sua postagem deve ser informativa, mas acessível, atendendo a um público que pode ou não entender de tecnologia. Faça com que pareça legal, evite palavras complexas para que não pareça que o post foi escrito por uma IA.

                **Nota**: {self.__tip_section}
            '''),
            agent=agent,
            expected_output="Postagem completa de blog com pelo menos 4 parágrafos",
      )

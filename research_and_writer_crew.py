from crewai import Crew, Process
from textwrap import dedent
from research_and_writer_agents import ResearchAndWriterAgents
from research_and_writer_tasks import ResearchAndWriterTasks

class ResearchAndWriterCrew:
    def __init__(self, user_writing_format, theme_to_search):
        self.user_writing_format = user_writing_format
        self.theme_to_search = theme_to_search

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        research_and_write_team = ResearchAndWriterAgents()
        research_and_write_tasks = ResearchAndWriterTasks(self.user_writing_format, self.theme_to_search)

        # Define your custom agents and tasks here
        research = research_and_write_team.research()
        writer = research_and_write_team.writer()

        # Custom tasks include agent name and variables as input
        research_task = research_and_write_tasks.research_theme(
            research,
        )

        writer_task = research_and_write_tasks.write_post(
            writer,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[research, writer],
            tasks=[research_task, writer_task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        return result
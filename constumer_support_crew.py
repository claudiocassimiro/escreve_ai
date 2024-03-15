from crewai import Crew, Process
from textwrap import dedent
from attendant_agents import AttendantAgents
from attendant_tasks import AttendantTasks

class ConstumerSupportCrew:
    def __init__(self, message):
        self.message = message

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        customer_service_team = AttendantAgents()
        attendant_tasks = AttendantTasks(self.message)

        # Define your custom agents and tasks here
        customer_service_on_whatsApp = customer_service_team.customer_service_on_whatsApp()

        # Custom tasks include agent name and variables as input
        whatsapp_attendant = attendant_tasks.whatsapp_attendant(
            customer_service_on_whatsApp,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[customer_service_on_whatsApp],
            tasks=[whatsapp_attendant],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        return result
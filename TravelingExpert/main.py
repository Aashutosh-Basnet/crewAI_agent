import os
from crewai import Crew
from textwrap import dedent
from agents import RecommendationAgents
from tasks import CustomTasks


class VideoCrew:
    def __init__(self, topic):
        self.topic = topic

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = RecommendationAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        expert_tutorial_agent = agents.expert_tutorial_agent()
        tutorial_selection_expert = agents.tutorial_selection_expert()
        tutorial_description_expert = agents.tutorial_description_expert()

        # Custom tasks include agent name and variables as input
        plan_video = tasks.plan_video(
            expert_tutorial_agent,
            self.topic,
        )

        evaluate_video_quality = tasks.evaluate_video_quality(
            tutorial_selection_expert,
            self.topic,
        )

        create_learning_plan = tasks.create_learning_plan(
            tutorial_selection_expert,
            self.topic,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_tutorial_agent, tutorial_selection_expert, tutorial_description_expert],
            tasks=[plan_video, evaluate_video_quality, create_learning_plan],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Tutorial video recommender: ")
    print("-------------------------------")
    
    topic = input(
        dedent("""
            What do you want to lern
        """)
    )

    custom_crew = VideoCrew(var1, var2)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is your video recommendations:")
    print("########################\n")
    print(result)

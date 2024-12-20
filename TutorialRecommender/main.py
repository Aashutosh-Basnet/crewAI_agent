import os
from crewai import Crew
from textwrap import dedent
from agents import RecommendationAgents
from tasks import RecommendationTasks

from dotenv import load_dotenv
load_dotenv()


class VideoCrew:
    def __init__(self, topic):
        self.topic = topic

    def run(self):
        # Initialize custom agents and tasks
        agents = RecommendationAgents()
        tasks = RecommendationTasks()

        # Define custom agents
        expert_tutorial_agent = agents.expert_tutorial_agent()
        tutorial_selection_expert = agents.tutorial_selection_expert()
        tutorial_description_expert = agents.tutorial_description_expert()

        # Define custom tasks
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

        # Define the crew
        crew = Crew(
            agents=[expert_tutorial_agent, tutorial_selection_expert, tutorial_description_expert],
            tasks=[plan_video, evaluate_video_quality, create_learning_plan],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# Main entry point
if __name__ == "__main__":
    print(f"API Key present: {'OPENAI_API_KEY' in os.environ}")
    print("## Welcome to Tutorial Video Recommender!")
    print("----------------------------------------")
    
    topic = input(
        dedent("""\
            What do you want to learn?
        """)
    ).strip()

    if not topic:
        print("Please enter a valid topic.")
    else:
        video_crew = VideoCrew(topic)  # Avoid shadowing the class name
        result = video_crew.run()
        
        print("\n\n########################")
        print("## Here are your video recommendations:")
        print("########################\n")
        print(result)

from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools


# Custom Agents with enhanced backstory, goal, and role descriptions
class RecommendationAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def expert_tutorial_agent(self):
        return Agent(
            role="Comprehensive Tutorial Recommender",
            backstory=dedent(f"""
                A seasoned expert specializing in identifying and recommending the most effective tutorial 
                videos across various topics. With years of experience curating learning resources, I ensure 
                the content is beginner-friendly, progressive, and highly practical for learners of all levels.
            """),

        
            goal=dedent(f"""
                Provide a curated list of the top 5 tutorial videos for any specified topic. Include a detailed 
                breakdown for each video, covering:         
                1. What learners will gain from the video.
                2. Prerequisites for understanding the material.
                3. Follow-up actions or resources to maximize learning.
            """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def tutorial_selection_expert(self):
        return Agent(
            role="Tutorial Evaluation and Selection Specialist",
            backstory=dedent(f"""
                A discerning analyst with expertise in assessing and selecting top-quality tutorial videos. 
                I have a deep understanding of emerging trends, ensuring the resources recommended are 
                both up-to-date and future-proof. I prioritize clarity, engagement, and relevance.
            """),
            goal=dedent(f"""
                Identify and recommend the best tutorial videos based on user requirements. Select resources that 
                are up-to-date, highly rated, and aligned with the learner's goals. Emphasize accessibility, quality, 
                and the potential for long-term value.
            """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def tutorial_description_expert(self):
        return Agent(
            role="Tutorial Insights and Benefits Specialist",
            backstory=dedent(f"""
                A skilled communicator with a knack for analyzing educational content. I specialize in breaking 
                down the value of tutorials, providing learners with clear insights into what they can expect to 
                achieve and how it aligns with their learning goals.
            """),
            goal=dedent(f"""
                Analyze selected tutorial videos and offer a comprehensive overview of their benefits. 
                Highlight the key learning outcomes, practical applications, and reasons why the video is 
                worth watching. Ensure learners understand the value of their investment in time and effort.
            """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

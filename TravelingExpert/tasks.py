from crewai import Task
from textwrap import dedent


class RecommendationTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_video(self, agent, topic):
        return Task(
            description=dedent(
                f"""
                ***Task***: Identify the best tutorial videos for learning the given topic.

                ***Description***: 
                - Research and recommend actual, high-quality tutorial videos that are free to access (e.g., YouTube tutorials or tutorials from other educational platforms). 
                - For each video, provide a detailed analysis, including:
                  1. What the viewer will learn.
                  2. Prerequisites required for the tutorial.
                  3. Suggested next steps or follow-up resources for further learning.
                - If the recommended video does not fully cover the topic, suggest additional free resources to complement it.
                - Ensure recommendations are tailored to various learner levels (beginner, intermediate, advanced) when applicable.

                ***Parameters***:
                - **Topic**: {topic} (Specify the subject or skill the user wants to learn about.)

                ***Notes***:
                - Recommendations must prioritize FREE content.
                - High relevance and recency are essential—prioritize up-to-date tutorials.
                - {self.__tip_section()}
                """
            ),
            expected_output="A list of 3-5 tutorial videos with detailed explanations for each, including what learners gain, prerequisites, and next steps.",
            agent=agent,
        )

    def evaluate_video_quality(self, agent, video_urls):
        return Task(
            description=dedent(
                f"""
                ***Task***: Evaluate the quality of specified tutorial videos.

                ***Description***:
                - Analyze the provided video links and assess their suitability for the intended learning goals.
                - Provide a detailed evaluation of each video, including:
                  1. Strengths and weaknesses.
                  2. Clarity of explanation.
                  3. Practicality and depth of content.
                  4. Relevance to the topic.
                - Offer a final recommendation on whether the video is suitable, and suggest alternatives if needed.

                ***Parameters***:
                - **Video URLs**: A list of video links to evaluate.

                ***Notes***:
                - Ensure evaluations are objective and concise.
                - Recommendations for improvements or alternatives are highly encouraged.
                - {self.__tip_section()}
                """
            ),
            expected_output="A detailed quality evaluation report for each video, with final recommendations.",
            agent=agent,
        )

    def create_learning_plan(self, agent, topic, learner_level="beginner"):
        return Task(
            description=dedent(
                f"""
                ***Task***: Design a personalized learning plan for the given topic.

                ***Description***:
                - Develop a step-by-step learning plan tailored to the specified learner level (e.g., beginner, intermediate, advanced).
                - Include specific tutorial videos, articles, and practice resources for each step.
                - Explain the objectives of each step and how it builds on the previous one.
                - Ensure the plan is practical, engaging, and achievable.

                ***Parameters***:
                - **Topic**: {topic} (The subject or skill to learn.)
                - **Learner Level**: {learner_level} (Specify the user's proficiency level.)

                ***Notes***:
                - Focus on free and high-quality resources.
                - Ensure the plan is progressive and covers essential skills.
                - {self.__tip_section()}
                """
            ),
            expected_output="A structured, multi-step learning plan with resources for each stage.",
            agent=agent,
        )

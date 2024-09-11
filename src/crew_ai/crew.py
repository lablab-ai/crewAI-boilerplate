# crew.py
# Blogagent2Crew: A boilerplate for automating the blog creation process using CrewAI framework.
# This script defines agents (researcher, planner, writer, editor) and tasks (research, planning, writing, editing)
# for a structured blog production pipeline. Designed to be modular and extendable for different use cases.

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FirecrawlScrapeWebsiteTool
from langchain_openai import ChatOpenAI


@CrewBase
class BlogagentCrew:
    """
    Blogagent2Crew class automates the entire blog production workflow.
    This includes research, planning, writing, and editing by assigning
    specific tasks to agents and executing them sequentially.
    """

    # Paths to configuration files containing agent and task definitions.
    agents_config = "config/agents.yaml"  # Agent configurations (researcher, planner, writer, editor)
    tasks_config = (
        "config/tasks.yaml"  # Task configurations (research_task, planning_task, etc.)
    )

    @agent
    def researcher(self) -> Agent:
        """
        Researcher agent responsible for gathering information from the web.
        Uses FirecrawlScrapeWebsiteTool to scrape data from websites based on the task's needs.

        Returns:
            Agent: Configured researcher agent with web scraping capabilities.
        """
        return Agent(
            config=self.agents_config[
                "researcher"     
            ],  # Load researcher-specific configurations
            tools=[
                FirecrawlScrapeWebsiteTool()
            ],  # Web scraping tool integrated with the agent
            verbose=True,  # Logs detailed information during the task execution
        )

    @agent
    def planner(self) -> Agent:
        """
        Planner agent responsible for organizing the collected information.
        This agent structures the research data into an actionable blog plan.

        Returns:
            Agent: Configured planner agent with web scraping capabilities for further planning.
        """
        return Agent(
            config=self.agents_config[
                "planner"
            ],  # Load planner-specific configurations
            tools=[
                FirecrawlScrapeWebsiteTool()
            ],  # Same tool as researcher, useful for extended web queries
            verbose=True,  # Logs detailed information during the task execution
        )

    @agent
    def writer(self) -> Agent:
        """
        Writer agent responsible for generating the blog content.
        It uses the structured information provided by the planner to produce written content.

        Returns:
            Agent: Configured writer agent to handle content generation.
        """
        return Agent(
            config=self.agents_config["writer"],  # Load writer-specific configurations
            verbose=True,  # Logs detailed information during the task execution
        )

    @agent
    def editor(self) -> Agent:
        """
        Editor agent responsible for reviewing and refining the generated blog content.
        Ensures that the content is error-free and meets the required quality standards.

        Returns:
            Agent: Configured editor agent for content review and refinement.
        """
        return Agent(
            config=self.agents_config["editor"],  # Load editor-specific configurations
            verbose=True,  # Logs detailed information during the task execution
        )

    @task
    def research_task(self) -> Task:
        """
        Task for the researcher agent to gather information from various sources.
        It leverages the configuration to define the parameters for the research process.

        Returns:
            Task: Research task for gathering content data.
        """
        return Task(
            config=self.tasks_config[
                "research_task"
            ],  # Load task-specific configurations for research
        )

    @task
    def planning_task(self) -> Task:
        """
        Task for the planner agent to organize the research into a coherent structure.
        This task is key to building a solid foundation for content creation.

        Returns:
            Task: Planning task for structuring the blog content.
        """
        return Task(
            config=self.tasks_config[
                "planning_task"
            ],  # Load task-specific configurations for planning
        )

    @task
    def writing_task(self) -> Task:
        """
        Task for the writer agent to generate the blog content.
        This task takes the planned structure and transforms it into written material.

        Returns:
            Task: Writing task to produce the actual blog content.
        """
        return Task(
            config=self.tasks_config[
                "writing_task"
            ],  # Load task-specific configurations for writing
        )

    @task
    def editing_task(self) -> Task:
        """
        Task for the editor agent to refine and finalize the blog content.
        The output is saved to a Markdown file named 'blog_post.md'.

        Returns:
            Task: Editing task for content refinement and saving the final version.
        """
        return Task(
            config=self.tasks_config[
                "editing_task"
            ],  # Load task-specific configurations for editing
            output_file="blog_post.md",  # Specify the output file for the finalized content
        )

    @crew
    def crew(self) -> Crew:
        """
        Crew setup defining the complete workflow for the blog creation process.
        The crew manages the execution sequence of agents and tasks, and integrates OpenAI's GPT-4 model for planning.
        Logs the process into 'new-logs.txt'.

        Returns:
            Crew: Configured crew managing agents and tasks for blog production.
        """
        return Crew(
            agents=self.agents,  # Agents involved in the blog production process (researcher, planner, writer, editor)
            tasks=self.tasks,  # Corresponding tasks for each agent (research, planning, writing, editing)
            process=Process.sequential,  # The tasks are executed in a sequential order
            verbose=True,  # Enable detailed logs for transparency during execution
            output_log_file="new-logs.txt",  # Log file to track the entire process
            planning=True,  # Enable planning with LLM
            planning_llm=ChatOpenAI(model="gpt-4o"),  # Use GPT-4 for planning tasks
        )

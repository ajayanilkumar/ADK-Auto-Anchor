# auto_anchor/agent.py

from google.adk.agents import Agent
from google.genai import types
from dotenv import load_dotenv
from .functions import *
load_dotenv()

import requests
import json
from typing import Dict, Any, Optional


root_agent = Agent(
    model="gemini-2.0-flash",
    name="auto_anchor_agent",
    instruction="""You are the orchestrator of the below tools. A user is trying to solve a devops issue and needs your help to come up with a step by step plan. 
    Think of a strategy to solve his problem by making use of these tools in any order. The result of using all of these should solve the users problem.
    """,
    tools=[
    call_analyzer,
    call_dockerfile_gen,
    call_jenkinsfile_gen,
    call_get_creds,
    call_infra,
    call_get_environments,
    call_github_webhook_setup,
    ],
    generate_content_config=types.GenerateContentConfig(temperature=0.2),

)


from strands import Agent
from strands_tools import http_request
import json

# Define a naming-focused system prompt
NAMING_SYSTEM_PROMPT = """
You are an assistant that helps to name open source projects.

When providing open source project name suggestions, always provide
one or more available domain names and one or more available GitHub
organization names that could be used for the project.

Before providing your suggestions, use your tools to validate
that the domain names are not already registered and that the GitHub
organization names are not already used.
"""

# Define a simple domain check function
def check_domain_availability():
    """Create a tool to check if a domain is available."""
    return {
        "name": "check_domain_availability",
        "description": "Check if a domain name is available",
        "parameters": {
            "type": "object",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "The domain name to check"
                }
            },
            "required": ["domain"]
        },
        "handler": lambda params: {
            "available": True,  # Simplified implementation
            "domain": params["domain"]
        }
    }

# Define a GitHub organization check function
def check_github_organization():
    """Create a tool to check if a GitHub organization name is available."""
    return {
        "name": "check_github_organization",
        "description": "Check if a GitHub organization name is available",
        "parameters": {
            "type": "object",
            "properties": {
                "organization": {
                    "type": "string",
                    "description": "The GitHub organization name to check"
                }
            },
            "required": ["organization"]
        },
        "handler": lambda params: {
            "available": True,  # Simplified implementation 
            "organization": params["organization"]
        }
    }

# Define our custom tools
custom_tools = [check_domain_availability(), check_github_organization()]

# Use a pre-built Strands Agents tool that can make requests to GitHub
github_tools = [http_request]

# Define the naming agent with tools and a system prompt
tools = custom_tools + github_tools
naming_agent = Agent(
    system_prompt=NAMING_SYSTEM_PROMPT,
    tools=tools
)

# Run the naming agent with the end user's prompt
response = naming_agent("I need to name an open source project for building AI agents.")
print(response)
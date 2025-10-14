
"""Chatbot using LangGraph with Tivaly Search API as a tool
The Response Obtained by TivalySearchAPI and how the LLM creates a final answer based on the Tavily's Response.
Now LLM can handle queries outside of trained data."""

# Loading important packages

import os
from langgraph.graph import StateGraph  # State
from typing import Annotated
from typing_extensions import TypedDict  # To Construct Agent State
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.adapters.openai import (
    convert_openai_messages,
)  # converts dictionaries to LangChain format
from langchain_openai import ChatOpenAI
from IPython.display import Image, display
from langgraph.prebuilt import (
    ToolNode,
    tools_condition,
)  # Tool Node: Adds Tool in the nodes


# Loading the env file
from dotenv import load_dotenv, find_dotenv

if load_dotenv(find_dotenv(), override=True):
    print(".env file loaded!")
else:
    print(".env file not found")

# Loading the OpenAI API Key
api_key = os.environ.get("OEPNAI_API_KEY")
if api_key:
    print("got the OpenAI API Key")
else:
    print("No OPENAI API KEY found")

# Configure the OpenAI API Key
client = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)
if client:
    print("OpenAI API KEY Authenticated")
else:
    print("Authentication Rejected, retry")


# Graph
class State(TypedDict):
    messages: Annotated[list, add_messages]


# Workflow
workflow = StateGraph(State)

tool = TavilySearchResults(max_results=3)  # Defined Tavily Tool
tools = [tool]  # Storing the Tool

# Setup LLM API
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
llm_with_tools = llm.bind_tools(tools=tools)  # bind llm with Tool - which tool can LLM call.


# Define Nodes
## LLM Node
def chatbot(state: State):
    """This function takes present State as an input and returns llm output."""
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Connect Nodes
workflow.add_node("chatbot", chatbot)

# Tavily Node
tool_node = ToolNode(tools=tools)
workflow.add_node("tools", tool_node)

# Define the Conditional Edges
workflow.add_conditional_edges(  # if the last AI message contains tool calls, route to the tool execution node; otherwise, end the workflow.
    "chatbot",
    tools_condition,  # end the workflow if no tools is called.
)

workflow.add_edge("tools", "chatbot")

workflow.set_entry_point("chatbot")
#workflow.set_finish_point("chatbot")

# Compile Graph
graph = workflow.compile()

# Simple Chatbot using LangGraph
print("WELCOME TO CHATBOT - LangGraph")
while True: 
    user_input = input("User: ")
    if user_input.lower() in ["bye", "quit", "exit", "q"]:
        print("Exited.")
        break

    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():  
                print("Assistant: ", value["messages"][-1])

        print("-"*50)   

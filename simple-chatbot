# Chatbot using LangGraph
# Loading important packages

import os
from langgraph.graph import StateGraph  # State
from typing import Annotated
from typing_extensions import TypedDict  # To Construct Agent State
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from IPython.display import Image, display

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

# Setup LLM API
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)


# Define Nodes
## LLM Node
def chatbot(state: State):
    """This function takes present State as an input and returns llm output."""
    return {"messages": [llm.invoke(state["messages"])]}


# Connect Nodes
workflow.add_node("chatbot", chatbot)
workflow.set_entry_point("chatbot")
workflow.set_finish_point("chatbot")

# Compile Graph
graph = workflow.compile()

# Visualize Graph
visualize_graph = display(Image(graph.get_graph().draw_mermaid_png()))

# Simple Chatbot using LangGraph
print("WELCOME TO CHATBOT - LangGraph")
while True:
    user_input = input("User: ")
    if user_input.lower() in ["bye", "quit", "exit", "q"]:
        print("Exiting..")
        break

    elif user_input.lower() in ["visualize", "visualise"]:
        print(visualize_graph)
        break

    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():
            print(f"Assistant Response: {value["messages"][-1].content}")
            print("-" * 100)

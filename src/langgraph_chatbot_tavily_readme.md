# LangGraph Chatbot with Tavily Search Tool

A conversational AI chatbot built with **LangGraph** and **OpenAI API** that can search the web in real-time using **Tavily Search API** as a tool.

## Features

- **Agentic Workflow**: Uses LangGraph's state management for structured conversation flow
- **Web Search Integration**: Accesses real-time information via Tavily Search API
- **Tool Calling**: LLM autonomously decides when to search the web
- **Conversational Memory**: Maintains context across multiple interactions

## Architecture

```
User Query → Chatbot Node → Conditional Edge
                 ↓                    ↓
            (No tool needed)    (Search needed)
                 ↓                    ↓
            Final Response      Tool Node (Tavily)
                                      ↓
                                Chatbot Node
                                      ↓
                                Final Response
```

## Usage

```bash
python langgraph_chatbot_tiavlyai_tool.py
```

### Example Interaction

```
WELCOME TO CHATBOT - LangGraph
User: Who won the 100m swimming gold medal at Paris Olympics 2024?
Assistant: At the Paris Olympics 2024, the gold medal in the Men's 100m 
Freestyle was won by Zhanle Pan from the People's Republic of China.
--------------------------------------------------
```

## Key Components

- **State Management**: `TypedDict` with message history tracking
- **LLM Node**: `chatbot()` - Processes user queries and generates responses
- **Tool Node**: Executes Tavily search when needed
- **Conditional Edges**: Routes to tools or ends workflow based on LLM decision

## How It Works

1. User sends a query
2. LLM analyzes if web search is needed
3. If yes → Calls Tavily API → Returns search results → LLM synthesizes answer
4. If no → LLM responds directly from knowledge
5. Maintains conversation state throughout

## Tech Stack

- **LangGraph**: Workflow orchestration
- **LangChain**: LLM integration framework
- **OpenAI GPT-4o-mini**: Language model
- **Tavily Search API**: Real-time web search
- **Python-dotenv**: Environment variable management

## Notes

- The chatbot automatically determines when to use web search
- Tavily returns top 3 results per query (configurable)
- Type `quit`, `exit`, `bye`, or `q` to end the conversation

## 🔗 Related Projects

- [Simple LangGraph Chatbot](../simple-chatbot) - Basic version without tool integration

## License

MIT License

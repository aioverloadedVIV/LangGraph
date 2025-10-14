# LangGraph Chatbot

A simple yet powerful conversational AI chatbot built using LangGraph and OpenAI's GPT-4o-mini model. This project demonstrates the fundamentals of building stateful conversational agents with LangGraph's graph-based workflow system.

## Features

- **Stateful Conversations**: Maintains conversation context using LangGraph's state management
- **Graph Visualization**: Built-in capability to visualize the conversation workflow
- **Interactive CLI**: Simple command-line interface for real-time chatting
- **Modular Architecture**: Clean separation of concerns with node-based design

## Prerequisites

- Python 3.8+
- OpenAI API Key
- Required Python packages (see Installation)

## Usage

Run the chatbot:

```bash
python langgraph_chatbot.py
```

### Available Commands

- Type your message to chat with the bot
- `visualize` or `visualise` - Display the conversation graph
- `bye`, `quit`, `exit`, or `q` - Exit the chatbot

### Example Interaction

```
WELCOME TO CHATBOT - LangGraph
User: Distance of Moon from Earth
Assistant Response: The average distance from the Earth to the Moon is 238,855 miles.
----------------------------------------------------------------------------------------------------
User: exit
Exiting..
```

### Components

1. **State Management**: Uses TypedDict to define conversation state with message history
2. **Workflow Graph**: StateGraph orchestrates the conversation flow
3. **LLM Node**: Chatbot function processes user input and generates responses
4. **Message Handling**: Annotated message list maintains conversation context

## Future Enhancements

- [ ] Add conversation memory limits
- [ ] Implement multi-turn conversation persistence
- [ ] Add system prompts for personality customization
- [ ] Support for multiple LLM providers
- [ ] Add conversation export functionality
- [ ] Implement streaming responses for better UX

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

Built with [LangGraph](https://github.com/langchain-ai/langgraph) by LangChain and powered by OpenAI's GPT models.

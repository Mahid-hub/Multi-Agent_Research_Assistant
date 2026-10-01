# AI Research Assistant

This project is a LangGraph-powered multi-agent research assistant that takes a user question, breaks it into sub-tasks, searches for relevant sources, reads and summarizes the results, and synthesizes a final research report.

## What it does

The system follows a simple research workflow:

1. The orchestrator decomposes a user question into several research tasks.
2. The search agent queries the web for each task using Tavily.
3. The reader agent reviews the returned content and extracts concise summaries.
4. The synthesizer combines the findings into one final report.

The pipeline is built in Python using LangGraph and OpenAI-compatible models via Groq.

## Project structure

- `main.py` - entry point for running the research workflow
- `Agents/orchestrator.py` - breaks the research question into tasks
- `Agents/searcher.py` - searches the web for each task
- `Agents/reader.py` - summarizes content from each search result
- `Agents/synthesizer.py` - combines summaries into the final report
- `src/graph.py` - defines the state graph and workflow connections
- `src/state.py` - typed state and structured output models
- `requirements.txt` - project dependencies

## Tech stack

- Python
- LangGraph
- LangChain
- OpenAI-compatible LLM via Groq
- Tavily search API
- Python-dotenv
- Langfuse observability

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your API keys:

   ```env
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

   Optional Langfuse configuration can also be added if you want tracing/telemetry enabled.

## Run the app

```bash
python main.py
```

Then enter a research question when prompted, for example:

```text
Enter your research question: What are the main benefits and risks of using microservices architecture?
```

## Example workflow

The app will:

- create research tasks like "benefits of microservices", "risks of microservices", and "when microservices are appropriate"
- search for sources related to each task
- extract summaries from the results
- generate a final synthesized report based only on the collected research summaries

## Notes

- The project uses the Groq OpenAI-compatible endpoint with the model `openai/gpt-oss-20b`.
- Search is performed through Tavily, with a commented-out DDGS option also present in the code.
- `src/state.py` defines the workflow state and expected structured outputs for tasks, reader summaries, and the final report.
- The graph is assembled in `src/graph.py` with a linear flow: orchestrator -> search -> reader -> synthesize.

## License

This project is for educational and research use. Adjust the license if you plan to distribute or publish it.

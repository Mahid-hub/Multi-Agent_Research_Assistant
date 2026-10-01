import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.state import FinalReport, ResearchState
from langfuse import observe

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise RuntimeError("GROQ_API_KEY is missing. Add it to .env or set it in the environment.")

llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)

structured_llm = llm.with_structured_output(FinalReport)

@observe(name="Synthesizer", as_type="chain")
def synthesize_report(state: ResearchState) -> ResearchState:
    if not state["reader_results"]:
        raise ValueError("No research summaries available.")
    
    result = ""
    for i, item in enumerate(state["reader_results"], start=1):
        result += f"""
                    Research Task: {item["task"]}
                    Source: {item["title"]}
                    URL: {item["url"]}
                    Summary: {item["summary"]}
                    """

    prompt = f"""
                You are the final research synthesizer.
                Research question:
                {state["question"]}
                Using ONLY the research summaries below, write a concise,
                well-structured research report.
                When multiple sources support the same fact,
                prefer reliable and authoritative sources where possible.
                Do not treat a source as authoritative merely because
                it appears in the research results.
                If sources conflict, do not silently choose one.
                Present the disagreement or uncertainty.
                Requirements:
                - Answer the research question directly.
                - Combine information from the sources.
                - Do not invent facts.
                - Keep the report concise.
                Research:
                {result}
                """

    result = structured_llm.invoke(prompt)
    state['final_report'] = result.report
    return state
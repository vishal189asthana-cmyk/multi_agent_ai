from langgraph.graph import StateGraph, START, END

from app.graph.state import AgentState
from app.graph.nodes import research_node, analysis_node
from app.graph.supervisor import supervisor_node


# Create graph
graph = StateGraph(AgentState)


# Register nodes
graph.add_node("supervisor", supervisor_node)
graph.add_node("research", research_node)
graph.add_node("analysis", analysis_node)


# Start with Supervisor
graph.add_edge(START, "supervisor")


# Routing function
def route_next(state):

    return state["next_agent"]


# Conditional routing
graph.add_conditional_edges(
    "supervisor",
    route_next,
    {
        "research": "research",
        "analysis": "analysis",
        "finish": END
    }
)


# Return to Supervisor after Research
graph.add_edge("research", "supervisor")


# Return to Supervisor after Analysis
graph.add_edge("analysis", "supervisor")


# Compile graph
workflow = graph.compile()
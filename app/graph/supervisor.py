def supervisor_node(state):
    
    print("\n--- Supervisor Executing ---")

    # Step 1: Check whether research is completed
    if not state.get("research_notes"):

        next_agent = "research"

    # Step 2: Check whether analysis is completed
    elif not state.get("analysis_report"):

        next_agent = "analysis"

    # Step 3: Both agents have completed their work
    else:

        next_agent = "finish"

    print("Supervisor Decision:", next_agent)

    return {
        "next_agent": next_agent
    }
import time

def stream_response(prompt):
    """Simulates an LLM generating text token by token."""
    simulated_response = f"Analysis of {prompt}: [Data] [Insight] [Conclusion]".split()

    for word in simulated_response:
        time.sleep(2)
        yield word + " "

# --- Client Usage ---
print("User: Analyze Jira tickets")
print("AI: ", end="", flush=True)

for chunk in stream_response("Jira tickets"):
    print(chunk, end="", flush=True)

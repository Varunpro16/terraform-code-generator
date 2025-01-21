from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.utilities.bash import BashProcess
from langchain.llms import OpenAI

# Initialize BashProcess
bash = BashProcess()

# Create the Python agent
agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=1000),
    tool=PythonREPLTool(),
    verbose=True,
)

# Run the command
agent_executor.run("""
    RUN THE COMMAND IN EXISTING TERMINAL
    COMMAND:
    streamlit run stream.py
""")

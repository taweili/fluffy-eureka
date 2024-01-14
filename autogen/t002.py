import autogen

config_list = [
    {
        'base_url': "http://localhost:8000",
        'model': "ollama/mistral",
        'api_key': "NULL"
    }
]

llm_config={
    "config_list": config_list
}


assistant = autogen.AssistantAgent(
    name="CTO",
    llm_config=llm_config,
    system_message="Chief technical officer of a tech company"
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
Write up a spec for a python program to print number from 1 to 100
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

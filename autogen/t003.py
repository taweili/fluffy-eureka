from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample.json
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")
assistant = AssistantAgent("assistant", 
                            llm_config={"config_list": config_list})

user_proxy = UserProxyAgent("user_proxy", 
                            human_input_mode="NEVER",
                            max_consecutive_auto_reply=5,
                            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
                            code_execution_config={"work_dir": "coding"})

user_proxy.initiate_chat(assistant, message="Get prime numbers between 1 to 100")
# This initiates an automated chat between the two agents to solve the task

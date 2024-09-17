import os

def print_env_vars():
    git_token = os.getenv("PIPE_AGENT_ENV_GIT_TOKEN_CLASSIC")
    repo_url = os.getenv("PIPE_AGENT_ENV_ARROW_REPO_GIT_URL")
    
    print("PIPE_AGENT_ENV_GIT_TOKEN_CLASSIC:", git_token)
    print("PIPE_AGENT_ENV_ARROW_REPO_GIT_URL:", repo_url)

print_env_vars()
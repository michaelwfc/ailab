
import os
from typing import Text
from pathlib import Path
import sys
from dotenv import load_dotenv, find_dotenv
import openai
from constants import OPENAI_API_KEY, OPENAI_API_BASE, AZURE, OPENAI_API_VERSION, DEPLOYMENT_NAME
from configs.config import VICUNA_API_KEY, VICUNA_API_BASE


def set_working_dir(project_name: Text = None, source_dir="src"):
    """set the working dir and add src dir to python path"""
    if project_name:
        working_dir = Path.home().joinpath(project_name)
    else:
        script_path = os.path.abspath(__file__)
        source_dir = Path(script_path).parent.parent.absolute()
        working_dir = Path(script_path).parent.parent.parent.absolute()

    os.chdir(working_dir)
    sys.path.extend([str(source_dir)])

    # print(f"sys.path={sys.path}")
    return working_dir


def load_env_variables_from_dotenv():
    _ = load_dotenv(find_dotenv())
    env_variable = os.environ
    return env_variable


def set_gpt_env(use_openai=True, use_vicuna=False, use_azure_openai=False):
    env_variables = load_env_variables_from_dotenv()
    _ = set_working_dir()
    print(f"working_dir={os.getcwd()}")

    if use_openai:
        openai.api_key = env_variables[OPENAI_API_KEY]
        if use_azure_openai:
            openai.api_base = AZURE
            openai.api_base = env_variables[OPENAI_API_BASE]
            openai.api_version = env_variables[OPENAI_API_VERSION]
            # deployment_name = env_variables[DEPLOYMENT_NAME]
    elif use_vicuna:
        openai.api_key = VICUNA_API_KEY
        openai.api_base = VICUNA_API_BASE


if __name__ == "__main__":
    set_working_dir()

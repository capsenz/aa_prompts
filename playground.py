"""
Play around with our models and prompts here!
"""
import os

from aleph_alpha_client import Client, CompletionRequest
from prompts import (
    chain_of_thought_qa_config,
    chain_of_thought_qa_german_config,
    entity_extraction_control_config,
    qa_control_config,
    qa_few_shot_config

)


if __name__ == "__main__":
    PROMPT_CONFIG_TO_TEST = chain_of_thought_qa_config
    TOKEN = os.getenv("AA_TOKEN")
    CLIENT = Client(TOKEN)

    response = CLIENT.complete(
        request=CompletionRequest(
            prompt=PROMPT_CONFIG_TO_TEST.prompt,
            **PROMPT_CONFIG_TO_TEST.settings
        ),
        model=PROMPT_CONFIG_TO_TEST.model
    )
    completion = response.completions[0].completion
    print(f"COMPLETION:\n\n{completion}")

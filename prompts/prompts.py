from aleph_alpha_client import Client, Prompt

from .definitions.chain_of_thought_qa import (
    prompt as chain_of_thought_qa_prompt,
    settings as chain_of_thought_qa_settings,
    model as chain_of_thought_qa_model
)


class PromptConfig:
        
    def __init__(
        self,
        prompt: str,
        settings: dict,
        model: str
    ):
        self.prompt = Prompt.from_text(prompt)
        self.settings = settings
        self.model = model


chain_of_thought_qa_config = PromptConfig(
    prompt=chain_of_thought_qa_prompt,
    settings=chain_of_thought_qa_settings,
    model=chain_of_thought_qa_model
)

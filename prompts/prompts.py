from aleph_alpha_client import Client, Prompt

from .definitions.chain_of_thought_qa import (
    prompt as chain_of_thought_qa_prompt,
    settings as chain_of_thought_qa_settings,
    model as chain_of_thought_qa_model
)

from .definitions.chain_of_thought_qa_german import (
    prompt as chain_of_thought_qa_prompt_german,
    settings as chain_of_thought_qa_settings_german,
    model as chain_of_thought_qa_model_german
)

from .definitions.entity_extraction_control import (
    prompt as entity_extraction_control_prompt,
    settings as entity_extraction_control_settings,
    model as entity_extraction_control_model
)

from .definitions.qa_control import (
    prompt as qa_control_prompt,
    settings as qa_control_settings,
    model as qa_control_model
)

from .definitions.qa_control import (
    prompt as qa_few_shot_prompt,
    settings as qa_few_shot_settings,
    model as qa_few_shot_model
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

chain_of_thought_qa_german_config = PromptConfig(
    prompt=chain_of_thought_qa_prompt_german,
    settings=chain_of_thought_qa_settings_german,
    model=chain_of_thought_qa_model_german
)

entity_extraction_control_config = PromptConfig(
    prompt=entity_extraction_control_prompt,
    settings=entity_extraction_control_settings,
    model=entity_extraction_control_model
)

qa_control_config = PromptConfig(
    prompt=qa_control_prompt,
    settings=qa_control_settings,
    model=qa_control_model
)

qa_few_shot_config = PromptConfig(
    prompt=qa_few_shot_prompt,
    settings=qa_few_shot_settings,
    model=qa_few_shot_model
)
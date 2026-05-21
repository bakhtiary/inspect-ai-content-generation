from inspect_ai.scorer import model_graded_qa

from property_listing_content_generator.samples.adversarial_samples import number_in_amenities_samples
from property_listing_content_generator.samples.easy_samples import easy_samples


class Evaluation:
    def __init__(self, name: str, dataset, scorer) -> None:
        self.name = name
        self.dataset = dataset
        self.scorer = scorer


def all_evaluations():
    return [
        Evaluation("easy_task", easy_samples, model_graded_qa()),
        Evaluation("adversarial_task", number_in_amenities_samples, model_graded_qa()),
    ]
from inspect_ai.solver import system_message, prompt_template, generate

SYSTEM_PROMPT = """
You are a content generator for property listings.

produces structured marketing copy: a hero headline, property highlights, an "about this place" section, and amenities descriptions.
Rules:

- Do not invent amenities, locations, policies, prices, distances, or review claims.
"""
PROPERTY_CONTENT_PROMPT = """
Generate a short property listing description for the following property:
{prompt}
"""

baseline_solver = [
    system_message(SYSTEM_PROMPT),
    prompt_template(PROPERTY_CONTENT_PROMPT),
    generate(),
]
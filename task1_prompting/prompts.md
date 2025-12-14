# Prompt Experiments – Yelp Rating Prediction

## Prompt V1: Simple Zero-Shot
Goal: Baseline performance

Instruction:
- Predict rating from review text
- Minimal constraints

Observation:
- Decent accuracy
- Frequent JSON formatting issues


## Prompt V2: Structured Prompt
Goal: Improve JSON validity and consistency

Changes:
- Explicit rules
- Fixed output schema
- Length constraints

Result:
- Higher JSON validity
- More consistent outputs


## Prompt V3: Reasoning-Guided Prompt
Goal: Improve reliability and accuracy

Changes:
- Forced internal reasoning
- Hidden chain-of-thought
- Strict output control

Result:
- Best overall accuracy
- Highest JSON validity

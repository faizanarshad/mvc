from transformers import pipeline

def generate_story(prompt: str, num_segments: int = 3):
    generator = pipeline('text-generation', model='gpt2')
    story = []
    current_prompt = prompt
    for _ in range(num_segments):
        result = generator(current_prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
        # Extract only the new segment
        segment = result[len(current_prompt):].strip()
        story.append(segment)
        current_prompt += ' ' + segment
    return story 
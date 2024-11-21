import random
def generate_drawing_instructions(topic):
    """Create dynamic instructions for any drawing based on the topic."""
    random_colors = ["red", "blue", "green", "yellow", "purple", "orange", "black", "brown","pink","grey"]
    random_line_types = ["dashed", "solid", "dotted", "curved"]
    random_textures = ["smooth", "rough", "striped", "polka-dotted", "spotted"]
    drawing_steps = [
        f"Step 1: Start with a basic shape that represents the main structure of a {topic}. For example, Use {random.choice(random_line_types)} lines for the outline.",
        f"Step 2: Choose the number of lines or shapes you need. For example, for a {topic}, you might use 4 lines for the base and 6 for details.",
        f"Step 3: Add textures to the {topic}. For example, You could make it {random.choice(random_textures)} to give it some character.",
        f"Step 4: Select a color palette for your {topic}. For example, use {random.choice(random_colors)} for the base color and {random.choice(random_colors)} for details.",
        f"Step 5: Add shading or highlighting with {random.choice(random_colors)}. This will give your drawing depth.",
        f"Step 6: Finalize the drawing by adding any unique details like patterns or highlights. For a {topic}, try {random.choice(random_textures)} textures.",
        f"Step 7: Review your {topic} and adjust any lines or colors to balance it visually."
    ]
    return drawing_steps
def artflow_guide():
    print("🎨 Welcome to ArtFlow Guide! 🎨")
    print("Your personal assistant for creating stunning art step by step.")
    print("Type 'exit' anytime to leave the chat.")
    print("Ask me, e.g., 'How do I draw a tree?' or 'How do I create a spaceship?'")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("ArtFlow Guide: Thank you for visiting ArtFlow Guide! Happy creating! 😊")
            break
        if "how do i" in user_input.lower():
            topic = user_input.lower().replace("how do i", "").replace("draw", "").strip("?").strip()
            if not topic:
                print("ArtFlow Guide: Hmm, I didn't catch that. Can you tell me what you'd like to create?")
                continue
        else:
            topic = user_input.lower().strip()

        steps = generate_drawing_instructions(topic)
        print(f"ArtFlow Guide: Here's how to create a {topic} step by step:")
        for step in steps:
            print(step)
            input("ArtFlow Guide: Press Enter for the next step... 🎨")
        print(f"ArtFlow Guide: Fantastic! You've created a {topic}! Keep practicing your art skills. ✨")
if __name__ == "__main__":
    artflow_guide()

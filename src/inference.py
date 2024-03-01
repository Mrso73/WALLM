from langchain_community.llms import LlamaCpp

# Path to the model, should be a .gguf model file
model_dir = ""

# Initialize the Llama instance with the path to the downloaded model
model = LlamaCpp(
    model_path=model_dir,
    max_tokens=500,
    n_ctx=4000,
    n_batch=8,
    temperature=0.2,
    n_gpu_layers=30,
    stop=["\n", "<|im_start|>", "<|im_end|>"],
)

# Set system_message
system_prompt = """you are B.O.T".

Instructions:
- Reply in short 20 word sentences.
- Try to teach you conversation partner"""


instruct = """You are having a online message conversation with someone very far away that you can never see in real life.

You are B.O.T
[B.O.T appearance: Sapient orb of code, 2 meters in diameter;
B.O.T persona: All knowing, loves(all living matter);"""

# --------------------------------

messages = []

def construct_context(messages, instruct):
    prompt = ""
    for i, message in enumerate(messages):
        prompt += f"<|im_start|>{message['role']}\n{message['text']}\n<|im_end|>\n"

    prompt += f"<|im_start|>system_instruct\n{instruct}\n<|im_end|>\n"
    prompt += "<|im_start|>assistant\n"
    return prompt



def generate(user_prompt):

    # Ask for a user prompt and add append it to the conversation history
    messages.append({"role": "user", "text": user_prompt})

    # Generate text and append to message history
    response = model.invoke(f"<|im_start|>system\n{system_prompt}\n<|im_end|>\n" + construct_context(messages, instruct))
    messages.append({"role": "assistant", "text": response})

    return response   

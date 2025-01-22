from transformers import AutoTokenizer
import transformers
import torch
import gc

# be sure to login
# huggingface-cli login
# also had to do some other installs
# !pip install accelerate\
#             protobuf\
#             sentencepiece\
#             torch\
#             transformers

class Llama2():
    def __init__(self):
        model = "meta-llama/Llama-2-7b-chat-hf"
        self.tokenizer = AutoTokenizer.from_pretrained(model, legacy=False)
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=model,
            tokenizer=self.tokenizer,
            torch_dtype=torch.float16,
            device_map="auto",
            temperature=0.0,
            repetition_penalty=1.1,
            do_sample=False
        )
        
    def query(self, q):
        with torch.no_grad():
            # sequences = self.pipeline(
            #     q,
            #     do_sample=True,
            #     top_k=10,
            #     num_return_sequences=1,
            #     eos_token_id=self.tokenizer.eos_token_id,
            #     temperature=0.01,
            #     return_full_text = False
            # )
            sequences = self.pipeline(
                q,
                return_full_text = False,
            )
        answer = sequences[0]['generated_text']
        del sequences
        gc.collect()
        torch.cuda.empty_cache()
        return answer

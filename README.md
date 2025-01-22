# Approaching Human-Level Forecasting with Language Models Reasoning Model Simple Implementation

> You can check a more detailed implementation and an alternative fine tunned version implementation in the origianl paper.

Specs:
> LLM : "meta-llama/Llama-2-7b-chat-hf"

## Tree Structure
    |-news_api.py
    |-sample_out2.txt
    |-sample_out.txt
    |-LICENSE
    |-constants.py
    |-utils.py
    |-main.py
    |-README.md
    |-prompts.py
    |-requirements.txt
    |-llama2.py


#### news_api.py
api calls to the [TheNewsAPI](https://www.thenewsapi.com/documentation), specifically: GET https://api.thenewsapi.com/v1/news/all?api_token=YOUR_API_TOKEN&language=en&limit=3
* due to the free tier limit you can only get 3 articles per call, however in the original paper they use 10 and select from there.
* Also, you need to create an account and get an API TOKEN to use the API.
* Using pip package "newspaper" [newspaper4k](https://github.com/AndyTheFactory/newspaper4k) to parse the article's contents after getting the URLs from TheNewsAPI.
#### sample_out.txt & sample_out2.txt
Example outputs on 2 runs
* took approx. 30 minutes in my machine (RTX2080ti)
#### constants.py
Contains some constants like Llama2's cutoff date found in the model card.
And some intermediate outputs that you can use to run main.py from some later point if needed.
#### LICENSE
basic MIT.
#### utils.py
Some parsing functions.
Important to note that the parsing functions depend a lot on the prompts used. They work for the current prompts but may have to be changed if you change the prompts. Also note that the prompts are taken from the Appendix in the original paper.
#### main.py
The main execution code to produce an output.
TODO: implement the mean calculation from the outputs (parsing needed).
#### main.py
Main file from which everything is run: ``python3 main.py``
#### README.md
The file you are reading.
#### prompts.py
Mimiking LangChain's prompts but instead using lambda functions for better readability.
#### llama2.py
Class to instantiate the HF transformer's model,
TODO: fix CUDA memory management (for some reason after a couple of inference calls the model runs out of memory, to mitigate this the main.py execution deletes the model and instantiates it again, thus making it slower in execution time).
#### requirements.txt
My conda env pip requirements.

--------------

### Future Ideas:
Complete implementation putting some money into it, since everything I used for this implementation was Free.
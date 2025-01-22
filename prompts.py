# replicates a little the Langchain Prompt Class
SEARCH_QUERY_1 = lambda question,background,max_words,num_keywords : \
f'''
<<SYS>> I will provide you with a forecasting question and the background information for the question.
Question: {question}
Background: {background}
<</SYS>>
[INST]
Task:
- Generate brief search queries (up to {max_words} words each) to gather information on Google that
could influence the forecast.
You must generate this exact amount of queries: {num_keywords}
Your response should take the following structure: Thoughts: {{ Insert your thinking here. }}
Search Queries: {{ Insert the queries here. Use semicolons to separate the queries. }}[/INST]
'''
SEARCH_QUERY_2 = lambda question,background,max_words,num_keywords :\
f'''
<<SYS>> I will provide you with a forecasting question and the background information for the question. I will
then ask you to generate short search queries (up to {max_words} words each) that I’ll use to find
articles on Google News to help answer the question.
Question: {question}
Background: {background}
<</SYS>>
[INST]
You must generate this exact amount of queries: {num_keywords}
Start off by writing down sub-questions. Then use your sub-questions to help steer the search queries
you produce.
Your response should take the following structure: Thoughts: {{ Insert your thinking here. }}
Search Queries: {{ Insert the queries here. Use semicolons to separate the queries. }}[/INST]
'''
ISOLATE_QUERY = lambda raw_answer :\
f'''
<<SYS>>You are an assistant helping parse a string.<</SYS>>
[INST] Extract the Search Queries for me from this string {raw_answer} and put them in a numbered list.[/INST]
'''

RELEVANCE_RANK = lambda question, background, resolution_criteria, article :\
f'''
<<SYS>> Please consider the following forecasting question and its background information. After that, I will give
you a news article and ask you to rate its relevance with respect to the forecasting question.
Question: {question}
Question Background:{background}
Resolution Criteria:{resolution_criteria}
Article: {article}
<</SYS>>
[INST]
Please rate the relevance of the article to the question, at the scale of 1-6
1 – irrelevant
2 – slightly relevant
3 – somewhat relevant
4 – relevant
5 – highly relevant
6 – most relevant
Guidelines:
- You don’t need to access any external sources. Just consider the information provided.
- Focus on the content of the article, not the title.
- If the text content is an error message about JavaScript, paywall, cookies or other technical issues,
output a score of 1.
Your response should look like the following:
Thought: {{ Insert your thinking }}
Rating: {{ Insert answer here }}[/INST]
'''

SUMMARIZE = lambda article, question, background:\
f'''
[INST] I want to make the following article shorter (condense it to no more than 100 words).
Article: {article}
When doing this task for me, please do not remove any details that would be helpful for making
considerations about the following forecasting question.
Forecasting Question: {question}
Question Background: {background}[/INST]
'''

PREDICTION = lambda question, background, resolution_criteria, retrieved_info:\
f'''
<SYS>
Question: {question}
Question Background: {background}
Resolution Criteria: {resolution_criteria}
We have retrieved the following information for this question:
{retrieved_info}
<</SYS>>
[INST]
Instructions:
1. Given the above question, rephrase and expand it to help you do better answering. Maintain all
information in the original question.
{{ Insert rephrased and expanded question. }}
2. Using your knowledge of the world and topic, as well as the information provided, provide a few
reasons why the answer might be no. Rate the strength of each reason.
{{ Insert your thoughts }}
3. Using your knowledge of the world and topic, as well as the information provided, provide a few
reasons why the answer might be yes. Rate the strength of each reason.
{{ Insert your thoughts }}
4. Aggregate your considerations. Think like a superforecaster (e.g. Nate Silver).
{{ Insert your aggregated considerations }}
5. Output an initial probability (prediction) given steps 1-4.
{{ Insert initial probability }}
6. Evaluate whether your calculated probability is excessively confident or not confident enough. Also,
consider anything else that might affect the forecast that you did not before consider (e.g. base rate of
the event).
{{ Insert your thoughts }}
7. Output your final prediction (a number between 0 and 1) with an asterisk at the beginning and end
of the decimal.
{{ Insert your answer }} [/INST]
'''
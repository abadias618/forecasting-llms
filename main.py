from prompts import *
import utils
import news_api
from llama2 import Llama2
from constants import RANKSS, SUMSS
import torch
import gc

sample_question = {
    "question":"Who will win the 2024 USA Election?",
    "start_date":"2023-04-17",
    "end_date":"2023-04-30",
    "resolve_date":"2024-11-05",
    "background": 'Presidential Elections are being held on November 2024',
    "resolution":'Resolves to "Trump" if Donald Trump wins or "Biden" if Joe Biden wins'
}

def main():
    # Step 1: Search query generation
    llm = Llama2()
    # We'll stay with query 2 since it is more predictable
    search_q2 = llm.query(SEARCH_QUERY_2(
        sample_question["question"],
        sample_question["background"],
        30,# max words
        3,# max queries
    ))
    print("Q2\n",search_q2)
    just_qs_2 = search_q2.split("Search Queries:")
    queries2 = llm.query(ISOLATE_QUERY(just_qs_2))
    print("\nqueries raw\n",queries2)
    
    # Step 2: News retrieval
    queries2_separated = utils.get_queries_as_list(queries2)
    print("\nqueries2_separated\n",queries2_separated)
    assert len(queries2_separated) > 0, "queries is empty"
    news = []
    for q in queries2_separated:
        news += news_api.get_news(q)
    #assert len(news)>0, "news is empty"
    print("\nnews\n",news)
    
    #memory management
    del llm
    llm = Llama2()
    
    # Step 3: Relevance ranking
    rankings = []
    for art in news:
        rank_query = llm.query(RELEVANCE_RANK(
            sample_question["question"],
            sample_question["background"],
            sample_question["resolution"],
            art
        ))
        print("\nrank_query",rank_query)
        rankings.append(rank_query)
    print("\nrankings\n", rankings)
    
    summaries = []
    for art in news:
        summ = llm.query(SUMMARIZE(
            art,
            sample_question["question"],
            sample_question["background"],
        ))
        print("\nsummary:",summ)
        summaries.append(summ)
    print("\nSUMS\n",summaries)
    
    #cheating
    #rankings = RANKSS
    #summaries = SUMSS
    
    #memory management
    del llm
    llm = Llama2()
    
    predictions = []
    for i in range(len(rankings)):
        if utils.get_ranking(rankings[i]) > 3:
            pred = llm.query(PREDICTION(
                sample_question["question"],
                sample_question["background"],
                sample_question["resolution"],
                summaries[i],
            ))
            print("pred",pred)
            predictions.append(pred)
    print("\nPREDS\n",predictions)
    print("\n\ndone")

if __name__ == '__main__':
    main()
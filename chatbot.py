from sklearn.metrics.pairwise import cosine_similarity

def chatbot_ans(loaded_model, sentence_embeddings, text:str, datafame):
    
    text = text+"?"
    test_embeddings=loaded_model.encode([text])
        
    # find similary scores (Asked query vs trained queries)
    score=cosine_similarity(sentence_embeddings, test_embeddings, dense_output=False)
    
    # find the index of the trained query/question which have maximum similarity
    max_similarity = 0
    max_similarity_index = 0
    for i, ques in enumerate(score):
        if max_similarity<=ques[0]:
            max_similarity = ques[0]
            max_similarity_index = i
    
    ans_text = datafame.iloc[max_similarity_index, 1]
    
    if max_similarity < 0.9:
        ans_text = "দুঃখিত। এই মুহূর্তে আপনার প্রশ্নের উত্তরটি দেয়া সম্ভব হচ্ছেনা। অনুগ্রহ করে আপনার নিকটস্থ শাখায় সরাসরি যোগাযোগ করুন।" 
    
    return ans_text, max_similarity








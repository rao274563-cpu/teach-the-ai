def get_next_challenge(mastery):

    if mastery < 50:
        return "Explain why training accuracy alone can be misleading."
    
    elif mastery < 75:
        return "Explain the difference between training performance and performance on unseen data."
    
    elif mastery < 90:
        return "If a model get 98% training accuracy but 65% test accuracy. Is it overfitting? Explain why."
    
    else:
        return "You are ready for the next concept."
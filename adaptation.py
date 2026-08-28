def get_next_challenge(mastery, concept="overfitting"):
    if concept == "features_labels":
        if mastery < 50:
            return "Which one is the input to a machine learning model: a feature or a label?"

        elif mastery < 75:
            return "Explain a difference between a feature and a label using a simple example."

        elif mastery < 90:
            return "For a housse price prediction model, the house size is given as the input and the price is predicted." \
                   "Which is the feature and which is the label? Explain why?"

        else:
            return "You are ready for the next"

    if mastery < 50:
        return "Explain why training accuracy alone can be misleading."
    
    elif mastery < 75:
        return "Explain the difference between training performance and performance on unseen data."
    
    elif mastery < 90:
        return "If a model get 98% training accuracy but 65% test accuracy. Is it overfitting? Explain why."
    
    else:
        return "You are ready for the next concept."
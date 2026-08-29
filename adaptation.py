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
            return "You are ready for the next concept."

    if concept == "training_testing":
        if mastery < 50:
            return "Why do we test a machine  learning model on a data it has not seen during training?"

        elif mastery < 75:
            return "Explain the difference between training data and testing data?"

        elif mastery < 90:
            return "A model perform very well on training data but poorly on test data. What does this tell you?"

        else:
            return "You are ready for the next concept."

    if concept == "model_evaluation":
        if mastery < 50:
            return "Is accuracy always enough to decide whether classificarion model is good?"

        elif mastery < 75:
            return "Why might we use metrics other that accuracy to evaluate a classification model?" 

        elif mastery < 90:
            return "A model has 95% accuracy but performs poorly on the minority class. Is accuracy enough? Wxplain why."   

        else:
            return "You have completed the machine learning path."

    if mastery < 50:
        return "Explain why training accuracy alone can be misleading."
    
    elif mastery < 75:
        return "Explain the difference between training performance and performance on unseen data."
    
    elif mastery < 90:
        return "If a model get 98% training accuracy but 65% test accuracy. Is it overfitting? Explain why."
    
    else:
        return "You are ready for the next concept."
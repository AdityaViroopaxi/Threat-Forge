def calculate_risk_score(feed_confidence, recency_weight, category_weight, w1=0.5, w2=0.3, w3=0.2):
    score = (feed_confidence * w1) + (recency_weight * w2) + (category_weight * w3)
    return score

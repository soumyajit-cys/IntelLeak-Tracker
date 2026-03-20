from database import keyword_collection, alert_collection
from datetime import datetime

def match_keywords(data):
    keywords = list(keyword_collection.find({}))
    alerts = []

    for kw in keywords:
        keyword = kw["keyword"]

        for category in data:
            for value in data[category]:
                if keyword.lower() in value.lower():
                    alert = {
                        "keyword": keyword,
                        "match": value,
                        "type": category,
                        "risk": get_risk(category),
                        "timestamp": datetime.utcnow()
                    }
                    alert_collection.insert_one(alert)
                    alerts.append(alert)
    return alerts

def get_risk(category):
    return {
        "usernames": "LOW",
        "emails": "MEDIUM",
        "hashes": "HIGH"
    }.get(category, "LOW")
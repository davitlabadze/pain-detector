import re

KEYWORDS = {
    "slow": "Time pain",
    "manual": "Time pain",
    "waste": "Time pain",
    "cost": "Cost pain",
    "expensive": "Cost pain",
    "error": "Data pain",
    "fail": "Risk pain",
    "alerts": "Time pain",
    "bug": "Data pain",
    "crash": "Risk pain",
    "memory leak": "Data pain",
    "downtime": "Risk pain",
    
    "მოწყვეტა": "Risk pain",
    "მოწყვეტები": "Risk pain",
    "მოწყვეტილი": "Risk pain",
    "მოწყვეტილი კავშირი": "Risk pain",
    "მოწყვეტილი ინტერნეტი": "Risk pain",
    "მოწყვეტილი სერვისი": "Risk pain",
    "მოწყვეტილი სისტემა": "Risk pain",
    "მოწყვეტილი აპლიკაცია": "Risk pain",
    "მოწყვეტილი პროგრამა": "Risk pain",
    "მოწყვეტილი ქსელი": "Risk pain",
    "მოწყვეტილი სიგნალი": "Risk pain",
    "მოწყვეტილი კავშირი": "Risk pain",
    "მოწყვეტილი ინტერნეტი": "Risk pain",
    "მოწყვეტილი სერვისი": "Risk pain",
    "მოწყვეტილი სისტემა": "Risk pain", 
    "ძვირი": "Cost pain",
    "ღირებულება": "Cost pain",
    "შეცდომა": "Data pain",
    "ვერ მუშაობს": "Risk pain",
    "შეცდომები": "Data pain",
    "ფორები": "Time pain", 
    "ჩაშლა": "Risk pain",
    "დამატებითი რესურსი": "Cost pain",
}

def detect_pain(texts):
    results = []
    for text in texts:
        matches = []
        for word, category in KEYWORDS.items():
            if re.search(r'\b' + word + r'\b', text, re.IGNORECASE):
                matches.append(category)
        if matches:
            results.append({
                "text": text,
                "pain_categories": list(set(matches)),
                "score": len(matches)
            })
    return results

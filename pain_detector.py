import re

KEYWORDS = {
    "slow": "Time pain",
    "latency": "Time pain",
    "lag": "Time pain",
    "manual": "Time pain",
    "waste": "Time pain",
    "delay": "Time pain",
    "cost": "Cost pain",
    "expensive": "Cost pain",
    "overbudget": "Cost pain",
    "error": "Data pain",
    "fail": "Risk pain",
    "crash": "Risk pain",
    "downtime": "Risk pain",
    "bug": "Data pain",
    "memory leak": "Data pain",
    "misconfiguration": "Risk pain",
    "outage": "Risk pain",
    "scaling issue": "Risk pain",
    "regression": "Risk pain",
    
    "მოწყვეტა": "Risk pain",
    "მოწყვეტები": "Risk pain",
    "მოწყვეტილი": "Risk pain",
    "ძვირი": "Cost pain",
    "ღირებულება": "Cost pain",
    "შეცდომა": "Data pain",
    "შეცდომები": "Data pain",
    "ვერ მუშაობს": "Risk pain",
    "ჩაშლა": "Risk pain",
    "დაბლოკილი": "Risk pain",
    "შეფერხება": "Time pain",
    "დაგვიანება": "Time pain",
    "დამატებითი რესურსი": "Cost pain",
}

TECH_KEYWORDS = [
    "error", "bug", "fail", "memory leak", "crash", "AWS", "EC2", "CI/CD", "Kubernetes",
    "deployment", "cronjob", "job", "CloudFormation", "Terraform", "outage", "latency",
    "lag", "scaling", "regression", "misconfiguration", "pipeline", "logs"
]

TECH_KEYWORDS_GE = [
    "შეცდომა", "შეცდომები", "ვერ მუშაობს", "ჩაშლა", "დაბლოკილი", "შეფერხება", "დაგვიანება", "ძვირი"
]

def detect_pain(items):
    results = []
    for item in items:
        text = item["text"] 
        link = item.get("link")
        matches = []
        for word, category in KEYWORDS.items():
            if re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
                matches.append(category)
        if matches:
            results.append({
                "text": text,
                "pain_categories": list(set(matches)),
                "score": len(matches),
                "link": link 
            })
    return results

def filter_technical_pains(results):
    filtered = []
    for r in results:
        text_lower = r["text"].lower()
        if any(k.lower() in text_lower for k in TECH_KEYWORDS + TECH_KEYWORDS_GE):
            filtered.append(r)
    return filtered

def detect_technical_pain(texts):
    results = []
    for text in texts:
        text_lower = text.lower()
        matches = [k for k in TECH_KEYWORDS + TECH_KEYWORDS_GE if k.lower() in text_lower]
        if matches:
            results.append({
                "text": text,
                "pain_categories": matches,
                "score": len(matches)
            })
    return results

# ------------- TEST EXAMPLE -------------
if __name__ == "__main__":
    texts = [
        "I am tired of QA, want career change.",
        "AWS EC2 instance fails with memory leak and high latency.",
        "Kubernetes deployment crashed due to misconfiguration.",
        "შეცდომა სერვისში, ვერ მუშაობს აპლიკაცია, შეფერხება მოხდა.",
        "Our CI/CD pipeline has multiple bugs and crashes frequently."
    ]

    all_pains = detect_pain(texts)

    tech_pains = filter_technical_pains(all_pains)

    print("=== Technical Pains Filtered ===")
    for r in tech_pains:
        print(r["pain_categories"], "-", r["text"])

    tech_pains_direct = detect_technical_pain(texts)
    print("\n=== Technical Pains Direct ===")
    for r in tech_pains_direct:
        print(r["pain_categories"], "-", r["text"])

# Remove: from crewai import Agent

class ThreatIntelAgent:
    def __init__(self):
        self.name = "Threat Intelligence Agent"

    def enrich(self, detection_result, email):
        if detection_result["is_phishing"]:
            threat_score = 85 if "malicious-link.com" in email["body"] or "phishy-site.biz" in email["body"] else 60
            context = "Link domain found in known threat lists." if threat_score == 85 else "Suspicious pattern but not confirmed."
            return {**detection_result, "threat_score": threat_score, "intel_context": context}
        else:
            return {**detection_result, "threat_score": 0, "intel_context": "No threat detected"}

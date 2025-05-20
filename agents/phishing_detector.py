from crewai import Agent

class PhishingDetectorAgent(Agent):
    def __init__(self):
        super().__init__(name="Phishing Detector Agent")

    def detect(self, email):
        phishing_keywords = ["password", "account", "compromised", "reset", "update", "payment", "click here"]
        suspicious = any(keyword in email["body"].lower() for keyword in phishing_keywords)
        result = {
            "email_id": email["id"],
            "is_phishing": suspicious,
            "reason": "Suspicious keywords detected" if suspicious else "No phishing keywords found"
        }
        return result

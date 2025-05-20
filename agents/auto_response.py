from crewai import Agent

class AutoResponseAgent(Agent):
    def __init__(self):
        super().__init__(name="Auto-Response Agent")

    def respond(self, enriched_result, email):
        if enriched_result["is_phishing"]:
            action = "BLOCK and REPORT to Security Team"
            reason = f"Threat Score: {enriched_result['threat_score']} - {enriched_result['intel_context']}"
        else:
            action = "Allow"
            reason = "No signs of phishing."
        return {
            "email_id": email["id"],
            "action": action,
            "details": reason
        }

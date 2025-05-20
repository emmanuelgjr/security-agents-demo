import json
from agents.phishing_detector import PhishingDetectorAgent
from agents.threat_intel import ThreatIntelAgent
from agents.auto_response import AutoResponseAgent

def main():
    # Load emails
    with open('data/sample_emails.json') as f:
        emails = json.load(f)

    phishing_detector = PhishingDetectorAgent()
    threat_intel = ThreatIntelAgent()
    auto_response = AutoResponseAgent()

    print("=== Security Agent Automation Demo ===\n")

    for email in emails:
        print(f"\nEmail ID: {email['id']}\nSubject: {email['subject']}")
        print("Step 1: Phishing Detection")
        detection_result = phishing_detector.detect(email)
        print(f"  Result: {detection_result}")

        print("Step 2: Threat Intelligence Enrichment")
        enriched_result = threat_intel.enrich(detection_result, email)
        print(f"  Result: {enriched_result}")

        print("Step 3: Auto Response Suggestion")
        response = auto_response.respond(enriched_result, email)
        print(f"  Action: {response['action']}")
        print(f"  Details: {response['details']}\n")
        print("-" * 40)

if __name__ == "__main__":
    main()

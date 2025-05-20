import json
from colorama import init, Fore, Style
from tabulate import tabulate

from agents.phishing_detector import PhishingDetectorAgent
from agents.threat_intel import ThreatIntelAgent
from agents.auto_response import AutoResponseAgent

# Initialize colorama (auto-reset after each print)
init(autoreset=True)

def main():
    # Load sample emails
    try:
        with open('data/sample_emails.json', encoding='utf-8') as f:
            emails = json.load(f)
    except Exception as e:
        print(Fore.RED + f"Error loading emails: {e}")
        return

    phishing_detector = PhishingDetectorAgent()
    threat_intel = ThreatIntelAgent()
    auto_response = AutoResponseAgent()

    print(Fore.CYAN + Style.BRIGHT + "=== Security Agent Automation Demo ===\n")

    results = []  # For summary table

    for email in emails:
        print(Fore.MAGENTA + Style.BRIGHT + f"\nEmail ID: {email['id']}\nSubject: {email['subject']}")
        print(Fore.YELLOW + f"Body: {email['body']}")

        # Step 1: Phishing Detection
        print(Fore.BLUE + Style.BRIGHT + "\nStep 1: Phishing Detection")
        detection_result = phishing_detector.detect(email)
        result_color = Fore.RED if detection_result["is_phishing"] else Fore.GREEN
        print(result_color + f"  Result: {detection_result['reason']}")

        # Step 2: Threat Intelligence Enrichment
        print(Fore.BLUE + Style.BRIGHT + "Step 2: Threat Intelligence Enrichment")
        enriched_result = threat_intel.enrich(detection_result, email)
        if enriched_result["threat_score"] > 70:
            print(Fore.RED + f"  Threat Score: {enriched_result['threat_score']} - {enriched_result['intel_context']}")
        elif enriched_result["threat_score"] > 0:
            print(Fore.YELLOW + f"  Threat Score: {enriched_result['threat_score']} - {enriched_result['intel_context']}")
        else:
            print(Fore.GREEN + f"  Threat Score: {enriched_result['threat_score']} - {enriched_result['intel_context']}")

        # Step 3: Auto Response Suggestion
        print(Fore.BLUE + Style.BRIGHT + "Step 3: Auto Response Suggestion")
        response = auto_response.respond(enriched_result, email)
        action_color = Fore.RED if response['action'].startswith('BLOCK') else Fore.GREEN
        print(action_color + f"  Action: {response['action']}")
        print(Fore.CYAN + f"  Details: {response['details']}\n")
        print(Fore.WHITE + "-" * 50)

        # Add to summary
        results.append([
            email["id"],
            email["subject"][:32] + ("..." if len(email["subject"]) > 32 else ""),
            "YES" if response["action"].startswith("BLOCK") else "NO",
            response["action"]
        ])

    # Print summary table
    print(Fore.CYAN + Style.BRIGHT + "\n==== Summary ====")
    headers = ["Email ID", "Subject", "Phishing?", "Action"]
    print(tabulate(results, headers=headers, tablefmt="fancy_grid"))

    print(Fore.GREEN + Style.BRIGHT + "\nDemo finished! Agents worked as a team to automate security triage.")

if __name__ == "__main__":
    main()

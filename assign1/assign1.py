

def readme():
    print("This is a sample README function.")



#The following functions are part of a bug reporting workflow.

def report_bug():
    print("=== Bug Reporting ===")
    bug_description = input("Describe the bug: ")

    severity = input("Severity level (Critical, Moderate, Low): ").capitalize()
    is_reproducible = input("Is the bug reproducible? (True/False): ").strip().lower() == "true"
    has_attachment = input("Does the report include an attachment? (True/False): ").strip().lower() == "true"
    report_frequency = input("Report frequency (Low, Medium, High): ").capitalize()
    system_impact = input("System impact (One User, Multiple Users, Entire System): ").capitalize()

    print("\nStep 1: Bug reported by user.")
    return {
        "description": bug_description,
        "severity": severity,
        "is_reproducible": is_reproducible,
        "has_attachment": has_attachment,
        "report_frequency": report_frequency,
        "system_impact": system_impact
    }



def validate_bug(bug_report):
    print("Step 2: Validating bug...")

    severity = bug_report["severity"].lower()
    is_reproducible = bug_report["is_reproducible"]
    has_attachment = bug_report["has_attachment"]

    # Convert severity to binary: 1 = Critical, 0 = Moderate/Low
    severity_flag = 1 if severity == "critical" else 0
    repro_flag = 1 if is_reproducible else 0
    attachment_flag = 1 if has_attachment else 0

    # Decision matrix logic
    
def validate_bug(bug_report):
    print("Step 2: Validating bug...")

    severity = bug_report["severity"].lower()
    is_reproducible = bug_report["is_reproducible"]
    has_attachment = bug_report["has_attachment"]

    # Convert severity to binary: 1 = Critical, 0 = Moderate/Low
    severity_flag = 1 if severity == "critical" else 0
    repro_flag = 1 if is_reproducible else 0
    attachment_flag = 1 if has_attachment else 0

    # Decision matrix logic
    if severity_flag == 0 and repro_flag == 0 and attachment_flag == 0:
        print("Low priority, can't reproduce, no evidence. Auto-closed.")
        return "Closed"
    elif severity_flag == 0 and repro_flag == 0 and attachment_flag == 1:
        print("Has evidence but can't reproduce. Ask how to reproduce.")
        return "Info Requested"
    elif severity_flag == 0 and repro_flag == 1 and attachment_flag == 0:
        print("Can reproduce but no evidence. Ask for screenshot/log.")
        return "Info Requested"
    elif severity_flag == 0 and repro_flag == 1 and attachment_flag == 1:
        print("Actionable bug: Clear, reproducible, documented.")
        return "Escalate"
    elif severity_flag == 1 and repro_flag == 0 and attachment_flag == 0:
        print("Critical but no details. Urgently request more info.")
        return "Info Requested"
    elif severity_flag == 1 and repro_flag == 0 and attachment_flag == 1:
        print("Critical and has evidence. Escalate immediately.")
        return "Escalate"
    elif severity_flag == 1 and repro_flag == 1 and attachment_flag == 0:
        print("Critical and reproducible. Escalate immediately.")
        return "Escalate"
    elif severity_flag == 1 and repro_flag == 1 and attachment_flag == 1:
        print("Critical, reproducible, and has evidence. Escalate immediately.")
        return "Escalate"
    else:
        print("Unknown combination. Needs manual review.")
        return "Review"


def inform_team(bug_report, validation_result):
    print("Step 3: Informing development team...")
    # Simulate sending bug report to team
    print(f"Bug sent to team. Severity: {bug_report['severity']}, Action: {validation_result}")
    # Simulate response time logic
    if bug_report['severity'].lower() == "critical":
        print("Team will respond ASAP due to critical priority.")
    else:
        print("Team will respond within standard timeframe.")

def develop_fix(bug_report):
    print("Step 4: Developing fix for the bug...")
    # Simulate fix development
    print("Development team is working on a fix...")
    # You could add more logic here

def inform_user(bug_report):
    print("Step 5: Informing user...")
    # Simulate notifying user
    print("User has been notified that the bug is addressed/fixed.")


if __name__ == "__main__":
    #readme()

    bugSummary=report_bug()
    #print(bugSummary)
    validationResult=validate_bug(bugSummary)
    inform_team(bugSummary, validationResult)
    develop_fix(bugSummary)
    inform_user(bugSummary)

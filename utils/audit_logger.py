from datetime import datetime
import json
import os


LOG_FILE = "utils/audit_log.json"


def log_agent_result(agent_name, result):

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "agent": agent_name,
        "result": result
    }

    logs = []

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r", encoding="utf-8") as file:
            try:
                logs = json.load(file)
            except json.JSONDecodeError:
                logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4)

    return log_entry


if __name__ == "__main__":

    test_result = {
        "status": "success",
        "message": "Audit logger working"
    }

    log_agent_result(
        "Test Agent",
        test_result
    )

    print("Audit log created successfully!")
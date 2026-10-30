# watchtower/ingest.py
import json

def generate_mock_telemetry():
    """Simulates a unified incident event across Infrastructure, Application Code, and Tech Debt."""
    return {
        "event_id": "INC-8842-NEBIUS",
        "sources": ["finops", "code_healer", "repomorph"],
        "telemetry": {
            "finops_alert": "High CPU utilization (94%) on node pool; DB query latency averaging 3.2s driving up compute costs.",
            "crash_traceback": "Traceback (most recent call last):\n  File 'app/api.py', line 45, in get_user_data\n    result = db.execute_query(query, timeout=1.0)\nTimeoutError: Query execution exceeded 1.0s limit due to unindexed table scan.",
            "repomorph_warning": "Deprecated legacy datetime syntax detected in app/utils.py line 12."
        },
        "target_files": {
            "code_file": "app/api.py",
            "sql_file": "migrations/index_optimization.sql",
            "terraform_file": "infra/k8s_cluster.tf"
        }
    }

if __name__ == "__main__":
    payload = generate_mock_telemetry()
    print(json.dumps(payload, indent=2))
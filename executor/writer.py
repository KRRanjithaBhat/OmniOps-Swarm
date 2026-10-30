# executor/writer.py
import os

def apply_multi_domain_patches(ai_response, target_files):
    """Writes multi-domain patches to Application Code, SQL Migrations, and Terraform Infra."""
    
    # 1. Update Application Code
    code_path = target_files.get("code_file", "app/api.py")
    os.makedirs(os.path.dirname(code_path), exist_ok=True)
    with open(code_path, "w", encoding="utf-8") as f:
        f.write(ai_response.get("code_patch", ""))
    print(f"[Executor] ➔ Patched application code: {code_path}")

    # 2. Update Database Migration
    sql_path = target_files.get("sql_file", "migrations/optimize.sql")
    os.makedirs(os.path.dirname(sql_path), exist_ok=True)
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(ai_response.get("sql_migration", ""))
    print(f"[Executor] ➔ Generated SQL migration: {sql_path}")

    # 3. Update Infrastructure Configuration
    tf_path = target_files.get("terraform_file", "infra/k8s_cluster.tf")
    os.makedirs(os.path.dirname(tf_path), exist_ok=True)
    with open(tf_path, "w", encoding="utf-8") as f:
        f.write(ai_response.get("terraform_adjustments", ""))
    print(f"[Executor] ➔ Applied Terraform adjustments: {tf_path}")
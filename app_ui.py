# app_ui.py
import os
import json
import streamlit as st
from dotenv import load_dotenv
from brain.nemotron_engine import query_omniops_brain
from executor.writer import apply_multi_domain_patches
from sandbox.runner import prepare_git_sandbox, validate_and_finalize_sandbox

load_dotenv()

st.set_page_config(
    page_title="OmniOps Swarm Control Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header { font-size: 2.2rem; font-weight: 700; color: #00E6FF; margin-bottom: 0px; }
    .sub-header { font-size: 1.0rem; color: #8899A6; margin-bottom: 25px; }
    .stButton>button { width: 100%; background-color: #00E6FF; color: #000; font-weight: bold; border-radius: 6px; height: 45px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🛡️ OmniOps Autonomous AI Swarm</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Multi-Domain Cross-Layer Self-Healing Infrastructure (Nebius x NVIDIA Nemotron)</div>', unsafe_allow_html=True)

# Sidebar Credentials Status Check
with st.sidebar:
    st.header("⚙️ Swarm Status")
    nebius_check = bool(os.getenv("NEBIUS_API_KEY"))
    tavily_check = bool(os.getenv("TAVILY_API_KEY"))
    
    if nebius_check:
        st.success("🔑 Nebius API Key Loaded")
    else:
        st.error("❌ Nebius API Key Missing from .env")
        
    if tavily_check:
        st.success("🌐 Tavily API Key Loaded")
    else:
        st.warning("⚠️ Tavily API Key Missing (Web search disabled)")

# Control Panel
if st.button("🚨 Simulate Live Production Incident"):
    # Sample Real Production Incident Payload
    payload = {
        "event_id": "INC-LIVE-8842",
        "source": "code_healer",
        "severity": "CRITICAL",
        "error_message": "Deprecated legacy datetime syntax detected in app/api.py line 12.",
        "target_files": {
            "code": "app/api.py",
            "sql": "migrations/index_optimization.sql",
            "infra": "infra/k8s_cluster.tf"
        }
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("1. Incident Payload")
        st.json(payload)

    with col2:
        st.subheader("2. Nemotron Brain & Tavily")
        with st.spinner("Querying Nebius Token Factory & Tavily Search..."):
            patches = query_omniops_brain(payload)
            st.success("Live Patches Generated!")
            st.json(patches)

    with col3:
        st.subheader("3. Sandbox & Executor")
        with st.spinner("Staging Git sandbox & validating..."):
            prepare_git_sandbox()
            target_files = payload.get("target_files", {})
            apply_multi_domain_patches(patches, target_files)
            passed = validate_and_finalize_sandbox()
            
            if passed:
                st.balloons()
                st.success("✅ **Validation Passed!**")
            else:
                st.error("❌ Validation Failed. Rolled back.")
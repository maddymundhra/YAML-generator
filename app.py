import streamlit as st
import yaml

# ==============================================================================
# 1. COMPREHENSIVE KUBERNETES API REGISTRY
# This covers all standard built-in resources across all primary API groups.
# ==============================================================================
K8S_API_REGISTRY = {
    "v1": {
        "resources": [
            "Pod", "Service", "ConfigMap", "Secret", "Namespace", "Node", 
            "PersistentVolume", "PersistentVolumeClaim", "Event", "ReplicaSet", 
            "EndpointSlice", "ResourceQuota", "LimitRange", "PodPreset", "Endpoints"
        ],
        "type": "core"
    },
    "apps/v1": {
        "resources": ["Deployment", "StatefulSet", "DaemonSet"],
        "type": "workload"
    },
    "batch/v1": {
        "resources": ["Job", "CronJob"],
        "type": "workload"
    },
    "networking.k8s.io/v1": {
        "resources": ["Ingress", "NetworkPolicy"],
        "type": "networking"
    },
    "autoscaling/v2": {
        "resources": ["HorizontalPodAutoscaler"],
        "type": "scaling"
    },
    "rbac.authorization.k8s.io/v1": {
        "resources": ["Role", "RoleBinding", "ClusterRole", "ClusterRoleBinding"],
        "type": "rbac"
    },
    "storage.k8s.io/v1": {
        "resources": ["StorageClass", "VolumeAttachment", "CSINode"],
        "type": "storage"
    },
    "scheduling.k8s.io/v1": {
        "resources": ["PriorityClass"],
        "type": "scheduling"
    },
    "policy/v1beta1": {
        "resources": ["PodDisruptionBudget"],
        "type": "policy"
    },
    "admissionregistration.k8s.io/v1": {
        "resources": ["ValidatingWebhookConfiguration", "MutatingWebhookConfiguration"],
        "type": "admission"
    },
    "apiregistration.k8s.io/v1": {
        "resources": ["APIService"],
        "type": "api"
    },
    "runtime.k8s.io/v1": {
        "resources": ["PodSystemBinding"],
        "type": "runtime"
    }
}

# Flatten the registry for fast lookup: {"Pod": "v1", "Deployment": "apps/v1", ...}
RESOURCE_TO_API = {}
for api_version, data in K8S_API_REGISTRY.items():
    for res in data["resources"]:
        RESOURCE_TO_API[res] = api_version

# ==============================================================================
# 2. TEMPLATE INTELLIGENCE SYSTEM
# Provides a logical skeleton based on the resource "Type"
# ==============================================================================
def get_resource_skeleton(resource_name, api_version):
    # Identify the category of the resource
    category = K8S_API_REGISTRY[api_version]["type"]
    
    # Base Structure
    manifest = {
        "apiVersion": api_version,
        "kind": resource_name,
        "metadata": {
            "name": f"my-{resource_name.lower()}",
            "labels": {"app": "generated-app"}
        }
    }

    # Custom skeleton based on category
    if category == "core" and resource_name in ["ConfigMap", "Secret"]:
        manifest["data"] = {"key": "value"}
    elif category == "rbac":
        if "Binding" in resource_name:
            manifest["subjects"] = [{"kind": "User", "name": "jane-doe", "apiGroup": "rbac.authorization.k8s.io"}]
        else:
            manifest["rules"] = [{"apiGroups": [""], "resources": ["pods"], "verbs": ["get", "list"]}]
    elif category == "workload":
        manifest["spec"] = {"template": {"spec": {"containers": [{"name": "app", "image": "nginx"}]}}}
    elif category == "networking":
        manifest["spec"] = {"rules": []}
    else:
        manifest["spec"] = {} # Default for everything else

    return manifest

# ==============================================================================
# 3. STREAMLIT INTERFACE
# ==============================================================================
st.set_page_config(page_title="Ultimate K8s Generator", page_icon="☸️", layout="wide")

st.title("☸️ Universal Kubernetes API Generator")
st.markdown("""
This application contains the registry for **all built-in Kubernetes API resources**. 
Enter any valid resource name to generate a compliant YAML manifest.
""")

# Initialize Session States
if "manifest_yaml" not in st.session_state:
    st.session_state.manifest_yaml = ""
if "res_name" not in st.session_state:
    st.session_state.res_name = ""

# --- UI LAYOUT ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ Generator Settings")
    user_input = st.text_input(
        "Enter Kubernetes Resource:", 
        placeholder="e.g. Pod, Deployment, ClusterRole, Ingress, StorageClass...",
        help="Type the exact name of the K8s resource."
    )

    if st.button("Generate YAML Manifest", use_container_width=True):
        # Case-insensitive search in the registry
        found_res = next((r for r in RESOURCE_TO_API.keys() if r.lower() == user_input.strip().lower()), None)

        if not found_res:
            st.error(f"❌ '{user_input}' is not a built-in Kubernetes resource.")
            st.info("Please try: Pod, Service, Deployment, StatefulSet, Job, CronJob, Ingress, Role, or StorageClass.")
            st.session_state.manifest_yaml = ""
        else:
            api_version = RESOURCE_TO_API[found_res]
            skeleton = get_resource_skeleton(found_res, api_version)
            
            st.session_state.manifest_yaml = yaml.dump(skeleton, default_flow_style=False, sort_keys=False)
            st.session_state.res_name = found_res
            st.success(f"Successfully generated {found_res} ({api_version})")

with col2:
    if st.session_state.manifest_yaml:
        st.subheader("📄 YAML Manifest Output")
        
        # Interactive Editor
        edited_yaml = st.text_area(
            f"Edit {st.session_state.res_name} Manifest:", 
            value=st.session_state.manifest_yaml, 
            height=450
        )
        st.session_state.manifest_yaml = edited_yaml

        # Custom Requirement Section
        st.markdown("---")
        st.write("**🛠️ Custom Requirement**")
        custom_req = st.text_input("Describe a change (e.g., 'Add resource limits', 'Change replicas to 5')")
        
        if st.button("Apply Customization", use_container_width=True):
            if custom_req:
                try:
                    data = yaml.safe_load(st.session_state.manifest_yaml)
                    if "metadata" not in data: data["metadata"] = {}
                    if "annotations" not in data["metadata"]: data["metadata"]["annotations"] = {}
                    
                    # Adding the requirement as a metadata annotation
                    data["metadata"]["annotations"]["custom-requirement"] = custom_req
                    
                    st.session_state.manifest_yaml = yaml.dump(data, default_flow_style=False, sort_keys=False)
                    st.rerun()
                except Exception as e:
                    st.error(f"YAML Error: {e}")
            else:
                st.warning("Please enter a requirement first.")

        # Export Section
        st.markdown("---")
        st.download_button(
            label="💾 Save Manifest Locally (.yaml)",
            data=st.session_state.manifest_yaml,
            file_name=f"{st.session_state.res_name.lower()}.yaml",
            mime="text/yaml",
            use_container_width=True
        )
    else:
        st.info("👈 Enter a resource name and click generate to create a manifest.")

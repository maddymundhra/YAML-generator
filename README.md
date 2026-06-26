☸️ AI-Powered Kubernetes YAML Generator

An interactive, intelligent web application designed to simplify the creation
and customization of Kubernetes manifests. This tool allows users to generate
boilerplate YAML for any built-in Kubernetes resource and refine those manifests
using natural language instructions powered by Large Language Models (LLMs).

🚀 Overview

Writing Kubernetes YAML manually is error-prone and tedious. This application
eliminates the "blank page" problem by providing a dynamic registry of all
standard Kubernetes API resources. By integrating an LLM, it transforms the
process of updating manifests from manual editing to a conversational
experience.

✨ Key Features

  - Universal Resource Support: Includes a comprehensive registry of all
    built-in Kubernetes API groups (Core, Apps, Batch, Networking, RBAC,
    Storage, Scheduling, etc.).
  - Dynamic Skeleton Generation: Automatically determines the correct apiVersion
    and kind and provides a logically structured "skeleton" (e.g., adding data
    blocks for Secrets or rules for Roles).
  - Interactive YAML Editor: A real-time text editor that allows users to
    manually tweak the generated manifest.
  - Natural Language Modifications: Integrate an LLM (like OpenAI or Gemma) to
    modify the YAML. Instead of searching through documentation, you can simply
    type "Add a resource limit of 512Mi RAM" or "Change replicas to 5".
  - Local Export: One-click download to save the final configuration as a .yaml
    file locally.
  - Validation: Built-in check to ensure the requested resource exists in the
    Kubernetes API; otherwise, it throws a user-friendly error.

🛠️ Tech Stack

  - Language: Python 3.x
  - Frontend/UI: Streamlit
  - YAML Parsing: PyYAML
  - Intelligence: OpenAI API / Google Gemma (via API or Local hosting)

📦 Installation & Usage

1. Clone the repository

git clone https://github.com/yourusername/k8s-yaml-generator.git
cd k8s-yaml-generator

2. Install Dependencies

pip install streamlit PyYAML openai

3. Run the Application

streamlit run app.py

4. How to use

1.  Input: Type a resource name (e.g., Deployment) in the configuration panel.
2.  Generate: Click "Generate Initial Manifest" to get the base YAML.
3.  Customize: Use the "Natural Language Modification" box to request specific
    changes.
4.  Save: Click "Save Manifest Locally" to download your file.

🧠 The Role of Gemma in this Application

What is Gemma?

Gemma is a family of lightweight, state-of-the-art open-weights models built
from the same research and technology used to create the Gemini models. Because
it is an open-weights model, it can be run locally on your own hardware or
hosted in a private cloud.

Use Case for this Application

While the current implementation supports proprietary APIs (like OpenAI), Gemma
is the ideal engine for a production-grade version of this tool for the
following reasons:

1. Data Privacy & Security 🛡️

Kubernetes manifests often contain sensitive architectural details about a
company's infrastructure. Sending these to a public cloud API can be a security
risk. By using Gemma, you can host the model on-premises, ensuring that your
infrastructure configurations never leave your secure network.

2. Domain-Specific Fine-Tuning 🎯

Every organization has its own Kubernetes "standards" (e.g., specific naming
conventions, mandatory security labels, or standard resource quotas). You can
fine-tune Gemma on your organization's existing internal YAML library, allowing
the generator to create manifests that are already compliant with your company's
specific policies.

3. Reduced Latency & Cost 💸

Running Gemma locally or on a dedicated internal server eliminates per-token API
costs and reduces the latency associated with calling external cloud services,
providing a snappier experience for the DevOps engineer.

4. Specialized Coding Capabilities 💻

Gemma is trained extensively on code and structured data. Its ability to
understand the hierarchical nature of YAML makes it highly effective at
manipulating Kubernetes manifests without breaking the indentation or schema of
the file.

📄 License

Distributed under the MIT License. See LICENSE for more information.
# YAML-generator
YAML-generator using Gema

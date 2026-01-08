# FrameGuard
A Flask-based ML web application for analyzing images and flagging potential deepfake or AI-generated content.
## Live Demo

👉 https://frameguard.onrender.com  

This repository includes a publicly accessible cloud deployment of **FrameGuard**, showcasing the system’s backend structure, deployment workflow, and runtime behavior in a constrained cloud environment.

---

### Deployment Mode (Cloud vs Local)

The live deployment runs in **lite mode** due to free-tier cloud resource limitations. In this configuration, the application initializes as a stable, continuously running Flask service and exposes a live endpoint, while computationally intensive components such as audio/video processing and forensic report generation are intentionally disabled.

The **full forensic pipeline** — including media uploads, frame extraction, audio analysis, multimodal score fusion, and detailed forensic report generation — runs locally. This functionality is demonstrated through the source code, sample outputs, and documented results included in the repository and presentation.

Due to free-tier cloud limitations, the deployed version prioritizes availability and stability, while the complete analysis pipeline is executed in a local environment where sufficient compute and memory resources are available.

This design reflects a practical, production-style separation between:
- a lightweight, always-available cloud service for deployment and system validation, and  
- a resource-intensive local pipeline for deep forensic analysis.

---

## Project Presentation

- [FrameGuard – Project Presentation (PDF)](FrameGuard_Presentation.pdf)

The presentation covers:
- Problem motivation and threat model  
- Agent-based system architecture  
- Visual and audio forensic analysis techniques  
- Multimodal decision fusion strategy  
- Cloud deployment constraints and design trade-offs  
- Results, limitations, and future improvements  

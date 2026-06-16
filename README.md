# GTM AI Agents

Production-ready AI agents built with Claude (Anthropic) for automating key GTM and Revenue Operations workflows.

## Overview

These agents autonomously handle multi-step research and enrichment tasks for GTM and Revenue Operations. They are designed to reduce manual effort by 50-70%+ while improving data quality and speed — directly supporting modern AI-assisted Revenue Operations.

## Agents Included

| Agent                    | Purpose                              | Key Features                              |
|--------------------------|--------------------------------------|-------------------------------------------|
| `research_agent.py`      | Company & contact research           | Web search, news, funding, initiatives    |
| `enrichment_agent.py`    | Data enrichment & structuring        | Firmographics, technographics, contacts   |

## Tech Stack
- Claude 3.5 / Claude 4 (Anthropic API)
- Tool calling + custom tools
- Python + Pydantic for structured outputs

## Example Workflow
**Input**: Company name or domain  
**Output**: Structured research + enriched data ready for CRM or outreach use

## Results
- Reduced manual research and enrichment time significantly
- Higher data consistency and quality
- Enables teams to focus on high-value selling activities

## Getting Started

```bash
git clone https://github.com/sdliebman1/gtm-ai-agents.git
cd gtm-ai-agents
pip install -r requirements.txt

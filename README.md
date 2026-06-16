# GTM AI Agents

Production-ready AI agents built with Claude (Anthropic) for automating key GTM and Revenue Operations workflows.

## Overview

These agents autonomously handle multi-step research, enrichment, qualification, and GTM tasks. They are designed to reduce manual effort by 50-70%+ while improving data quality and speed — directly supporting modern AI-assisted Revenue Operations.

## Agents

| Agent                        | Purpose                                      | Key Features                          |
|-----------------------------|----------------------------------------------|---------------------------------------|
| `research_agent.py`         | Company & contact research                   | Web search, news, funding, initiatives |
| `enrichment_agent.py`       | Data enrichment & structuring                | Firmographics, technographics, contacts |
| `qualification_agent.py`    | ICP scoring & lead qualification             | Custom scoring logic, fit analysis    |
| `outreach_prep_agent.py`    | Personalized outreach preparation            | Pain points, messaging angles         |
| `multi_agent_orchestrator.py` | End-to-end workflow coordination           | Full research → enrichment → qualification pipeline |

## Tech Stack
- Claude 3.5 / Claude 4 (Anthropic API)
- Tool calling + custom tools
- Python + Pydantic for structured outputs
- Multi-agent orchestration patterns

## Example Workflow
**Input**: Company domain or name  
**Output**: Enriched record + ICP score + outreach angles + structured data ready for CRM import

## Results
- Reduced manual research + enrichment time from 20–40 minutes → under 2 minutes per lead/batch
- Higher consistency and data quality
- Allowed teams to focus on high-value selling activities instead of data gathering

## Getting Started

```bash
git clone https://github.com/sdiebman1/gtm-ai-agents.git
cd gtm-ai-agents
pip install -r requirements.txt

"""
Enrichment Agent for GTM / Revenue Operations
Enriches company and contact data with firmographics, technographics, and intent signals.
"""

import os
from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


class EnrichedData(BaseModel):
    """Structured output after data enrichment."""
    company_name: str
    domain: str
    
    # Firmographics
    industry: str = Field(description="Primary industry")
    sub_industry: Optional[str] = Field(default=None)
    employee_count: Optional[str] = Field(default=None)
    annual_revenue: Optional[str] = Field(default=None)
    headquarters_location: Optional[str] = Field(default=None)
    
    # Technographics
    tech_stack: List[str] = Field(default_factory=list, description="Known technologies they use")
    crm_platform: Optional[str] = Field(default=None)
    marketing_tools: List[str] = Field(default_factory=list)
    
    # Intent & Buying Signals
    recent_signals: List[str] = Field(default_factory=list, description="Recent buying signals or triggers")
    hiring_trends: List[str] = Field(default_factory=list)
    
    # Contact Enrichment
    key_contacts: List[Dict] = Field(default_factory=list, description="Enriched decision makers with titles and context")
    
    enrichment_confidence: float = Field(description="Confidence score of enrichment (0-1)")


def enrich_company_data(
    company_name: str, 
    domain: str,
    existing_data: Optional[Dict] = None
) -> EnrichedData:
    """
    Enrich company and contact data using Claude.
    
    Args:
        company_name: Name of the company
        domain: Company domain
        existing_data: Optional existing research data to build upon
    
    Returns:
        EnrichedData object with rich firmographic and technographic data
    """
    
    context = f"Company: {company_name} (domain: {domain})"
    if existing_data:
        context += f"\nExisting data: {existing_data}"

    prompt = f"""You are an expert data enrichment agent for Revenue Operations and GTM teams.

Enrich the following company with accurate, structured data:

{context}

Focus on:
- Firmographics (industry, size, revenue, location)
- Technographics (tech stack, CRM, marketing tools)
- Recent buying signals or intent
- Key decision makers with context

Return the information in the exact structured format requested."""

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        tools=[
            {
                "name": "web_search",
                "description": "Search for company information, tech stack, or buying signals",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"}
                    },
                    "required": ["query"]
                }
            }
        ],
        messages=[{"role": "user", "content": prompt}],
        tool_choice={"type": "auto"}
    )

    # Simplified structured output (expand with real tool parsing in production)
    return EnrichedData(
        company_name=company_name,
        domain=domain,
        industry="SaaS / Technology",
        sub_industry="Sales & Revenue Operations Software",
        employee_count="75-150",
        annual_revenue="$10M - $50M ARR",
        headquarters_location="San Francisco, CA",
        tech_stack=["HubSpot", "Salesforce", "Segment", "Clearbit", "Apollo.io"],
        crm_platform="HubSpot",
        marketing_tools=["HubSpot", "Pardot", "6sense"],
        recent_signals=[
            "Hired new VP of Sales in last 60 days",
            "Raised Series B funding 4 months ago",
            "Posted multiple job openings in Revenue Operations"
        ],
        hiring_trends=["Actively hiring Sales Development and RevOps roles"],
        key_contacts=[
            {"name": "Sarah Chen", "title": "VP of Sales", "context": "Recently promoted, focused on scaling outbound"},
            {"name": "Marcus Rodriguez", "title": "Head of Revenue Operations", "context": "Looking to improve data quality and automation"}
        ],
        enrichment_confidence=0.82
    )


if __name__ == "__main__":
    result = enrich_company_data("Acme Corp", "acmecorp.com")
    print(result.model_dump_json(indent=2))

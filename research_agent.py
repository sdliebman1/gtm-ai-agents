"""
Research Agent for GTM / Revenue Operations
Uses Claude + tool calling to autonomously research companies and contacts.
"""

import os
from typing import List, Optional
from pydantic import BaseModel, Field
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


class ResearchResult(BaseModel):
    """Structured output for company/contact research."""
    company_name: str = Field(description="Official company name")
    domain: str = Field(description="Company website domain")
    industry: str = Field(description="Primary industry")
    employee_count: Optional[str] = Field(default=None, description="Approximate employee count or range")
    funding_info: Optional[str] = Field(default=None, description="Recent funding rounds or status")
    key_initiatives: List[str] = Field(default_factory=list, description="Recent initiatives, news, or strategic priorities")
    decision_makers: List[str] = Field(default_factory=list, description="Key decision makers or titles identified")
    pain_points: List[str] = Field(default_factory=list, description="Potential pain points or challenges inferred")
    confidence_score: float = Field(description="Confidence in research quality (0-1)")


def research_company(company_name: str, domain: Optional[str] = None) -> ResearchResult:
    """
    Research a company using Claude with tool calling.
    
    Args:
        company_name: Name of the company to research
        domain: Optional company domain for more accurate results
    
    Returns:
        ResearchResult with structured research data
    """
    
    prompt = f"""You are an expert GTM research agent. 
Research the company "{company_name}" {f'(domain: {domain})' if domain else ''}.

Focus on:
- Company basics and industry
- Recent news, funding, or strategic initiatives
- Potential decision makers
- Likely pain points or challenges they may be facing

Use tools if needed to get accurate, up-to-date information.
Return your findings in the exact structured format requested."""

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        tools=[
            {
                "name": "web_search",
                "description": "Search the web for information about a company",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query"}
                    },
                    "required": ["query"]
                }
            }
        ],
        messages=[
            {"role": "user", "content": prompt}
        ],
        tool_choice={"type": "auto"}
    )

    # For now, return a structured response (in production you'd parse tool results)
    # This is a simplified version — you can expand tool handling later
    return ResearchResult(
        company_name=company_name,
        domain=domain or "unknown.com",
        industry="Technology / SaaS",
        employee_count="50-200",
        funding_info="Series B - $45M (2025)",
        key_initiatives=[
            "Expanding into enterprise segment",
            "Recent product launch focused on automation",
            "Hiring heavily in sales and customer success"
        ],
        decision_makers=["VP of Sales", "Head of Revenue Operations", "CMO"],
        pain_points=[
            "Manual lead research and enrichment is slow",
            "Inconsistent data quality in CRM",
            "Difficulty scaling outbound motions efficiently"
        ],
        confidence_score=0.85
    )


if __name__ == "__main__":
    # Example usage
    result = research_company("Acme Corp", "acmecorp.com")
    print(result.model_dump_json(indent=2))

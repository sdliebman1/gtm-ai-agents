"""
Example Usage - GTM AI Agents
Demonstrates how to use the Research and Enrichment agents together.
"""

from agents.research_agent import research_company
from agents.enrichment_agent import enrich_company_data


def main():
    print("=" * 60)
    print("GTM AI Agents - Example Workflow")
    print("=" * 60)

    # Step 1: Research a company
    print("\n[1] Running Research Agent...")
    research_result = research_company(
        company_name="Acme Corp", 
        domain="acmecorp.com"
    )
    print(f"Research completed for: {research_result.company_name}")
    print(f"Key initiatives found: {len(research_result.key_initiatives)}")

    # Step 2: Enrich the company data
    print("\n[2] Running Enrichment Agent...")
    enriched_result = enrich_company_data(
        company_name=research_result.company_name,
        domain=research_result.domain
    )
    print(f"Enrichment completed for: {enriched_result.company_name}")
    print(f"Tech stack identified: {enriched_result.tech_stack}")
    print(f"Recent signals: {len(enriched_result.recent_signals)}")

    # Final Output Summary
    print("\n" + "=" * 60)
    print("FINAL ENRICHED OUTPUT (Ready for CRM/Outreach)")
    print("=" * 60)
    print(f"Company: {enriched_result.company_name}")
    print(f"Industry: {enriched_result.industry}")
    print(f"Employee Count: {enriched_result.employee_count}")
    print(f"Tech Stack: {', '.join(enriched_result.tech_stack)}")
    print(f"Recent Signals: {enriched_result.recent_signals}")
    print(f"Key Contacts: {len(enriched_result.key_contacts)} identified")


if __name__ == "__main__":
    main()

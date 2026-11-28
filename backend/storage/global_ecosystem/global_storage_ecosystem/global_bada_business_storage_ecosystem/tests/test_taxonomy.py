"""Offline taxonomy tests; no vendor API calls."""
from ..ecosystem_taxonomy import load_taxonomy,list_ecosystems,find_ecosystem
def test_two_business_domains_are_indexed():
 data=load_taxonomy();assert len(data["groups"])==2;assert len(list_ecosystems())==2
def test_domain_lookup():
 assert find_ecosystem("AFFILIATE_MARKETING") is not None
 assert find_ecosystem("NETWORK_MARKETING_AND_DIRECT_SELLING") is not None

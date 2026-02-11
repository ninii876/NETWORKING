import ip_address_analyze
import connectivity_check
import security_rule_engine
import innovation_section

print("NETWORK SIMULATOR")
print("\n-----ip_address_analyze-----")
ip_address_analyze.analyze_ip()
print("\n-----connectivity_check-----")
connectivity_check.check_connectivity()
print("\n-----security_rule_engine-----")
security_rule_engine.vlan_segmentation()
print("\n-----innovation_section----")
innovation_section.detect_ip_conflicts()

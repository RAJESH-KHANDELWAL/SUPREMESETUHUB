"""Framework-neutral quality strategy builder."""
TEST_LAYERS = ("unit","integration","contract","security","privacy","accessibility","performance","resilience","end_to_end")
def build_test_strategy(product_type: str, risk_level: str = "standard") -> dict:
    if risk_level not in {"low","standard","high","critical"}: raise ValueError("Unsupported risk_level")
    layers = list(TEST_LAYERS)
    if risk_level == "low": layers.remove("resilience")
    if risk_level in {"high","critical"}: layers.extend(("dependency_audit","threat_model_validation","disaster_recovery"))
    return {"product_type":product_type.strip(),"risk_level":risk_level,"recommended_layers":layers,"status":"PLAN_ONLY"}

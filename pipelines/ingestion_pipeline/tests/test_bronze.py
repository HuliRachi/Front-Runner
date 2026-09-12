
import pytest

from bronze_quality_logic import quarantine_rule


def test_quarantine_rule_combines_multiple_rules():
    rules = {
        "valid_order_id": "after.order_id IS NOT NULL",
        "valid_total_amount": "after.total_amount IS NULL OR after.total_amount >= 0",
    }

    result = quarantine_rule(rules)

    assert result == "NOT(after.order_id IS NOT NULL AND after.total_amount IS NULL OR after.total_amount >= 0)"


def test_quarantine_rule_rejects_empty_dict():
   
    with pytest.raises(ValueError, match="requires at least one rule"):
        quarantine_rule({})

import json
import logging

from replace_me_data.logging import JsonFormatter


def test_structured_log_uses_safe_allow_list() -> None:
    record = logging.LogRecord(
        "pipeline",
        logging.INFO,
        __file__,
        1,
        "loaded",
        (),
        None,
    )
    record.run_id = "test-run"
    record.secret = "must-not-be-logged"
    payload = json.loads(JsonFormatter().format(record))
    assert payload["event"] == "loaded"
    assert payload["run_id"] == "test-run"
    assert "secret" not in payload
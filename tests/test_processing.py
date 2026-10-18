from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(
    sample_operations: list[dict[str, int | str]],
) -> None:
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_canceled(
    sample_operations: list[dict[str, int | str]],
) -> None:
    result = filter_by_state(sample_operations, "CANCELED")
    assert len(result) == 2
    assert all(item["state"] == "CANCELED" for item in result)


def test_sort_by_date_desc(
    sample_operations: list[dict[str, int | str]],
) -> None:
    result = sort_by_date(sample_operations)
    assert result[0]["id"] == 41428829
    assert result[-1]["id"] == 939719570


def test_sort_by_date_asc(
    sample_operations: list[dict[str, int | str]],
) -> None:
    result = sort_by_date(sample_operations, reverse=False)
    assert result[0]["id"] == 939719570
    assert result[-1]["id"] == 41428829

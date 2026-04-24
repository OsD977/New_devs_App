from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def parse_timezone(tz_string: str) -> ZoneInfo:
    """
    Safely parses a timezone string, falling back to UTC if invalid.
    """
    try:
        return ZoneInfo(tz_string)
    except (ZoneInfoNotFoundError, KeyError) as e:
        print(f"WARNING: Invalid timezone '{tz_string}', falling back to UTC. Error: {e}")
        return ZoneInfo("UTC")
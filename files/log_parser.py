"""
Section 9: Log File Parser
Covers: Regex, Functions, Handle Error and Exceptions, Dictionary
"""

import re
import os

SAMPLE_LOG = os.path.join(os.path.dirname(__file__), "data", "sample.log")

LOG_LINE_RE = re.compile(
    r"^\[(?P<timestamp>[\d\-: ]+)\]\s+(?P<level>\w+)\s+(?P<message>.*)$"
)


def ensure_sample_log():
    os.makedirs(os.path.dirname(SAMPLE_LOG), exist_ok=True)
    if not os.path.exists(SAMPLE_LOG):
        with open(SAMPLE_LOG, "w") as f:
            f.write(
                "[2026-09-20 10:01:15] INFO Server started\n"
                "[2026-09-20 10:02:03] WARNING Disk usage at 80%\n"
                "[2026-09-20 10:03:44] ERROR Database connection failed\n"
                "[2026-09-20 10:04:10] INFO Retrying connection\n"
                "[2026-09-20 10:04:12] ERROR Database connection failed\n"
                "[2026-09-20 10:05:01] INFO Connection restored\n"
            )


def parse_log(path):
    counts = {}
    parsed_lines = []
    try:
        with open(path, "r") as f:
            for line in f:
                match = LOG_LINE_RE.match(line.strip())
                if match:
                    level = match.group("level")
                    counts[level] = counts.get(level, 0) + 1
                    parsed_lines.append(match.groupdict())
    except FileNotFoundError:
        print(f"Log file not found: {path}")
        return [], {}
    return parsed_lines, counts


def run_log_parser_menu():
    print("\n--- Log File Parser ---")
    ensure_sample_log()
    print(f"Using sample log at: {SAMPLE_LOG}")
    parsed_lines, counts = parse_log(SAMPLE_LOG)

    if not parsed_lines:
        return

    print("\nParsed entries:")
    for entry in parsed_lines:
        print(f"  [{entry['timestamp']}] {entry['level']}: {entry['message']}")

    print("\nCounts by level:")
    for level, count in counts.items():
        print(f"  {level}: {count}")

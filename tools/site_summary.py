import json
from datetime import datetime

class SiteEntry:
    """Represents a single site entry with structured metadata."""

    def __init__(self, url, title, keywords, description, tags):
        self.url = url
        self.title = title
        self.keywords = keywords
        self.description = description
        self.tags = tags

    def to_dict(self):
        return {
            "url": self.url,
            "title": self.title,
            "keywords": self.keywords,
            "description": self.description,
            "tags": self.tags
        }

def load_site_samples():
    """Return a list of predefined site entries for demonstration."""
    entries = [
        SiteEntry(
            url="https://pc-leyu.com",
            title="Leyu Platform",
            keywords=["leyu", "entertainment", "pc games", "digital leisure"],
            description="A digital entertainment hub featuring casual games and interactive content.",
            tags=["gaming", "leisure", "online"]
        ),
        SiteEntry(
            url="https://example-news.org",
            title="Global News Feed",
            keywords=["news", "updates", "world", "current events"],
            description="Up-to-date coverage on international headlines and local stories.",
            tags=["news", "media", "information"]
        ),
        SiteEntry(
            url="https://docs.example.com",
            title="Technical Documentation Portal",
            keywords=["docs", "tutorials", "api", "reference"],
            description="Comprehensive guides and API references for developers.",
            tags=["development", "docs", "programming"]
        )
    ]
    return entries

def format_entry_summary(entry, index):
    """Format a single entry into a readable summary string."""
    lines = [
        f"Entry #{index + 1}",
        f"  Title: {entry.title}",
        f"  URL: {entry.url}",
        f"  Keywords: {', '.join(entry.keywords)}",
        f"  Description: {entry.description}",
        f"  Tags: {', '.join(entry.tags)}"
    ]
    return "\n".join(lines)

def build_markdown_report(entries):
    """Generate a Markdown-formatted report from a list of SiteEntry objects."""
    report_lines = [
        "# Site Summary Report",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Entries Overview",
        ""
    ]
    for idx, entry in enumerate(entries):
        report_lines.append(format_entry_summary(entry, idx))
        report_lines.append("")
    report_lines.append("---")
    report_lines.append(f"Total entries: {len(entries)}")
    return "\n".join(report_lines)

def build_json_output(entries):
    """Return a JSON string representing all entries."""
    data = {
        "generated_at": datetime.now().isoformat(),
        "entries": [e.to_dict() for e in entries]
    }
    return json.dumps(data, indent=2, ensure_ascii=False)

def print_structured_summary():
    """Print a structured text summary of site entries."""
    entries = load_site_samples()
    separator = "=" * 60
    print(separator)
    print("SITE SUMMARY — STRUCTURED OUTPUT")
    print(separator)
    for idx, entry in enumerate(entries):
        print(format_entry_summary(entry, idx))
        print(separator)

def main():
    mode = "markdown"  # options: markdown, json, text
    entries = load_site_samples()

    if mode == "markdown":
        report = build_markdown_report(entries)
        print(report)
    elif mode == "json":
        output = build_json_output(entries)
        print(output)
    elif mode == "text":
        print_structured_summary()
    else:
        print("Unknown output mode.")

if __name__ == "__main__":
    main()
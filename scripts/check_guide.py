#!/usr/bin/env python3
"""Check this collection's Markdown without third-party packages or network access."""

import html
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)(?:\s+#+)?\s*$")
LINK = re.compile(r"\[([^]\n]+)\]\((<[^>\n]+>|(?:[^\s()]|\([^\s()]*\))+?)\)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
INLINE_CODE = re.compile(r"(`+).*?(?<!`)\1(?!`)")
RESOURCE_ENTRY = re.compile(r"^ {0,3}(?:-|\d+\.) \[")
RESOURCE_DETAILS = re.compile(r" - \S")
DIFFICULTY_LABEL = re.compile(r"\*\*(?:Beginner|Intermediate|Advanced|Expert)\b", re.IGNORECASE)
PUNCTUATION = {"—": "em dash", ";": "semicolon", ":": "colon"}


def document_lines(text):
    """Keep line numbers and distinguish prose examples from executable fences."""
    fence = None
    prose_example = False
    for number, line in enumerate(text.splitlines(), 1):
        marker = FENCE.match(line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            elif prose_example:
                yield number, line, False
            continue
        if marker:
            fence = marker[1]
            prose_example = marker[2].strip().lower() in {"text", "plaintext", "markdown", "md"}
            continue
        # Indented code blocks are outside the supported prose format.
        if line.startswith(("    ", "\t")):
            continue
        yield number, line, True


def prose_text(line):
    line = INLINE_CODE.sub("", line)
    # Link text keeps each source's original title, including its punctuation.
    line = LINK.sub("", line)
    line = re.sub(r"(?:https?://|mailto:)[^\s<>]+", "", line)
    return html.unescape(line)


def heading_anchors(lines):
    anchors = set()
    for _, line, structural in lines:
        match = HEADING.match(line) if structural else None
        if not match:
            continue
        title = LINK.sub(lambda link: link[1], match[2])
        title = html.unescape(re.sub(r"<[^>]*>", "", title)).lower()
        base = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        slug = base
        suffix = 0
        while slug in anchors:
            suffix += 1
            slug = f"{base}-{suffix}"
        anchors.add(slug)
    return anchors


def check_repository(root):
    root = root.resolve()
    paths = [root / "README.md", root / "CONTRIBUTING.md"]
    documents = {}
    errors = []
    for path in paths:
        try:
            documents[path] = list(document_lines(path.read_text(encoding="utf-8")))
        except (OSError, UnicodeError) as error:
            errors.append(f"{path.relative_to(root)} could not be read ({error})")
    anchors = {path: heading_anchors(lines) for path, lines in documents.items()}

    for path, lines in documents.items():
        def report(number, message):
            errors.append(f"{path.relative_to(root)} line {number} - {message}")

        section = "document introduction"
        section_resources = set()
        required_sections = []

        def finish_sections(level):
            while required_sections and required_sections[-1]["level"] >= level:
                finished = required_sections.pop()
                if not finished["has_resource"]:
                    report(finished["line"], f"resource section {finished['title']!r} has no external resource entry")

        for number, line, structural in lines:
            prose = prose_text(line)
            for character, name in PUNCTUATION.items():
                if character in prose:
                    report(number, f"remove {name} from prose")
            if not structural:
                continue
            # Ignore example links and headings inside inline code.
            content = INLINE_CODE.sub("", line)
            if path == root / "README.md" and DIFFICULTY_LABEL.search(content):
                report(number, "difficulty labels are not part of the source collection")
            heading = HEADING.match(content)
            if heading and path == root / "README.md":
                level = len(heading[1])
                finish_sections(level)
                if level == 3 or (level == 2 and (re.match(r"\d+\. ", heading[2]) or heading[2] == "Frontier")):
                    required_sections.append({"level": level, "line": number, "title": heading[2], "has_resource": False})
                section = heading[2]
                section_resources = set()

            for link in LINK.finditer(content):
                target = link[2].strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    continue
                destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
                if not destination.is_relative_to(root):
                    report(number, f"local link leaves the repository ({target})")
                    continue
                if not destination.is_file():
                    report(number, f"missing local file ({target})")
                    continue
                if parsed.fragment and destination.suffix.lower() == ".md":
                    if destination not in anchors:
                        try:
                            anchors[destination] = heading_anchors(list(document_lines(destination.read_text(encoding="utf-8"))))
                        except (OSError, UnicodeError):
                            report(number, f"cannot read linked document ({target})")
                            continue
                    if unquote(parsed.fragment) not in anchors[destination]:
                        report(number, f"missing heading ({target})")

            entry = RESOURCE_ENTRY.match(content)
            if path != root / "README.md" or not entry:
                continue
            resource = LINK.match(content, entry.end() - 1)
            if not resource:
                continue
            target = resource[2].strip("<>")
            if not target.startswith(("https://", "http://")):
                continue
            if not RESOURCE_DETAILS.match(content[resource.end():]):
                report(number, "resource entry needs a description after a hyphen")
            for required in required_sections:
                required["has_resource"] = True
            normalized = target.rstrip("/")
            if normalized in section_resources:
                report(number, f"duplicate resource in {section!r} ({target})")
            section_resources.add(normalized)
        finish_sections(0)
    return errors


def main():
    errors = check_repository(ROOT)
    if errors:
        print("Guide checks failed")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Guide checks passed for README.md and CONTRIBUTING.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

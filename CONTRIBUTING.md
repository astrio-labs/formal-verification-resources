# Contributing

This list is a reading path into formal verification. Add a source only if it fills a gap in the path or teaches a topic better than the current entry. Cryptography is out of scope.

## What belongs here

Good sources are the paper that introduced an idea, official documentation and tutorials, the repository that holds a tool or proof, and write-ups by the people who did the work. Among these, prefer the one a newcomer can learn from. Summaries, secondhand tutorials, marketing pages, and broad surveys do not belong.

Place each source where it fits in the order, from techniques to their applications. A subsection holds at most five sources, so a sixth must replace one.

## Entry format

```markdown
- [Original title](https://example.org/resource) - What it covers, in a few words.
```

Use the original title as link text and keep the description to a few words. Link a paper, chapter, or page rather than a whole textbook, except in Start here, and do not repeat Start here sources in topic sections. Mention paid access or an outdated toolchain. Write prose without em dashes, semicolons, or colons.

## Verification claims

An entry that reports a verification result should make clear what was proved, about which artifact, with which tool, under which assumptions, and within what bounds. It should also say whether the result is a model check, a program proof, or a theorem. Leave the claim out if any of this is unclear.

## Frontier

Frontier holds recent AI-assisted proving work. Each entry needs something others can inspect, such as a paper, released proofs, or code. Work moves into the main sections once it has an original paper, a released artifact, and results that others have checked.

## Pull requests

State the source, the section it belongs in, what it adds, and any affiliation with the work. Open the link yourself and confirm that the description matches it.

Run `python3 scripts/check_guide.py` before submitting. It checks local links and anchors, duplicate links, and punctuation. A weekly job checks external links, and pages that block automated requests are listed in [.lycheeignore](.lycheeignore).

Review the source, not the person proposing it.

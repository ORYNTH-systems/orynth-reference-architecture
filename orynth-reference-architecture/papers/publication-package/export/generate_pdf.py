from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from pathlib import Path
import html

base = Path(__file__).resolve().parent.parent

source = base / "PUBLICATION_DRAFT.md"
output = Path(__file__).resolve().parent / "ORYNTH_REFERENCE_ARCHITECTURE_v1.0.0.pdf"

text = source.read_text(encoding="utf-8")

doc = SimpleDocTemplate(
    str(output),
    title="ORYNTH Reference Architecture",
    author="Ashley S. Harris"
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Heading1"],
    fontSize=15,
    leading=19,
    spaceAfter=16
)

heading_style = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading2"],
    fontSize=12,
    leading=15,
    spaceBefore=12,
    spaceAfter=8
)

body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontSize=10,
    leading=14
)

story = []

for raw_line in text.splitlines():

    line = raw_line.strip()

    if not line:
        story.append(Spacer(1, 8))
        continue

    line = line.replace("\\", "")

    # Markdown headings
    if line.startswith("# "):
        story.append(
            Paragraph(
                html.escape(line[2:]),
                title_style
            )
        )

    elif line.startswith("## "):
        story.append(
            Paragraph(
                html.escape(line[3:]),
                heading_style
            )
        )

    # Bullets
    elif line.startswith("- "):
        story.append(
            Paragraph(
                html.escape("• " + line[2:]),
                body_style
            )
        )

    # Horizontal separators
    elif line == "---":
        story.append(Spacer(1, 14))

    # Diagram artifacts
    elif line in ["fi", "fl", "v"]:
        story.append(
            Paragraph(
                "↓",
                body_style
            )
        )

    # Normal text
    else:
        cleaned = line

        # Preserve words containing "fi"
        # Only convert isolated broken arrow text
        if cleaned == "fi":
            cleaned = "↓"

        story.append(
            Paragraph(
                html.escape(cleaned),
                body_style
            )
        )

    story.append(Spacer(1, 5))

doc.build(story)

print(f"Generated: {output}")
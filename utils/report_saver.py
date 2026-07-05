from pathlib import Path


def save_report(company, report):

    # Create reports folder if it doesn't exist
    Path("reports").mkdir(exist_ok=True)

    # Create filename
    filename = Path("reports") / f"{company}_report.md"

    # Save report
    filename.write_text(report, encoding="utf-8")

    print(f"\nReport saved to: {filename}")

    return filename
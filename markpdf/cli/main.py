import argparse
from pathlib import Path

from markpdf.markpdf import MarkPDF


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    MarkPDF().render(args.input, args.output)


if __name__ == "__main__":
    main()

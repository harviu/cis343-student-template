"""Download the current released practice tests and run them locally."""
from pathlib import Path
import subprocess
import sys
import tempfile


def main():
    project = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="cis343-tests-") as temp:
        tests = Path(temp) / "tests"
        try:
            subprocess.run([
                "git", "clone", "--depth", "1", "--branch", "main",
                "https://github.com/harviu/cis343-tests.git", str(tests),
            ], check=True, timeout=120)
            return subprocess.run([
                sys.executable, str(tests / "run_tests.py"),
                str(project), *sys.argv[1:],
            ], check=False).returncode
        except (OSError, subprocess.SubprocessError) as error:
            print(f"Could not fetch/run instructor tests: {error}", file=sys.stderr)
            return 2


if __name__ == "__main__":
    sys.exit(main())

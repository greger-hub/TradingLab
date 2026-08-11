#!/usr/bin/env python3

"""
TradingLab Package Tool

Skapar, verifierar och säkerhetskontrollerar en ZIP-fil inför release.

Kör:
    python3 tools/package.py
"""

from datetime import datetime
from pathlib import Path
import os
import re
import sys
import zipfile


# ==========================================================
# Konfiguration
# ==========================================================

VERSION = "0.4.1"

PROJECT_NAME = "TradingLab"

RELEASE_FOLDER = "releases"

EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".venv",
    "venv",
    "build",
    "dist",
}

EXCLUDED_FILES = {
    ".env",
    ".DS_Store",
}

EXCLUDED_SUFFIXES = {
    ".pyc",
}

CRITICAL_ZIP_ENTRIES = (
    ".env",
    ".git/",
    "__pycache__/",
    ".venv/",
    "venv/",
)

#
# Mönster för misstänkta hårdkodade hemligheter.
#
SECRET_ASSIGNMENT_PATTERN = re.compile(
    r"""
    (?P<name>
        API_KEY
        |API_TOKEN
        |ACCESS_KEY
        |SECRET
        |SECRET_KEY
        |AUTH_TOKEN
        |TOKEN
        |PASSWORD
        |PASSWD
        |PRIVATE_KEY
    )
    \s*
    =
    \s*
    (?P<quote>["'])
    (?P<value>[^"']+)
    (?P=quote)
    """,
    re.IGNORECASE | re.VERBOSE,
)

#
# Värden som uppenbart är exempel eller placeholders.
#
PLACEHOLDER_VALUES = {
    "",
    "your_api_key",
    "your_api_token",
    "your_token",
    "your_secret",
    "your_secret_key",
    "your_password",
    "change_me",
    "changeme",
    "example",
    "example_key",
    "replace_me",
    "replace-me",
    "xxx",
    "xxxx",
    "xxxxx",
    "none",
    "null",
}

#
# Enkel kontroll av Bearer-token som faktiskt hårdkodats.
#
BEARER_PATTERN = re.compile(
    r"""Bearer\s+[A-Za-z0-9._~+/=-]{12,}""",
    re.IGNORECASE,
)


# ==========================================================
# Hjälpfunktioner
# ==========================================================

def find_project_root() -> Path:
    """
    package.py ligger i tools/.

    Projektroten är därför parent.parent.
    """
    return Path(__file__).resolve().parent.parent


def relative_path(path: Path, project_root: Path) -> str:
    """
    Returnerar en sökväg relativt projektroten.
    """
    return str(path.relative_to(project_root))


def check_project_files(
    project_root: Path,
) -> tuple[bool, list[str]]:
    """
    Kontrollerar grundläggande projektfiler.

    Returnerar:
        (critical_ok, warnings)
    """

    warnings = []
    critical_ok = True

    print("Projektkontroll")
    print("-" * 60)

    gitignore = project_root / ".gitignore"

    if gitignore.exists():
        print("✓ .gitignore hittad")
    else:
        print("✗ FEL: .gitignore saknas")
        critical_ok = False

    readme = project_root / "README.md"

    if readme.exists():
        print("✓ README.md hittad")
    else:
        warning = "README.md saknas"
        warnings.append(warning)
        print(f"⚠ VARNING: {warning}")

    requirements = project_root / "requirements.txt"

    if requirements.exists():
        print("✓ requirements.txt hittad")
    else:
        warning = "requirements.txt saknas"
        warnings.append(warning)
        print(f"⚠ VARNING: {warning}")

    print()

    return critical_ok, warnings


def create_release_directory(
    project_root: Path,
) -> Path:
    """
    Skapar releases-katalogen om den inte redan finns.
    """
    release_dir = project_root / RELEASE_FOLDER
    release_dir.mkdir(exist_ok=True)

    return release_dir


def should_exclude_file(
    file_path: Path,
    release_dir: Path,
) -> bool:
    """
    Returnerar True om filen inte ska inkluderas i ZIP-filen.
    """

    if file_path.name in EXCLUDED_FILES:
        return True

    if file_path.suffix in EXCLUDED_SUFFIXES:
        return True

    if file_path.parent == release_dir:
        return True

    return False


# ==========================================================
# Paketering
# ==========================================================

def create_zip(
    project_root: Path,
    release_dir: Path,
    zip_path: Path,
) -> tuple[int, int, int]:
    """
    Skapar ZIP-filen.

    Returnerar:
        included_files
        excluded_dirs
        excluded_files
    """

    included_files = 0
    excluded_dirs = 0
    excluded_files = 0

    print("Paketering")
    print("-" * 60)

    with zipfile.ZipFile(
        zip_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:

        for root, dirs, files in os.walk(project_root):

            root_path = Path(root)

            #
            # Hoppa över hela katalogträd.
            #
            dirs_to_remove = []

            for directory in dirs:

                if directory in EXCLUDED_DIRS:

                    excluded_dirs += 1

                    excluded_path = root_path / directory

                    print(
                        f"Exkluderar katalog: "
                        f"{relative_path(excluded_path, project_root)}"
                    )

                    dirs_to_remove.append(directory)

            for directory in dirs_to_remove:
                dirs.remove(directory)

            #
            # Lägg till filer.
            #
            for file in files:

                file_path = root_path / file

                if should_exclude_file(
                    file_path,
                    release_dir,
                ):

                    excluded_files += 1

                    print(
                        f"Exkluderar fil: "
                        f"{relative_path(file_path, project_root)}"
                    )

                    continue

                archive.write(
                    file_path,
                    file_path.relative_to(project_root),
                )

                included_files += 1

    print()

    return (
        included_files,
        excluded_dirs,
        excluded_files,
    )


# ==========================================================
# ZIP-verifiering
# ==========================================================

def verify_zip(
    zip_path: Path,
) -> tuple[bool, list[str]]:
    """
    Verifierar att ZIP-filen inte innehåller förbjudna objekt.

    Returnerar:
        (verification_ok, errors)
    """

    errors = []

    print("ZIP-verifiering")
    print("-" * 60)

    if not zip_path.exists():

        error = "ZIP-filen kunde inte hittas."

        errors.append(error)

        print(f"✗ FEL: {error}")
        print()

        return False, errors

    try:

        with zipfile.ZipFile(
            zip_path,
            "r",
        ) as archive:

            names = archive.namelist()

    except zipfile.BadZipFile:

        error = "ZIP-filen är korrupt eller ogiltig."

        errors.append(error)

        print(f"✗ FEL: {error}")
        print()

        return False, errors

    for name in names:

        normalized = name.replace("\\", "/")

        for forbidden in CRITICAL_ZIP_ENTRIES:

            if forbidden.endswith("/"):
                if (
                    normalized == forbidden.rstrip("/")
                    or normalized.startswith(forbidden)
                ):
                    errors.append(
                        f"Förbjudet objekt hittades i ZIP: "
                        f"{name}"
                    )

            elif normalized == forbidden:
                errors.append(
                    f"Förbjuden fil hittades i ZIP: "
                    f"{name}"
                )

    if errors:

        for error in errors:
            print(f"✗ FEL: {error}")

        print()

        return False, errors

    print("✓ .env finns inte i ZIP")
    print("✓ .git finns inte i ZIP")
    print("✓ __pycache__ finns inte i ZIP")
    print("✓ .venv finns inte i ZIP")
    print()

    return True, errors


# ==========================================================
# Säkerhetsskanning
# ==========================================================

def is_placeholder(value: str) -> bool:
    """
    Avgör om ett värde uppenbart är ett exempelvärde.
    """

    normalized = value.strip().lower()

    if normalized in PLACEHOLDER_VALUES:
        return True

    if normalized.startswith("your_"):
        return True

    if normalized.startswith("replace_"):
        return True

    if normalized.startswith("replace-"):
        return True

    if normalized.startswith("example_"):
        return True

    return False


def scan_python_file(
    file_path: Path,
    project_root: Path,
) -> list[str]:
    """
    Skannar en Python-fil efter misstänkta hårdkodade
    hemligheter.

    Returnerar en lista med träffar.
    """

    findings = []

    try:

        content = file_path.read_text(
            encoding="utf-8",
        )

    except UnicodeDecodeError:

        return [
            (
                f"{relative_path(file_path, project_root)}: "
                "kunde inte läsas som UTF-8"
            )
        ]

    except OSError as error:

        return [
            (
                f"{relative_path(file_path, project_root)}: "
                f"kunde inte läsas ({error})"
            )
        ]

    lines = content.splitlines()

    for line_number, line in enumerate(
        lines,
        start=1,
    ):

        #
        # Kontroll av hårdkodade assignment-värden.
        #
        matches = SECRET_ASSIGNMENT_PATTERN.finditer(line)

        for match in matches:

            value = match.group("value").strip()

            if is_placeholder(value):
                continue

            variable_name = match.group("name")

            findings.append(
                (
                    f"{relative_path(file_path, project_root)}:"
                    f"{line_number} - "
                    f"möjligt hårdkodat {variable_name}"
                )
            )

        #
        # Kontroll av hårdkodade Bearer-token.
        #
        bearer_match = BEARER_PATTERN.search(line)

        if bearer_match:

            findings.append(
                (
                    f"{relative_path(file_path, project_root)}:"
                    f"{line_number} - "
                    "möjlig hårdkodad Bearer-token"
                )
            )

    return findings


def scan_for_secrets(
    project_root: Path,
) -> tuple[bool, list[str]]:
    """
    Skannar projektets Python-filer efter misstänkta
    hårdkodade hemligheter.

    Returnerar:
        (security_ok, findings)
    """

    findings = []

    print("Säkerhetsskanning")
    print("-" * 60)

    for root, dirs, files in os.walk(project_root):

        root_path = Path(root)

        #
        # Skippa kataloger som ändå inte ska ingå i release.
        #
        dirs[:] = [
            directory
            for directory in dirs
            if directory not in EXCLUDED_DIRS
        ]

        for file in files:

            if not file.endswith(".py"):
                continue

            file_path = root_path / file

            file_findings = scan_python_file(
                file_path,
                project_root,
            )

            findings.extend(file_findings)

    if not findings:

        print(
            "✓ Inga misstänkta hårdkodade "
            "hemligheter hittades"
        )
        print()

        return True, findings

    print(
        f"⚠ Hittade {len(findings)} "
        "misstänkta träff(ar):"
    )

    for finding in findings:
        print(f"  ⚠ {finding}")

    print()
    print(
        "✗ Säkerhetsskanningen kräver granskning."
    )
    print()

    return False, findings


# ==========================================================
# Release Report
# ==========================================================

def print_release_report(
    project_root: Path,
    zip_path: Path,
    included_files: int,
    excluded_dirs: int,
    excluded_files: int,
    warnings: list[str],
    verification_ok: bool,
    project_ok: bool,
    security_ok: bool,
    security_findings: list[str],
) -> None:
    """
    Skriver ut slutlig release-rapport.
    """

    print("=" * 60)
    print("TradingLab Release Report")
    print("=" * 60)

    print()
    print(f"Projekt                 : {project_root}")
    print(f"Version                 : {VERSION}")

    print()
    print("Paketering")
    print(
        f"  Paketerade filer      : "
        f"{included_files}"
    )
    print(
        f"  Exkluderade kataloger : "
        f"{excluded_dirs}"
    )
    print(
        f"  Exkluderade filer     : "
        f"{excluded_files}"
    )

    print()
    print("ZIP")
    print(f"  Fil                   : {zip_path}")

    print()
    print("Kontroller")

    if project_ok:
        print("  ✓ Projektkontroll godkänd")
    else:
        print("  ✗ Projektkontroll misslyckades")

    if verification_ok:
        print("  ✓ ZIP-verifiering godkänd")
    else:
        print("  ✗ ZIP-verifiering misslyckades")

    if security_ok:
        print("  ✓ Säkerhetsskanning godkänd")
    else:
        print("  ✗ Säkerhetsskanning misslyckades")

    if warnings:

        print()
        print("Varningar")

        for warning in warnings:
            print(f"  ⚠ {warning}")

    if security_findings:

        print()
        print("Säkerhetsträffar")

        for finding in security_findings:
            print(f"  ⚠ {finding}")

    print()

    if (
        project_ok
        and verification_ok
        and security_ok
    ):
        print("✓ RELEASE GODKÄND")
    else:
        print("✗ RELEASE STOPPAD")

    print()
    print("=" * 60)


# ==========================================================
# Huvudfunktion
# ==========================================================

def create_package() -> bool:
    """
    Skapar, verifierar och säkerhetskontrollerar
    en release.

    Returnerar:
        True  = release godkänd
        False = release stoppad
    """

    project_root = find_project_root()

    release_dir = create_release_directory(
        project_root
    )

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    zip_name = (
        f"{PROJECT_NAME}_v{VERSION}_"
        f"{today}.zip"
    )

    zip_path = release_dir / zip_name

    print("=" * 60)
    print("TradingLab Package Tool")
    print("=" * 60)

    print()
    print(f"Projekt : {project_root}")
    print(f"Version : {VERSION}")
    print()

    #
    # ------------------------------------------------------
    # 1. Projektkontroll
    # ------------------------------------------------------
    #

    project_ok, warnings = check_project_files(
        project_root
    )

    if not project_ok:

        print(
            "✗ Kritisk projektkontroll "
            "misslyckades."
        )
        print("  Paketeringen avbryts.")
        print()

        print_release_report(
            project_root=project_root,
            zip_path=zip_path,
            included_files=0,
            excluded_dirs=0,
            excluded_files=0,
            warnings=warnings,
            verification_ok=False,
            project_ok=False,
            security_ok=False,
            security_findings=[],
        )

        return False

    #
    # ------------------------------------------------------
    # 2. Säkerhetsskanning
    # ------------------------------------------------------
    #

    security_ok, security_findings = (
        scan_for_secrets(project_root)
    )

    if not security_ok:

        print(
            "✗ Kritiska säkerhetsträffar "
            "upptäcktes."
        )
        print(
            "  Releasepaketet skapas inte."
        )
        print()

        print_release_report(
            project_root=project_root,
            zip_path=zip_path,
            included_files=0,
            excluded_dirs=0,
            excluded_files=0,
            warnings=warnings,
            verification_ok=False,
            project_ok=True,
            security_ok=False,
            security_findings=security_findings,
        )

        return False

    #
    # ------------------------------------------------------
    # 3. Skapa ZIP
    # ------------------------------------------------------
    #

    try:

        (
            included_files,
            excluded_dirs,
            excluded_files,
        ) = create_zip(
            project_root,
            release_dir,
            zip_path,
        )

    except OSError as error:

        print()
        print(
            f"✗ FEL vid paketering: {error}"
        )
        print()

        if zip_path.exists():
            zip_path.unlink()

        print_release_report(
            project_root=project_root,
            zip_path=zip_path,
            included_files=0,
            excluded_dirs=0,
            excluded_files=0,
            warnings=warnings,
            verification_ok=False,
            project_ok=True,
            security_ok=True,
            security_findings=[],
        )

        return False

    #
    # ------------------------------------------------------
    # 4. Verifiera ZIP
    # ------------------------------------------------------
    #

    verification_ok, _ = verify_zip(
        zip_path
    )

    #
    # Om verifieringen misslyckas ska ingen
    # release-ZIP ligga kvar.
    #
    if not verification_ok:

        if zip_path.exists():
            zip_path.unlink()

    #
    # ------------------------------------------------------
    # 5. Slutrapport
    # ------------------------------------------------------
    #

    print_release_report(
        project_root=project_root,
        zip_path=zip_path,
        included_files=included_files,
        excluded_dirs=excluded_dirs,
        excluded_files=excluded_files,
        warnings=warnings,
        verification_ok=verification_ok,
        project_ok=True,
        security_ok=True,
        security_findings=[],
    )

    return verification_ok


# ==========================================================
# Start
# ==========================================================

if __name__ == "__main__":

    success = create_package()

    if success:
        sys.exit(0)

    sys.exit(1)
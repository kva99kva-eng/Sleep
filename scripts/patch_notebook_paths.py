from pathlib import Path
import shutil
import re
import nbformat

PROJECT_ROOT = Path.cwd()
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
BACKUP_DIR = PROJECT_ROOT / "_backup_before_path_patch"

if not NOTEBOOKS_DIR.exists():
    raise FileNotFoundError(f"Notebooks folder not found: {NOTEBOOKS_DIR}")

BACKUP_DIR.mkdir(exist_ok=True)

PATH_HELPER = """from pathlib import Path

def find_project_root(start=Path.cwd()):
    for p in [start, *start.parents]:
        if (p / 'README.md').exists() and (p / 'data').exists():
            return p
    raise FileNotFoundError('Project root not found. Make sure README.md and data/ exist.')

PROJECT_ROOT = find_project_root()
RAW_DIR = PROJECT_ROOT / 'data' / 'raw'
PROCESSED_DIR = PROJECT_ROOT / 'data' / 'processed'
FIGURES_DIR = PROJECT_ROOT / 'figures'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'

print('PROJECT_ROOT =', PROJECT_ROOT)
print('RAW_DIR =', RAW_DIR)
print('PROCESSED_DIR =', PROCESSED_DIR)
"""

MMASH_HELPER = """from pathlib import Path

mmash_candidates = list((RAW_DIR / 'mmash').rglob('DataPaper'))

print("Found MMASH candidates:")
for p in mmash_candidates:
    print(p)

if not mmash_candidates:
    raise FileNotFoundError(
        'DataPaper not found inside data/raw/mmash. '
        'Move the unpacked MMASH folder there first.'
    )

MMASH_BASE = mmash_candidates[0]
print("MMASH_BASE =", MMASH_BASE)

user_dirs = sorted([p for p in MMASH_BASE.iterdir() if p.is_dir() and p.name.startswith('user_')])

print(f'Found {len(user_dirs)} users')
print([p.name for p in user_dirs[:10]])
"""

COMMON_REGEX_REPLACEMENTS = [
    # hypno_df read
    (
        r"pd\.read_csv\(\s*r?['\"][^'\"]*hypno_df\.csv['\"]\s*\)",
        "pd.read_csv(RAW_DIR / 'sleep_edf' / 'hypno_df.csv')"
    ),
    # single-subject features save
    (
        r"features_df\.to_csv\(\s*.*?sleep_features_subject_001\.csv.*?\)",
        "features_df.to_csv(PROCESSED_DIR / 'sleep_features_subject_001.csv', index=False)"
    ),
    # all-subject features save
    (
        r"sleep_features_df\.to_csv\(\s*.*?sleep_features_all_subjects\.csv.*?\)",
        "sleep_features_df.to_csv(PROCESSED_DIR / 'sleep_features_all_subjects.csv', index=False)"
    ),
    # processing_log save
    (
        r"processing_log_df\.to_csv\(\s*.*?processing_log\.csv.*?\)",
        "processing_log_df.to_csv(PROCESSED_DIR / 'processing_log.csv', index=False)"
    ),
    # mmash save
    (
        r"mmash_df\.to_csv\(\s*.*?mmash_modeling_dataset\.csv.*?\)",
        "mmash_df.to_csv(PROCESSED_DIR / 'mmash_modeling_dataset.csv', index=False)"
    ),
    # paired outputs save
    (
        r"paired_summary\.to_csv\(\s*.*?paired_summary\.csv.*?\)",
        "paired_summary.to_csv(PROCESSED_DIR / 'paired_summary.csv', index=False)"
    ),
    (
        r"paired_results_df\.to_csv\(\s*.*?paired_results_df\.csv.*?\)",
        "paired_results_df.to_csv(PROCESSED_DIR / 'paired_results_df.csv', index=False)"
    ),
    # sleep deprivation csv read
    (
        r"pd\.read_csv\(\s*r?['\"][^'\"]*SD_CANTAB_DB_public\.csv['\"]\s*\)",
        "pd.read_csv(RAW_DIR / 'sleep_deprivation' / 'SD_CANTAB_DB_public.csv')"
    ),
]

def ensure_helper_cell(nb):
    if not nb.cells:
        nb.cells.insert(0, nbformat.v4.new_code_cell(PATH_HELPER))
        return True

    for cell in nb.cells[:3]:
        if cell.cell_type == "code" and "def find_project_root" in cell.source:
            return False

    nb.cells.insert(0, nbformat.v4.new_code_cell(PATH_HELPER))
    return True

def replace_mmash_cell(nb):
    changed = False
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue

        src = cell.source
        if (
            "MMASH DataPaper folder not found." in src
            or "Found MMASH candidates:" in src
            or "mmash_candidates" in src
            or "MMASH_BASE" in src and "user_dirs" in src
        ):
            cell.source = MMASH_HELPER
            changed = True
    return changed

def replace_common_patterns(nb):
    changed = 0
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue

        src = cell.source
        new_src = src

        for pattern, repl in COMMON_REGEX_REPLACEMENTS:
            new_src = re.sub(pattern, repl, new_src, flags=re.DOTALL)

        # 02.5 special case: if notebook explicitly sets csv_files to hypno_df.csv
        new_src = re.sub(
            r"csv_files\s*=\s*sorted\(\s*INPUT_DIR\.glob\(\s*['\"]hypno_df\.csv['\"]\s*\)\s*\)",
            "csv_files = [RAW_DIR / 'sleep_edf' / 'hypno_df.csv']",
            new_src
        )

        # 02.5 output path special cases
        new_src = re.sub(
            r"OUTPUT_FEATURES_PATH\s*=\s*Path\(\s*['\"]sleep_features_all_subjects\.csv['\"]\s*\)",
            "OUTPUT_FEATURES_PATH = PROCESSED_DIR / 'sleep_features_all_subjects.csv'",
            new_src
        )
        new_src = re.sub(
            r"OUTPUT_LOG_PATH\s*=\s*Path\(\s*['\"]processing_log\.csv['\"]\s*\)",
            "OUTPUT_LOG_PATH = PROCESSED_DIR / 'processing_log.csv'",
            new_src
        )

        # Sometimes INPUT_DIR = Path('.') can stay, but for your current setup one-file mode is safer
        new_src = re.sub(
            r"INPUT_DIR\s*=\s*Path\(\s*['\"]\.\s*['\"]\s*\)",
            "INPUT_DIR = RAW_DIR / 'sleep_edf'",
            new_src
        )

        if new_src != src:
            cell.source = new_src
            changed += 1

    return changed

def patch_notebook(nb_path):
    print(f"\\n--- Patching: {nb_path.name}")

    backup_path = BACKUP_DIR / nb_path.name
    shutil.copy2(nb_path, backup_path)

    nb = nbformat.read(nb_path, as_version=4)

    helper_added = ensure_helper_cell(nb)
    mmash_changed = replace_mmash_cell(nb)
    common_changed = replace_common_patterns(nb)

    nbformat.write(nb, nb_path)

    print("Backup:", backup_path)
    print("Added helper cell:", helper_added)
    print("Replaced MMASH block:", mmash_changed)
    print("Changed code cells:", common_changed)

notebooks = sorted(NOTEBOOKS_DIR.glob("*.ipynb"))

if not notebooks:
    raise FileNotFoundError(f"No notebooks found in {NOTEBOOKS_DIR}")

print("PROJECT_ROOT =", PROJECT_ROOT)
print("NOTEBOOKS_DIR =", NOTEBOOKS_DIR)
print("Found notebooks:")
for nb in notebooks:
    print("-", nb.name)

for nb in notebooks:
    patch_notebook(nb)

print("\\nDone.")
print("Check notebooks and run them from top to bottom.")
print("Backups saved in:", BACKUP_DIR)
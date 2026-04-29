import kagglehub
from pathlib import Path

output_path = Path("backend/src/data/jeopardy_data")

# Download latest version
path = kagglehub.dataset_download("tunguz/200000-jeopardy-questions", output_dir=output_path)

print("Path to dataset files:", path)
#!/bin/python

import sys
from pathlib import Path
import bw2io as bi

fp = Path(sys.argv[0]).resolve()
if not fp.is_file():
    print(f"Error with project filepath {fp}")

print(f"Restoring project file: {fp}")
bi.restore_project_directory(fp)

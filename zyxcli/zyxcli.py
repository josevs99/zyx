#!/usr/bin/env python3
import sys
from utils.repl import run_interactive, app

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Args provided → non-interactive
        app()
    else:
        # No args → interactive REPL
        run_interactive()

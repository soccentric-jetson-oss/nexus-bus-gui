# SPDX-License-Identifier: MIT
"""
Nexus Bus GUI - Application entry point.

Thin entry point that creates the QApplication and launches the
main window. All UI logic lives in src.app.NexusBusApp.
"""

import sys
from PySide6.QtWidgets import QApplication
from src.app import NexusBusApp


def main():
    """Create and run the Nexus Bus GUI application."""
    app = QApplication(sys.argv)
    app.setApplicationName("Nexus Bus")
    window = NexusBusApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

"""Dashboard page for Nexus Bus peripheral access."""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from src.theme import TITLE_STYLE, SUBTITLE_STYLE
from src.widgets import BigButtonBox, MacCard


class DashboardPage(QWidget):
    def __init__(self, client, parent=None):
        super().__init__(parent)
        self._client = client
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 24, 32, 24)
        layout.setSpacing(24)
        header = QLabel("Dashboard")
        header.setStyleSheet(TITLE_STYLE)
        layout.addWidget(header)
        desc = QLabel("Read and write to peripheral buses on Jetson AGX Orin.")
        desc.setStyleSheet(SUBTITLE_STYLE)
        layout.addWidget(desc)
        btn_row = QHBoxLayout()
        btn_row.setSpacing(20)
        self.read_box = BigButtonBox("Bus Read", "Read data from a peripheral bus.\nSelect bus type and address in Controls.", "Read", "primary")
        btn_row.addWidget(self.read_box)
        self.write_box = BigButtonBox("Bus Write", "Write data to a peripheral bus.\nConfigure value and address in Controls.", "Write", "secondary")
        btn_row.addWidget(self.write_box)
        layout.addLayout(btn_row)
        cards_row = QHBoxLayout()
        cards_row.setSpacing(16)
        self.status_card = MacCard("Status", "Idle", "", "#616161")
        self.bus_card = MacCard("Active Bus", "None", "")
        cards_row.addWidget(self.status_card)
        cards_row.addWidget(self.bus_card)
        layout.addLayout(cards_row)
        layout.addStretch()

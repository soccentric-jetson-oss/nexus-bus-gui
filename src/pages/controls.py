"""Controls page for Nexus Bus configuration."""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QSpinBox, QFrame
from src.theme import TITLE_STYLE, SUBTITLE_STYLE, SECTION_TITLE_STYLE, BIG_BUTTON_STYLE, CARD_STYLE, INPUT_STYLE


class ControlsPage(QWidget):
    def __init__(self, client, parent=None):
        super().__init__(parent)
        self._client = client
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 24, 32, 24)
        layout.setSpacing(24)
        header = QLabel("Controls")
        header.setStyleSheet(TITLE_STYLE)
        layout.addWidget(header)
        desc = QLabel("Configure bus type, address, and data for read/write operations.")
        desc.setStyleSheet(SUBTITLE_STYLE)
        layout.addWidget(desc)

        frame = QFrame()
        frame.setStyleSheet(CARD_STYLE)
        fl = QVBoxLayout(frame)
        fl.setSpacing(12)
        fl.addWidget(QLabel("Bus Configuration"))
        fl.itemAt(fl.count()-1).widget().setStyleSheet(SECTION_TITLE_STYLE)

        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Bus Type:"))
        self.type_cb = QComboBox()
        self.type_cb.addItems(["GPIO", "I2C", "SPI", "UART", "CAN"])
        self.type_cb.setStyleSheet(INPUT_STYLE)
        row1.addWidget(self.type_cb)
        row1.addStretch()
        fl.addLayout(row1)

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Address:"))
        self.addr_sb = QSpinBox()
        self.addr_sb.setRange(0, 255)
        self.addr_sb.setPrefix("0x")
        self.addr_sb.setStyleSheet(INPUT_STYLE)
        row2.addWidget(self.addr_sb)
        row2.addStretch()
        fl.addLayout(row2)

        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Value:"))
        self.val_sb = QSpinBox()
        self.val_sb.setRange(0, 65535)
        self.val_sb.setPrefix("0x")
        self.val_sb.setStyleSheet(INPUT_STYLE)
        row3.addWidget(self.val_sb)
        row3.addStretch()
        fl.addLayout(row3)

        btn_row = QHBoxLayout()
        self.read_btn = QPushButton("Read")
        self.read_btn.setStyleSheet(BIG_BUTTON_STYLE)
        self.read_btn.clicked.connect(lambda: self._client.read(self.type_cb.currentIndex(), 0, self.addr_sb.value(), 0))
        btn_row.addWidget(self.read_btn)
        self.write_btn = QPushButton("Write")
        self.write_btn.setStyleSheet(f"QPushButton {{background: #388E3C; color: white; border: none; border-radius: 12px; padding: 16px 32px; font-size: 15px; font-weight: 600; min-width: 180px; min-height: 48px;}} QPushButton:hover {{background: #2E7D32;}}")
        self.write_btn.clicked.connect(lambda: self._client.write(self.type_cb.currentIndex(), 0, self.addr_sb.value(), 0, self.val_sb.value()))
        btn_row.addWidget(self.write_btn)
        btn_row.addStretch()
        fl.addLayout(btn_row)
        layout.addWidget(frame)
        layout.addStretch()

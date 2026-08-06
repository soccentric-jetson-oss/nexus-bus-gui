"""Nexus Bus GUI - Main application window."""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QPushButton, QComboBox, QSpinBox, QFrame
)
from src.client.client import NexusBusClient


class NexusBusApp(QMainWindow):
    """Main application window for Nexus Bus GUI."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nexus Bus")
        self.setMinimumSize(600, 400)
        self._client = NexusBusClient()
        self._setup_ui()
        self._client.connect()
        self._update_status()

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(QLabel("Nexus Bus — Peripheral Access"))

        # Bus configuration form
        form_frame = QFrame()
        form_frame.setFrameStyle(QFrame.StyledPanel)
        form = QFormLayout(form_frame)

        self.type_cb = QComboBox()
        self.type_cb.addItems(["GPIO", "I2C", "SPI", "UART", "CAN"])
        self.id_sb = QSpinBox()
        self.id_sb.setRange(0, 7)
        self.addr_sb = QSpinBox()
        self.addr_sb.setRange(0, 255)
        self.addr_sb.setPrefix("0x")
        self.reg_sb = QSpinBox()
        self.reg_sb.setRange(0, 255)
        self.reg_sb.setPrefix("0x")
        self.val_sb = QSpinBox()
        self.val_sb.setRange(0, 65535)
        self.val_sb.setPrefix("0x")

        form.addRow("Bus Type:", self.type_cb)
        form.addRow("Bus ID:", self.id_sb)
        form.addRow("Address:", self.addr_sb)
        form.addRow("Register:", self.reg_sb)
        form.addRow("Value:", self.val_sb)
        layout.addWidget(form_frame)

        # Action buttons
        btn_row = QHBoxLayout()
        self.read_btn = QPushButton("Read")
        self.read_btn.clicked.connect(self._on_read)
        self.write_btn = QPushButton("Write")
        self.write_btn.clicked.connect(self._on_write)
        btn_row.addWidget(self.read_btn)
        btn_row.addWidget(self.write_btn)
        layout.addLayout(btn_row)

        # Result display
        self.result_label = QLabel("Result: --")
        self.result_label.setStyleSheet("color:#616161; font-size:14px;")
        layout.addWidget(self.result_label)
        layout.addStretch()

    def _update_status(self):
        if self._client.connected:
            self.result_label.setText("Connected")
        else:
            self.result_label.setText("Disconnected")

    def _on_read(self):
        result = self._client.read(
            self.type_cb.currentIndex(), self.id_sb.value(),
            self.addr_sb.value(), self.reg_sb.value()
        )
        if result["success"]:
            self.result_label.setText(f"Value: 0x{result['value']:X}")
        else:
            self.result_label.setText(f"Error: {result['error']}")

    def _on_write(self):
        result = self._client.write(
            self.type_cb.currentIndex(), self.id_sb.value(),
            self.addr_sb.value(), self.reg_sb.value(), self.val_sb.value()
        )
        if result["success"]:
            self.result_label.setText("Write OK")
        else:
            self.result_label.setText(f"Error: {result['error']}")

import sys; from PySide6.QtWidgets import *; from PySide6.QtCore import Qt
import grpc; from src.client import nexus_bus_pb2, nexus_bus_pb2_grpc

class NexusBusApp(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("Nexus Bus"); self.setMinimumSize(600,400)
        self.stub = None; self._ui(); self._connect()
    def _ui(self):
        w=QWidget(); self.setCentralWidget(w); l=QVBoxLayout(w); l.setContentsMargins(20,20,20,20)
        l.addWidget(QLabel("Nexus Bus — Peripheral Access"))
        f=QFrame(); f.setFrameStyle(QFrame.StyledPanel); fl=QFormLayout(f)
        self.type_cb=QComboBox(); self.type_cb.addItems(["GPIO","I2C","SPI","UART","CAN"])
        self.id_sb=QSpinBox(); self.id_sb.setRange(0,7)
        self.addr_sb=QSpinBox(); self.addr_sb.setRange(0,255); self.addr_sb.setPrefix("0x")
        self.reg_sb=QSpinBox(); self.reg_sb.setRange(0,255); self.reg_sb.setPrefix("0x")
        self.val_sb=QSpinBox(); self.val_sb.setRange(0,65535); self.val_sb.setPrefix("0x")
        fl.addRow("Bus Type:",self.type_cb); fl.addRow("Bus ID:",self.id_sb); fl.addRow("Address:",self.addr_sb); fl.addRow("Register:",self.reg_sb); fl.addRow("Value:",self.val_sb)
        l.addWidget(f)
        r=QHBoxLayout()
        self.read_btn=QPushButton("Read"); self.read_btn.clicked.connect(self._read)
        self.write_btn=QPushButton("Write"); self.write_btn.clicked.connect(self._write)
        r.addWidget(self.read_btn); r.addWidget(self.write_btn); l.addLayout(r)
        self.result=QLabel("Result: --"); self.result.setStyleSheet("color:#888;font-size:14px;"); l.addWidget(self.result)
        l.addStretch()
    def _connect(self):
        try:
            ch=grpc.insecure_channel("localhost:50054")
            self.stub=nexus_bus_pb2_grpc.NexusBusStub(ch)
            r=self.stub.HealthCheck(nexus_bus_pb2.HealthRequest(),timeout=2)
            self.result.setText(f"Connected (v{r.version})")
        except: self.result.setText("Disconnected")
    def _read(self):
        if not self.stub: return
        r=self.stub.Read(nexus_bus_pb2.ReadRequest(bus_type=self.type_cb.currentIndex(),bus_id=self.id_sb.value(),addr=self.addr_sb.value(),reg=self.reg_sb.value()),timeout=5)
        self.result.setText(f"Value: 0x{r.value:X}" if r.success else f"Error: {r.error}")
    def _write(self):
        if not self.stub: return
        r=self.stub.Write(nexus_bus_pb2.WriteRequest(bus_type=self.type_cb.currentIndex(),bus_id=self.id_sb.value(),addr=self.addr_sb.value(),reg=self.reg_sb.value(),value=self.val_sb.value()),timeout=5)
        self.result.setText("Write OK" if r.success else f"Error: {r.error}")

app=QApplication(sys.argv); w=NexusBusApp(); w.show(); sys.exit(app.exec())

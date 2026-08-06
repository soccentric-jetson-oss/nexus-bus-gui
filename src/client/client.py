"""Nexus Bus GUI - gRPC client wrapper."""

import grpc
from src.client import nexus_bus_pb2, nexus_bus_pb2_grpc


class NexusBusClient:
    """Thread-safe gRPC client for Nexus Bus server communication."""

    def __init__(self, address: str = "localhost:50054", timeout: float = 2.0):
        self._address = address
        self._timeout = timeout
        self._channel = None
        self._stub = None
        self._connected = False

    @property
    def connected(self) -> bool:
        return self._connected

    def connect(self) -> bool:
        try:
            self._channel = grpc.insecure_channel(self._address)
            self._stub = nexus_bus_pb2_grpc.NexusBusStub(self._channel)
            resp = self._stub.HealthCheck(
                nexus_bus_pb2.HealthRequest(), timeout=self._timeout
            )
            self._connected = resp.status == "SERVING"
        except Exception:
            self._connected = False
        return self._connected

    def read(self, bus_type: int, bus_id: int, addr: int, reg: int) -> dict:
        if not self._stub:
            return {"success": False, "value": 0, "error": "Not connected"}
        try:
            resp = self._stub.Read(
                nexus_bus_pb2.ReadRequest(
                    bus_type=bus_type, bus_id=bus_id, addr=addr, reg=reg
                ),
                timeout=5.0,
            )
            return {"success": resp.success, "value": resp.value, "error": resp.error}
        except Exception as e:
            return {"success": False, "value": 0, "error": str(e)}

    def write(self, bus_type: int, bus_id: int, addr: int, reg: int, value: int) -> dict:
        if not self._stub:
            return {"success": False, "error": "Not connected"}
        try:
            resp = self._stub.Write(
                nexus_bus_pb2.WriteRequest(
                    bus_type=bus_type, bus_id=bus_id,
                    addr=addr, reg=reg, value=value
                ),
                timeout=5.0,
            )
            return {"success": resp.success, "error": resp.error}
        except Exception as e:
            return {"success": False, "error": str(e)}

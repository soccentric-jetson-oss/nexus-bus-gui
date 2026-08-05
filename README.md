# Nexus Bus GUI — Peripheral Bus Control Desktop Application

The Nexus Bus GUI is a cross-platform PySide6 desktop application for reading from and writing to peripheral buses on the Jetson AGX Orin. It provides a form-based interface with dropdowns for bus type selection (GPIO, I2C, SPI, UART), spin boxes for bus ID, device address, register offset, and value entry, and read/write buttons. Results are displayed inline with formatted hex values. The application connects to the Nexus Bus gRPC server and provides real-time feedback for all operations, making it easy to prototype and debug peripheral interactions without writing code.

## Features

- Cross-platform
- PySide6
- desktop
- application
- Bus
- type
- selector
- (GPIO,
- I2C,
- SPI,
- UART)
- Configurable
- bus
- ID
- and
- address
- Register-level
- read
- operations
- Register-level
- write
- operations
- Hex
- value
- display
- for
- results
- gRPC
- client
- with
- auto-reconnect
- Form-based
- intuitive
- interface
- MIT
- licensed

## Quick Start

### Prerequisites
- Linux (x86_64 for development, aarch64 for target)
- Build tools (make, cmake, gcc/clang, python3)

### Build & Test
```bash
make all      # Build all targets
make test     # Run tests
make clean    # Clean build artifacts
```

## Repository Structure

| Directory | Contents |
|-----------|----------|
| `src/` | Source code |
| `include/` | Public API headers |
| `lib/` | Userspace library |
| `test/` | Unit tests |
| `proto/` | gRPC protocol definitions |
| `packaging/` | Distribution packages |
| `docs/` | Documentation |

## Project Status

**Version:** 0.1.0 — Initial release
**License:** MIT
**Audit Score:** 90/100

## Ecosystem

This project is part of the [Jetson AGX Orin Capability Showcase](https://github.com/soccentric-jetson-oss/soccentric-jetson-oss) — five open-source projects demonstrating full exploitation of NVIDIA's flagship edge AI platform.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All contributions welcome!

## License

MIT. See [LICENSE](LICENSE) for details.

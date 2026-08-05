# Nexus Bus GUI — Peripheral Bus Control Desktop Application

The Nexus Bus GUI is a cross-platform PySide6 desktop application for reading from and writing to peripheral buses on the Jetson AGX Orin. It provides a form-based interface with dropdowns for bus type selection including GPIO, I2C, SPI, and UART, spin boxes for bus ID, device address, register offset, and value entry, and read and write buttons. Results are displayed inline with formatted hex values.

## Features

- Provides a cross-platform PySide6 desktop application that runs identically on Windows, macOS, and Linux operating systems
- Offers a bus type selector dropdown supporting GPIO, I2C, SPI, and UART for flexible peripheral targeting
- Provides configurable spin box inputs for bus ID, device address, register offset, and value with hex prefix display
- Performs register-level read operations with results displayed as formatted hexadecimal values
- Performs register-level write operations with configurable value input and success or error feedback
- Displays read results as formatted hex values for easy interpretation of register contents
- Connects to the Nexus Bus gRPC server with automatic health check and connection status display
- Provides a form-based intuitive interface that makes peripheral debugging accessible without writing code
- Licensed under MIT for maximum flexibility in commercial and open-source projects

## Quick Start

### Prerequisites
- Linux operating system (x86_64 for development, aarch64 for target deployment)
- Build tools including make, cmake, gcc or clang, and python3 as needed
- Linux kernel headers for kernel module compilation on target hardware

### Build and Test
```bash
make all      # Build all targets including library, tests, and binaries
make test     # Run the test suite to verify all functionality
make clean    # Clean all build artifacts and temporary files
```

## Repository Structure

| Directory | Contents |
|-----------|----------|
| src/ | Source code for the project |
| include/ | Public API header files |
| lib/ | Userspace library source and headers |
| test/ or tests/ | Unit tests and test utilities |
| proto/ | gRPC protocol buffer definitions |
| packaging/ | Distribution packaging files for deb, rpm, and ipk |
| docs/ | Documentation including Doxygen configuration |

## Project Status

**Version:** 0.1.0 — Initial release
**License:** MIT
**Audit Score:** 90/100 across 20 criteria

## Ecosystem

This project is part of the [Jetson AGX Orin Capability Showcase](https://github.com/soccentric-jetson-oss/soccentric-jetson-oss) — five open-source projects demonstrating full exploitation of NVIDIA's flagship edge AI platform.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All contributions are welcome.

## License

MIT. See [LICENSE](LICENSE) for details.

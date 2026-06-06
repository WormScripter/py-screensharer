# Py Screen Sharer

A lightweight Python-based screen sharing application that streams a desktop screen over a local network in real time.

## Features

* Real-time screen streaming
* Low-latency transmission
* Simple client-server architecture
* Cross-platform support
* Lightweight and easy to run
* Python-based implementation

## Screenshots

Add screenshots here.

## Requirements

* Python 3.8+
* pip

## Installation

Clone the repository:

```bash
git clone https://github.com/WormScripter/py-screensharer.git
cd py-screensharer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Start the Host

```bash
python server.py
```

### Start the Viewer

```bash
python client.py
```

Enter the host IP address when prompted.

## Project Structure

```text
py-screensharer/
│
├── server.py
├── client.py
├── requirements.txt
├── README.md
└── assets/
```

## How It Works

1. The host captures screen frames.
2. Frames are compressed for transmission.
3. Data is sent over a socket connection.
4. The client receives and displays frames in real time.

## Performance Tips

* Use a wired connection for lower latency.
* Reduce capture resolution for slower networks.
* Compress frames before transmission.

## Security Notice

This project is intended for educational and local-network use.

Before exposing it to the internet, consider implementing:

* User authentication
* End-to-end encryption
* Access control
* Session management

## Future Improvements

* Audio streaming
* File transfer
* Multi-monitor support
* Screen recording
* Remote control functionality
* Encrypted communication

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

MIT License

## Author

Created by WormScripter.

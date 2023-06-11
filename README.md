# Image Background Removal with Flask

This is a Flask project that allows you to remove the background of an uploaded image and convert it to a transparent PNG format. It utilizes Docker to ensure easy setup and deployment.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload an image and remove its background.
- Convert the image to a transparent PNG format.
- Visualize the original and modified images side by side.

## Prerequisites

Make sure you have the following dependencies installed:

- Docker: [https://www.docker.com](https://www.docker.com)

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/idylmz/bgremover.git
cd bgremover
```

2. Build the Docker image:

```
docker-compose build
```

## Usage

1. Start the Docker container:

```
docker-compose up -d
```

2. Open your web browser and visit [http://localhost:8000](http://localhost:8000).

3. Upload an image and click the "Remove Background" button.

4. The modified image with a transparent background will be displayed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

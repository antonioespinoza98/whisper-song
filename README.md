# Whisper AI to transcribe song lyrics

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

Instructions on how to install and set up the project.

To install the required environment using Conda and the provided `environment.yml` file, run:

```bash
conda env create -f environment.yml
```
## Usage
The application is structured around two primary files:

- **core.py**: Contains the `transcribe` function, which uses OpenAI's Whisper model to transcribe audio files into text. This script handles the audio processing and communicates with the Whisper API to perform the transcription.

- **webservice.py**: Implements a web service using FastAPI. It defines the `/asr` endpoint that accepts audio file uploads. Upon receiving a file, it calls the `transcribe` function from `core.py` to process the audio and returns the transcribed text.

- **file_processing.ipynb**: Downloads audio from YouTube, isolates vocals from the background acoustics, and reduces noise for enhanced clarity of the singer's voice.

To run the application using Docker and Docker Compose, follow these steps:

1. **Build and start the Docker containers**:

    ```bash
    docker-compose up --build
    ```

    This command builds the Docker image defined in the `Dockerfile` and starts the services specified in `docker-compose.yml`.

2. **Access the Swagger UI interface**:

    Open your web browser and navigate to `http://localhost:9000/docs`. This will load the Swagger UI where you can interact with the API.

3. **Upload an audio file for transcription**:

    In the Swagger UI, use the `/asr` endpoint to upload your audio file. The application will process the file using OpenAI's Whisper model and return the transcribed song lyrics.

**Prerequisites**:

- Ensure Docker and Docker Compose are installed on your system.
- The application listens on port `9000` by default; make sure this port is available.


## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. **Fork the repository** to your GitHub account.

2. **Clone your forked repository** to your local machine:

    ```bash
    git clone https://github.com/your-username/whisper-song.git
    ```

3. **Create a new branch** for your feature or bug fix:

    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Make your changes** and **commit** them:

    ```bash
    git commit -m "Add your descriptive commit message"
    ```

5. **Push your changes** to GitHub:

    ```bash
    git push origin feature/your-feature-name
    ```

6. **Submit a pull request** to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

if you have questions or suggestions, please reach out to my e-mail: espinozamarco70@gmail.com!
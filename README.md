# VISION-PLAY : Advanced Motion & Team Analysis

## 🔎 Project Overview

**Vision-Play** is a sophisticated computer vision system designed for real-time tracking and analysis of sports videos. Leveraging state-of-the-art object detection with YOLO and image processing with OpenCV, this platform extracts valuable insights from video footage including player movements, ball trajectory, team assignments, and camera motion compensation.

The system converts video inputs into actionable sports analytics, enabling coaches, analysts, and broadcasters to gain deeper understanding of gameplay dynamics and player performance metrics.

## 🚀 Key Features

- **Advanced Object Detection**: Precisely identify players, referees, balls, and other relevant objects using custom-trained YOLO models
- **Player-Ball Assignment**: Automatically determine which player is in possession or closest to the ball at any given moment
- **Camera Movement Compensation**: Intelligently track and correct for camera panning, zooming, and movement
- **Real-World Coordinate Mapping**: Transform pixel coordinates into meaningful field/court positions
- **Performance Metrics**: Calculate and visualize critical metrics including:
  - Player speed and acceleration
  - Distance covered by players
  - Time in possession
  - Team formation analysis
- **Multi-Sport Support**: Adaptable architecture designed to work across different sports with minimal reconfiguration
- **Real-Time Processing Pipeline**: Optimized for efficient processing with support for both recorded and live video feeds

## 📊 Example Applications

- **Tactical Analysis**: Review team formations and player positioning
- **Performance Evaluation**: Track player movement patterns and physical exertion
- **Automated Highlights**: Identify key moments based on player-ball interactions
- **Broadcasting Enhancement**: Generate real-time statistics for viewers
- **Training Optimization**: Analyze practice sessions for technique improvement

## 📂 Project Structure

```
Vision-Play/
├── camera_movement_estimator/    # Camera motion tracking and compensation
├── development_and_analysis/     # Tools for project development and testing
├── Input-Videos/                 # Source videos for processing (not included in repo)
├── models/                       # Pre-trained neural network models
├── Output-Videos/                # Processed videos with visualizations
├── player_ball_assigner/         # Logic for determining ball possession
├── runs/                         # Experiment logs and results
├── speed_and_distance_estimator/ # Calculation of movement metrics
├── stubs/                        # Interface definitions and mock implementations
├── team_assigner/                # Team classification algorithms
├── trackers/                     # Object tracking implementations
├── training/                     # Model training scripts and utilities
├── utils/                        # Common utility functions
├── venv/                         # Virtual environment (not tracked)
├── view_transformer/             # Coordinate system transformation
├── .gitignore                    # Git ignore configuration
├── main.py                       # Application entry point
├── requirements.txt              # Project dependencies
├── yolo_inference.py             # YOLO model inference implementation
└── yolov8m.pt                    # YOLO model weights
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.7 or higher
- CUDA-compatible GPU (recommended for real-time processing)
- FFmpeg (for video processing)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Vision-Play.git
cd Vision-Play
```

### Step 2: Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download Model Weights

Download the required YOLO model weights from the release page or train your own models following the instructions in the `training/` directory.

```bash
# Example for downloading pre-trained weights (if available)
wget https://github.com/your-username/Vision-Play/releases/download/v1.0/yolov8m.pt -O yolov8m.pt
```

### Step 5: Prepare Input Videos

Place your source videos in the `Input-Videos/` directory or specify custom paths when running the application.

## 🎮 Usage

### Basic Usage

Process a video file and generate analysis:

```bash
python main.py --input Input-Videos/match.mp4 --output Output-Videos/analyzed_match.mp4
```

### Advanced Options

```bash
python main.py --input Input-Videos/match.mp4 \
               --output Output-Videos/analyzed_match.mp4 \
               --model models/custom_sport.pt \
               --conf 0.5 \
               --view-transform field_template.json \
               --track-players \
               --track-ball \
               --calculate-metrics
```

### Configuration

Customize the system behavior by modifying the configuration files in the project directories or by providing command-line arguments.

## 📈 Performance Optimization

For optimal performance:

- Use a GPU with CUDA support
- Adjust model size based on your hardware capabilities
- Reduce input video resolution for faster processing
- Use the `--skip-frames` option for non-critical applications

## 🧪 Development and Testing

The `development_and_analysis/` directory contains tools for:

- Model evaluation and benchmarking
- Performance profiling
- Test data generation
- Visualization debugging

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Documentation (will be added)

Comprehensive documentation is available in the `docs/` directory, covering:

- API references
- Algorithm explanations
- Integration guides
- Model training procedures

## 📧 Contact

For questions, support, or collaboration opportunities:

- Email: kushagraagrawal128@gmail.com
- Issue Tracker: [GitHub Issues](https://github.com/DS-Kushagra/Vision-Play/issues)

## Acknowledgements

- [Ultralytics](https://github.com/ultralytics/yolov5) for the YOLO implementation
- [OpenCV](https://opencv.org/) for computer vision utilities
- [PyTorch](https://pytorch.org/) for deep learning framework
- Sports video datasets providers for training data

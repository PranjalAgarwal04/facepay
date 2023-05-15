# FacePay

![FacePay](./assets/images/facepay.png?raw=true "FacePay")

FacePay is a secure and convenient payment authorization solution that utilizes facial recognition technology. It allows users to authenticate and authorize their digital transactions by simply scanning their face through a device's camera. The app captures and analyzes unique facial features to verify the user's identity, providing an additional layer of security and eliminating the need for traditional authentication methods like passwords or PINs. By leveraging advanced biometric technology, the app enhances user experience, streamlines the payment process, and mitigates the risk of fraudulent activities. With its seamless integration into various industries, cross-platform compatibility, and potential for continuous improvement, the app offers a future-ready solution for secure and efficient payment authorization using facial recognition.

## Flowchart

![Flowchart](./assets/images/flowchart.png?raw=true "Flowchart")

## Installation

- Fork and clone the [repository](https://github.com/PranjalAgarwal04/facepay)

```bash
git clone <repo-url>
```

- Navigate to the project directory

```bash
cd facepay
```

- Create a virtual environment

```bash
python -m venv venv
```

- Activate the virtual environment

```bash
./venv/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Download the [dataset](http://vis-www.cs.umass.edu/lfw/#download) in `.tgz` and put in the `facepay` directory

## Usage

- Run the `script.ipynb` notebook to generate the dataset
- Press `a` to collect anchor images
- Press `p` to collect positive images
- Press `q` to quit
- Collect < 300 images for each.

- Run `capture.py` to capture images for testing

```bash
python capture.py
```

- Press `c` to capture images
- Press `q` to quit

- Copy `model` folder from `facepay` to `app` directory

- Navigate to the `app` directory

```bash
cd app
```

- Run the app

```bash
python app.py
```

## Results

### Dataset Generation

![Dataset Generation](./assets/images/dataset-generation.png?raw=true "Dataset Generation")

### Embedding Summary

![Embedding Summary](./assets/images/embedding-summary.png?raw=true "Embedding Summary")

### Model Summary

![Model Summary](./assets/images/model-summary.png?raw=true "Model Summary")

### Model Training

![Model Training](./assets/images/model-training.png?raw=true "Model Training")

### Model Results

![Model Results](./assets/images/model-results.png?raw=true "Model Results")

### Model Testing

![Model Testing](./assets/images/model-testing.png?raw=true "Model Testing")

### App Testing

![App Testing](./assets/images/app-testing.png?raw=true "App Testing")

## Resources

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Dataset](http://vis-www.cs.umass.edu/lfw)
- [Research Paper](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)
- [Kivy](https://kivy.org/)

## Status

- [x] Dataset Generation
- [x] Model Training
- [x] Model Testing
- [ ] Web App Development
- [ ] Web App Testing
- [ ] Web App Deployment

## Author

[Pranjal Agarwal](https://github.com/PranjalAgarwal04)

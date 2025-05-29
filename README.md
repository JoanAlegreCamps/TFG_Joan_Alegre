# mtDNA-aging-pipeline

This repository contains the code and macros developed for a Bachelor's Thesis project on analyzing mitochondrial DNA (mtDNA) dynamics during replicative aging in *Saccharomyces cerevisiae*. The project combines long-term fluorescence microscopy in microfluidic devices with semi-automated image processing.

## 🔍 Overview

The main goal is to extract and analyze fluorescence intensity from mitochondrial membranes and mtDNA in single yeast cells over time. This analysis was initially performed manually in Fiji but has been progressively optimized using macros and Python scripts.

## 📁 Repository Structure
mtDNA-aging-pipeline/
├── src/ # Python scripts
│ ├── background_subtraction.py
│ └── fluorescence_quantification.py
├── macros/ # Fiji macros
│ ├── track_cell_macro.ijm
│ ├── measure_intensity_over_time.ijm
│ └── measure_all_rois_over_time.ijm
├── example_data/ # Example .tif and .xlsx files (if provided)
├── requirements.txt
└── README.md

## ⚙️ Installation

### Prerequisites

- Python 3.8+
- [Fiji / ImageJ](https://imagej.net/software/fiji/)
- Git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mtDNA-aging-pipeline.git
cd mtDNA-aging-pipeline
exit
2. Install dependencies:
pip install -r requirements.txt

3. Open Fiji and run the macros from the macros/ folder via:
Plugins > Macros > Run...


**Example Usage**

1. Subtract background from multi-channel .tif
python src/background_subtraction.py
This script loads a .tif file, subtracts a background value from green and red channels, and saves the corrected image.

2. Track a single ROI with Fiji
Use the track_cell_macro.ijm macro to:

Measure fluorescence in green and red channels (channels 2 and 3).

Track intensity of one ROI through all frames.

3. Measure ROI over time
Use measure_intensity_over_time.ijm to:

Measure the selected ROI in each timepoint (e.g., over 90 frames).

Use measure_all_rois_over_time.ijm to:

Automatically loop over all saved ROIs and extract intensity values frame-by-frame.

4. Clean up and separate fluorescence measurements (Python)
python src/fluorescence_quantification.py
This script processes the raw .xlsx file exported from Fiji, separates values into green/red channels (based on even/odd rows), and saves a clean version of the dataset.


















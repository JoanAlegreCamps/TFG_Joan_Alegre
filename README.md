# TFG_Joan_Alegre -> mtDNA-aging-pipeline

This repository contains the code developed for a Bachelor's Thesis project focused on analyzing mitochondrial DNA (mtDNA) dynamics during replicative aging in *Saccharomyces cerevisiae*. The workflow combines microfluidic time-lapse fluorescence microscopy with semi-automated image processing and quantification tools.

## Project Overview

The main objective of this project was to build a reproducible, semi-automated analysis pipeline that simplifies the quantification of mitochondrial and mtDNA fluorescence over time in individual yeast cells. The tools developed here are intended to support future biological studies on mitochondrial inheritance, aging, and cell cycle dynamics.

The project includes:
- Python scripts for background subtraction and fluorescence data processing.
- Fiji macros for semi-manual cell tracking and measurement.
- Integration with Cell-ACDC for segmentation and tracking based on the BABY model.

## Installation Requirements

### Prerequisites

- Python 3.8 or higher  
- Fiji/ImageJ (https://imagej.net/software/fiji/)  
- Git  

### Installing the pipeline

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mtDNA-aging-pipeline.git
cd mtDNA-aging-pipeline

###
**Manual tracking with Fiji (macro)**
To manually extract fluorescence intensity from mother cells across time:

1. Open your time-lapse .tif file in Fiji.
2. Use the ROI Tool to draw a selection around the cell.
3. Run the macro macros/track_cell_macro.ijm (from Plugins > Macros > Run).
      This will automatically measure green (channel 2) and red (channel 3) fluorescence for the selected ROI across all frames.
4. Measurements will appear in the Results window and can be exported to .csv or .xlsx.

# Multi-Omics Analysis of Colon Cancer using Variational Autoencoders

This project implements an integrated multi-omics analysis framework for TCGA colon cancer data using variational autoencoders (VAE) and Maximum Mean Discrepancy VAE (MMD-VAE), based on the architecture described in [Hira et al. (2021)](https://www.nature.com/articles/s41598-021-85285-4).

## Overview

The project performs comprehensive multi-omics analysis of colon cancer data by:
1. **Dimensionality reduction** using VAE and MMD-VAE to compress high-dimensional omics features
2. **Cancer sample identification** 
3. **Molecular subtype classification** and clustering
4. **Survival analysis** for prognosis

### Key Features

- **Mono-omics analysis**: Individual analysis of genomics, transcriptomics, epigenomics, and proteomics data
- **Integrated multi-omics**: Combined analysis of di-omics and tri-omics data
- **Deep learning architecture**: VAE and MMD-VAE for compressed feature learning
- **Clinical applications**: Classification, clustering, and survival prediction

## Paper Reference

Hira, M.T., Razzaque, M.A., Angione, C. et al. Integrated multi-omics analysis of ovarian cancer using variational autoencoders. *Sci Rep* **11**, 6265 (2021). https://doi.org/10.1038/s41598-021-85285-4

## Architecture

The project implements two main architectures:

1. **Variational Autoencoder (VAE)**: Standard VAE for compressed feature learning
2. **MMD-VAE**: Improved version that addresses variance over-estimation issues in feature space

Both architectures include:
- Encoder network for dimensionality reduction
- Latent space representation
- Decoder network for reconstruction
- Supervised components for downstream tasks

## Requirements

```bash
# Python 3.8 or higher
# Required packages listed in requirements.txt
```

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd Multiomics-coloncancer

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Data

The project uses TCGA Colon Adenocarcinoma (COAD) data including:
- **Genomics**: DNA mutation data
- **Transcriptomics**: RNA-seq gene expression data
- **Epigenomics**: DNA methylation data
- **Clinical data**: Patient survival and subtype information

Data can be downloaded from:
- [GDC Data Portal](https://portal.gdc.cancer.gov/)
- [cBioPortal](https://www.cbioportal.org/)

## Usage

### Data Preprocessing

```bash
# Preprocess TCGA colon cancer data
python scripts/preprocess_data.py --input data/raw --output data/processed
```

### Training VAE/MMD-VAE Models

```bash
# Train VAE model
python train_vae.py --omics rna --latent_dim 64 --epochs 100

# Train MMD-VAE model
python train_mmd_vae.py --omics rna methylation --latent_dim 128 --epochs 100

# Integrated multi-omics training
python train_integrated.py --omics rna methylation protein --latent_dim 256
```

### Evaluation

```bash
# Run classification
python evaluate.py --model saved_models/vae_model.pth --task classification

# Run survival analysis
python evaluate.py --model saved_models/mmd_vae_model.pth --task survival

# Generate plots and metrics
python visualize_results.py --results results/ --output figures/
```

## Project Structure

```
Multiomics-coloncancer/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/          # Raw TCGA data
│   └── processed/     # Preprocessed data
├── src/
│   ├── models/        # VAE and MMD-VAE architectures
│   ├── data_loader.py # Data loading utilities
│   ├── trainer.py     # Training scripts
│   └── utils.py       # Utility functions
├── scripts/           # Data preprocessing scripts
├── notebooks/         # Jupyter notebooks for exploration
├── results/           # Saved results and metrics
└── figures/           # Generated plots and visualizations
```

## Results

Expected performance metrics (based on the original paper applied to colon cancer):

- **Classification Accuracy**: 
  - VAE: ~87-95%
  - MMD-VAE: ~93-96%
  
- **Survival Analysis**: 
  - Concordance index for survival prediction
  - Kaplan-Meier curves for survival analysis

## Development

### Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this code in your research, please cite:

```bibtex
@article{hira2021integrated,
  title={Integrated multi-omics analysis of ovarian cancer using variational autoencoders},
  author={Hira, Muta Tah and Razzaque, M A and Angione, Claudio and others},
  journal={Scientific Reports},
  volume={11},
  number={6265},
  year={2021},
  publisher={Nature Publishing Group}
}
```

## Contact

For questions or issues, please open an issue on GitHub or contact the maintainers.

## Acknowledgments

This project is based on the work by Hira et al. (2021) and applies their methodology to colon cancer analysis.


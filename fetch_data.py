import os
import requests
import gzip
import shutil

# Create directory
os.makedirs('data/raw/COAD', exist_ok=True)

# Selected datasets matching the paper
datasets = {
    'cnv': {
        'url': 'https://tcga.xenahubs.net/download/TCGA.COAD.sampleMap/Gistic2_CopyNumber_Gistic2_all_data_by_genes.gz',
        'description': 'Gene-level CNV (GISTIC2)'
    },
    'methylation': {
        'url': 'https://tcga.xenahubs.net/download/TCGA.COAD.sampleMap/HumanMethylation27.gz',
        'description': 'DNA Methylation 27k'
    },
    'rnaseq': {
        'url': 'https://tcga.xenahubs.net/download/TCGA.COAD.sampleMap/HiSeqV2.gz',
        'description': 'Gene Expression RNA-seq (HiSeqV2)'
    },
    'clinical': {
        'url': 'https://tcga.xenahubs.net/download/TCGA.COAD.sampleMap/COAD_clinicalMatrix.gz',
        'description': 'Clinical data'
    }
}

def download_and_extract(name, info):
    """Download and extract dataset"""
    gz_path = f'data/raw/COAD/{name}.tsv.gz'
    tsv_path = f'data/raw/COAD/{name}.tsv'
    
    if os.path.exists(tsv_path):
        print(f"✓ {info['description']} already exists")
        return
    
    print(f"\nDownloading {info['description']}...")
    print(f"URL: {info['url']}")
    
    response = requests.get(info['url'], stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(gz_path, 'wb') as f:
        downloaded = 0
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            downloaded += len(chunk)
            if total_size > 0:
                print(f"\rProgress: {(downloaded/total_size)*100:.1f}%", end='')
    
    print("\n✓ Download complete!")
    print("Extracting...")
    
    with gzip.open(gz_path, 'rb') as f_in:
        with open(tsv_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    os.remove(gz_path)
    print("✓ Extraction complete!")

# Download all datasets
for name, info in datasets.items():
    download_and_extract(name, info)

print("\n" + "="*50)
print("All datasets downloaded successfully!")
print("="*50)
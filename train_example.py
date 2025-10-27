"""
Example training script for VAE/MMD-VAE models
"""

import torch
import torch.optim as optim
import argparse
from src.models.vae import VAE
from src.models.mmd_vae import MMDVAE
from src.data_loader import MultiOmicsDataLoader


def train_vae(model, train_loader, epochs=100, lr=0.001):
    """Train VAE model."""
    optimizer = optim.Adam(model.parameters(), lr=lr)
    model.train()
    
    for epoch in range(epochs):
        total_loss = 0
        recon_loss_total = 0
        kl_loss_total = 0
        
        for batch_idx, data in enumerate(train_loader):
            optimizer.zero_grad()
            
            # Forward pass
            recon_batch, mu, logvar = model(data)
            
            # Loss computation
            recon_loss = F.mse_loss(recon_batch, data, reduction='sum')
            kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
            loss = recon_loss + kl_loss
            
            # Backward pass
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            recon_loss_total += recon_loss.item()
            kl_loss_total += kl_loss.item()
        
        avg_loss = total_loss / len(train_loader.dataset)
        print(f'Epoch {epoch}, Loss: {avg_loss:.4f}, '
              f'Recon: {recon_loss_total/len(train_loader.dataset):.4f}, '
              f'KL: {kl_loss_total/len(train_loader.dataset):.4f}')


def main():
    parser = argparse.ArgumentParser(description='Train VAE/MMD-VAE for multi-omics data')
    parser.add_argument('--model', type=str, choices=['vae', 'mmd_vae'], 
                       default='vae', help='Model type')
    parser.add_argument('--omics', type=str, nargs='+', 
                       default=['rna'], help='Omics types to use')
    parser.add_argument('--latent_dim', type=int, default=64, 
                       help='Latent dimension')
    parser.add_argument('--epochs', type=int, default=100, 
                       help='Number of epochs')
    parser.add_argument('--batch_size', type=int, default=32, 
                       help='Batch size')
    parser.add_argument('--lr', type=float, default=0.001, 
                       help='Learning rate')
    
    args = parser.parse_args()
    
    # Load data
    loader = MultiOmicsDataLoader()
    data_list = loader.load_omics_data(args.omics)
    
    # TODO: Prepare train_loader from data
    # train_loader = ...
    
    # Initialize model
    input_dim = data_list[0].shape[1]  # Example
    if args.model == 'vae':
        model = VAE(input_dim, args.latent_dim)
    else:
        model = MMDVAE(input_dim, args.latent_dim)
    
    # Train model
    if args.model == 'vae':
        train_vae(model, train_loader, args.epochs, args.lr)
    else:
        # TODO: Implement MMD-VAE training
        pass
    
    # Save model
    torch.save(model.state_dict(), f'models/{args.model}_colon_cancer.pth')


if __name__ == '__main__':
    main()


from torch.utils.data import DataLoader
from modeling import Bert, BertConfig
from dataloader import get_dataloader
from torch.optim import AdamW
import torch.nn as nn
import torch

# -----------------------
# Hyperparameters
# -----------------------
# TODO: set data path
TRAIN_DATA_PATH = None
VAL_DATA_PATH = None

# TODO: set batch size
BATCH_SIZE = None

# TODO: set number of epochs
EPOCHS = None

# TODO: set learning rate
LR = None

# TODO: set maximum sequence length
MAX_LEN = None

# Device
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -----------------------
# Tokenizer
# -----------------------
# TODO: initialize tokenizer
tokenizer = None

# -----------------------
# DataLoaders
# -----------------------
# TODO: create train DataLoader
train_loader = None

# TODO: create validation DataLoader
val_loader = None

# -----------------------
# Model
# -----------------------
# TODO: create BertConfig and Bert model
config = None
model = None
model.to(DEVICE)

# -----------------------
# Loss and Optimizer
# -----------------------
# TODO: define loss function
criterion = None

# TODO: define optimizer
optimizer = None

# -----------------------
# Training steps
# -----------------------
# TODO: write training loop
# For each epoch:
#   - iterate over train_loader
#       - get batch
#       - forward pass
#       - compute loss
#       - backward pass
#       - optimizer step
#   - iterate over val_loader
#       - get batch
#       - forward pass
#       - compute validation loss / accuracy

# -----------------------
# Save model checkpoint
# -----------------------
# TODO: save model state_dict
# torch.save(model.state_dict(), "bert_classifier.pth")

# -----------------------
# Save loss and accuracy plots
# -----------------------
# TODO: plot train_losses, val_losses in 'loss.png'
# TODO: plot train_accuracies, val_accuracies in 'acc.png'
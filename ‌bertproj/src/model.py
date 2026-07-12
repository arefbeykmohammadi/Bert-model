from torch import nn
import torch

class Embedding(nn.Module):
    def __init__(self) -> None:
        super(Embedding, self).__init__()
        # Token + Position embeddings

    def forward(self):
        # Return embeddings for input tokens
        pass

class FeedForward(nn.Module):
    def __init__(self) -> None:
        super(FeedForward, self).__init__()
        # Two-layer FFN with activation

    def forward(self):
        # Apply FFN to input
        pass

class Attention(nn.Module):
    def __init__(self) -> None:
        super(Attention, self).__init__()
        # Multi-head self-attention

    def forward(self):
        # Compute attention output
        pass

class EncoderLayer(nn.Module):
    def __init__(self) -> None:
        super(EncoderLayer, self).__init__()
        # Attention + FFN + residual + layernorm

    def forward(self):
        # One encoder layer forward
        pass

class Encoder(nn.Module):
    def __init__(self) -> None:
        super(Encoder, self).__init__()
        # Stack of EncoderLayers

    def forward(self):
        # Return final hidden states
        pass

class BertConfig:
    def __init__(self):
        # TODO: set vocabulary size
        self.vocab_size = None

        # TODO: set hidden size of embeddings and model
        self.hidden_dim = None

        # TODO: set number of attention heads
        self.num_heads = None

        # TODO: set number of encoder layers
        self.num_layers = None

        # TODO: set feedforward hidden size
        self.ffn_dim = None

        # TODO: set maximum sequence length
        self.max_len = None

        # TODO: set number of output classes
        self.num_classes = None

        # TODO: set dropout rate
        self.dropout = None

class Bert(nn.Module):
    def __init__(self, config : BertConfig) -> None:
        super(Bert, self).__init__()
        # Embedding + Encoder + classification head

    def forward(self):
        # Return logits for classification
        pass
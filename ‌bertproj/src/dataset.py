from torch.utils.data import Dataset, DataLoader
import torch

class TextDataset(Dataset):
    def __init__(self, data_path, tokenizer, max_len):
        """
        Args:
            data_path (str): path to dataset file
            tokenizer: tokenizer object
            max_len (int): maximum sequence length
        """
        # TODO: load texts and labels from data_path
        self.texts = None
        self.labels = None
        self.tokenizer = ...
        self.max_len = ...

    def __len__(self):
        # TODO: return dataset length
        return 0

    def __getitem__(self, idx):
        # TODO: tokenize self.texts[idx]
        # input_ids = ...
        # TODO: pad/truncate to max_len
        # TODO: create attention_mask (1 for real tokens, 0 for padding)
        input_ids = None
        attention_mask = None

        # TODO: prepare label tensor
        label = None

        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'label': label
        }

def get_dataloader(
    data_path : str,
    tokenizer,
    batch_size : int = 32,
    max_len : int = 128,
    shuffle : bool = True
):
    """
    Create DataLoader for training or evaluation
    """
    dataset = TextDataset(
        data_path,
        tokenizer,
        max_len
    )
    return DataLoader(
        dataset,
        batch_size = batch_size,
        shuffle = shuffle
    )
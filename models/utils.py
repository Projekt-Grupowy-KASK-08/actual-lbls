import numpy as np
import torch
from torch._C import dtype


class CreateTensors(object):
    """Convert ndarrays in sample to Tensors."""

    def __init__(self, num_of_class: int = 6):
        self.class_num = num_of_class

    def __call__(self, sample):
        activity, label = sample["activity"], sample["label"]
        return {
            "activity": torch.from_numpy(activity).type(torch.FloatTensor),
            "label": torch.tensor(label),
        }


class PadActivity(object):
    def __init__(self, input_size: int = 10000):
        self.input_size = input_size

    def __call__(self, sample):
        activity, label = sample["activity"], sample["label"]
        activity = np.pad(activity, (self.input_size - activity.shape[0]))
        return {"activity": activity, "label": label}


class FFT(object):
    def __init__(self, output_size):
        pass

    def __call__(self, sample):
        pass

from __future__ import print_function, division
import os
from pandas.core import frame
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset


class NeuralActivityDataset(Dataset):
    def __init__(self, dataset_path, transforms=None, sample_length=10000):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.activity_frame = pd.read_csv(os.path.join(dataset_path, "metadata.csv"))
        self.dataset = dataset_path
        self.transforms = transforms
        self.sample_length = sample_length
        self.data = []
        self.class_num = 2
        size = self.activity_frame.size
        for idx in range(len(self.activity_frame)):
            activity_name = os.path.join(self.dataset, self.activity_frame.iloc[idx, 0])
            activity = np.load(activity_name)
            label = self.activity_frame.iloc[idx, 1]

            for index in range(0, len(activity), self.sample_length):
                if index + self.sample_length > len(activity):
                    padding = np.zeros(self.sample_length - (len(activity) - index))
                    fragment = np.concatenate(
                        (activity[index : len(activity)], padding)
                    )
                    self.data.append({"label": label, "activity": fragment})
                else:
                    self.data.append(
                        {
                            "label": label,
                            "activity": activity[index : index + self.sample_length],
                        }
                    )

    def __len__(self):
        """
        Returns length of dataset.
        """
        return len(self.data)

    def __getitem__(self, idx):
        """
        Allows to iterate through dataset.
        """
        print(idx)
        if torch.is_tensor(idx):
            idx = idx.tolist()
        sample = self.data[idx]
        print(sample)
        if self.transforms:
            sample = self.transforms(sample)
        return sample["activity"], sample["label"]


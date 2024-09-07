from neural_activity_dataset import NeuralActivityDataset
from neural_network_models import LSTMModel
from torchvision import transforms
from utils import CreateTensors
import pytorch_lightning as pl
from torch.utils.data import DataLoader
from torch.utils.data.dataset import random_split
import torch
from pytorch_lightning import loggers as pl_loggers

# from clearml import Task
# task = Task.init(project_name="sequential-data-clasification", task_name="pytorch lightning")
# Add transforms which should be run on dataset
transforms_set = [CreateTensors()]
transform_pipeline = transforms.Compose(transforms_set)
dataset = NeuralActivityDataset(
    dataset_path="/home/konrad/git/sequential_data_classification/MER_dataset",
    transforms=transform_pipeline,
    sample_length=10000
)
# Split dataset into validation and train
train_size = int(0.9 * len(dataset))
val_size = len(dataset) - int(0.95 * len(dataset))
test_size = len(dataset) - train_size - val_size
train_data, val_data, test_data = random_split(
    dataset,
    [train_size, val_size, test_size],
    generator=torch.Generator().manual_seed(42),
)
# Init data loaders
train_loader = DataLoader(train_data, batch_size=1)
test_loader = DataLoader(test_data, batch_size=1)
val_loader = DataLoader(val_data, batch_size=1)
# Init model
model = LSTMModel(
    input_dim=1, output_dim=6, hidden_dim=1, layer_dim=3, dropout_prob=0.1
)
model.summarize(mode="full")
# create logger
tb_logger = pl_loggers.TensorBoardLogger("logs/")
# train
trainer = pl.Trainer(logger=tb_logger, max_epochs=10, log_every_n_steps=5)
trainer.fit(model, train_loader, val_loader)
# validation
trainer.test(dataloaders=test_loader)

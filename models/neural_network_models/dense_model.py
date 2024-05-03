import pytorch_lightning as pl
from torch.nn import functional as F
import torch
import torchmetrics
import torch
from torch.nn import functional as F
import pytorch_lightning as pl


class SimpleNN(pl.LightningModule):
    """
    Simple neural network with 3 fully connected layers.
    """

    def __init__(self, input_size: int = 10000, output_size: int = 6) -> None:
        super().__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.layer_1 = torch.nn.LSTM(self.input_size, 128)
        self.layer_2 = torch.nn.Linear(128, 256)
        self.layer_3 = torch.nn.Linear(256, self.output_size)

    def forward(self, x):

        x = self.layer_1(x)
        x = torch.relu(x)

        x = self.layer_2(x)
        x = torch.relu(x)

        x = self.layer_3(x)
        y = torch.log_softmax(x, dim=1, dtype=x.dtype)

        return y

    def cross_entropy_loss(self, logits, labels):
        return F.nll_loss(logits, labels)

    def training_step(self, train_batch, batch_idx):
        x, y = train_batch
        logits = self.forward(x)
        loss = self.cross_entropy_loss(logits, y)
        self.log("train_loss", loss)
        return loss

    def validation_step(self, val_batch, batch_idx):
        x, y = val_batch
        logits = self.forward(x)
        loss = self.cross_entropy_loss(logits, y)
        self.log("val_loss", loss)

    def test_step(self, test_batch, batch_idx):
        x, y = test_batch
        f1_metric = torchmetrics.F1()
        acc_metric = torchmetrics.Accuracy()
        conf_metric = torchmetrics.ConfusionMatrix(num_classes=6)
        with torch.no_grad():
            logits = self.forward(x)
        acc = acc_metric(logits, y)
        f1 = f1_metric(logits, y)
        conf_matrix = conf_metric(logits, y)
        self.log("Confusion matrix", conf_matrix)
        self.log("Accuracy", acc)
        self.log("F1", f1)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

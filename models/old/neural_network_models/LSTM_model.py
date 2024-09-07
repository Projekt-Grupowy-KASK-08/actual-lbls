import pytorch_lightning as pl
from torch.nn import functional as F
import torch
import torchmetrics
import torch
from torch import nn
from torch.nn import functional as F
import pytorch_lightning as pl


class LSTMModel(pl.LightningModule):

    """
    LSTM network with lstm a few LSTM layers stackedd  on each other and one fully connected layer.
    """

    def __init__(self, input_dim, hidden_dim, layer_dim, output_dim, dropout_prob):
        super().__init__()
        # Defining the number of layers and the nodes in each layer
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim
        # LSTM layers
        self.lstm = nn.LSTM(
            input_dim, hidden_dim, layer_dim, batch_first=True, dropout=dropout_prob
        )
        # Fully connected layer
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = x.unsqueeze(-1)
        out, (hn, cn) = self.lstm(x)
        out = out[:, -1, :]
        out = self.fc(out)
        return out

    def training_step(self, train_batch, batch_idx):
        x, y = train_batch
        logits = self.forward(x)
        loss = self.mean_squared_loss(logits, y)
        self.log("train_loss", loss)
        return loss

    def mean_squared_loss(self, logits, labels):
        one_hot_labels = F.one_hot(labels, num_classes=6).type(torch.FloatTensor)
        return F.mse_loss(logits, one_hot_labels)

    def test_step(self, test_batch, batch_idx):
        x, y = test_batch
        f1_metric = torchmetrics.F1()
        acc_metric = torchmetrics.Accuracy()
        conf_metric = torchmetrics.ConfusionMatrix(num_classes=6)
        with torch.no_grad():
            logits = self.forward(x)
        acc = acc_metric(logits, y)
        f1 = f1_metric(logits, y)
        self.log("Accuracy", acc)
        self.log("F1", f1)

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

    def validation_step(self, val_batch, batch_idx):
        x, y = val_batch
        logits = self.forward(x)
        loss = self.mean_squared_loss(logits, y)
        self.log("val_loss", loss)

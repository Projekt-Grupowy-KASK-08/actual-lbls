import pytorch_lightning as pl
from torch.nn import functional as F
import torch
import torchmetrics
import torch
from torch import nn
from torch.nn import functional as F
import pytorch_lightning as pl

class Flatten(nn.Module):
    """Converts N-dimensional tensor into 'flat' one."""

    def __init__(self, keep_batch_dim=True):
        super().__init__()
        self.keep_batch_dim = keep_batch_dim

    def forward(self, x):
        if self.keep_batch_dim:
            return x.view(x.size(0), -1)
        return x.view(-1)

class _SepConv1d(nn.Module):
    """A simple separable convolution implementation.
    
    The separable convlution is a method to reduce number of the parameters 
    in the deep learning network for slight decrease in predictions quality.
    """
    def __init__(self, ni, no, kernel, stride, pad):
        super().__init__()
        self.depthwise = nn.Conv1d(ni, ni, kernel, stride, padding=pad, groups=ni)
        self.pointwise = nn.Conv1d(ni, no, kernel_size=1)

    def forward(self, x):
        return self.pointwise(self.depthwise(x))

class SepConv1d(nn.Module):
    """Implementes a 1-d convolution with 'batteries included'.
    
    The module adds (optionally) activation function and dropout layers right after
    a separable convolution layer.
    """
    def __init__(self, ni, no, kernel, stride, pad, drop=None,
                 activ=lambda: nn.ReLU(inplace=True)):
    
        super().__init__()
        assert drop is None or (0.0 < drop < 1.0)
        layers = [_SepConv1d(ni, no, kernel, stride, pad)]
        if activ:
            layers.append(activ())
        if drop is not None:
            layers.append(nn.Dropout(drop))
        self.layers = nn.Sequential(*layers)
        
    def forward(self, x): 
        return self.layers(x)

class SepConvClassifier(pl.LightningModule):
    """
    The classifier that uses SepaConv1d network.
    """

    def __init__(self, hidden_dim, input_dim=1, output_dim=2, dropout_prob=0.1):
        super().__init__()


        self.cnn = nn.Sequential(
            SepConv1d(input_dim,  32, 8, 2, 3, drop=dropout_prob),
            SepConv1d(    32,  64, 8, 4, 2, drop=dropout_prob),
            SepConv1d(    64, 128, 8, 4, 2, drop=dropout_prob),
            SepConv1d(   128, 256, 8, 4, 2),
        )

        self.flatten = nn.Sequential(
            Flatten()
        )
        self.classifier = nn.Sequential(
            nn.Linear(19968, hidden_dim), nn.ReLU(inplace=True),
            nn.Dropout(dropout_prob), nn.Linear( hidden_dim, output_dim), nn.ReLU(inplace=True))

        self.criterion = nn.CrossEntropyLoss(reduction='sum')

    def forward(self, x):
        x = x.view((1,1,10000))
        x = self.cnn(x)
        flat = self.flatten(x)
        out = self.classifier(flat)
        return out

    def training_step(self, train_batch, batch_idx):
        x, y = train_batch
        out = self.forward(x)
        loss = self.criterion(out, y)
        self.log("train_loss", loss)
        return loss

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
        out = self.forward(x)
        loss = self.criterion(out, y)
        self.log("val_loss", loss)
"""Illustrate usage of `DocumentClassifier`."""
import typing as t
import torch.nn as nn
import torchtext.vocab as v
from ..encode import document as denc
from ..example import ag_news as ag
from ..model import document as d
from . import model as m


def train(encoder_path: str, model_path: str):
    """Fit a `DocumentClassifier` on AG News."""
    m.AgNewsTrainer(_DocumentTrainImpl(), m.select_device(), 3000, 3000).train(
        encoder_path, model_path
    )


class _DocumentTrainImpl:
    """Implement `TrainProtocol`."""

    def create_encoder(
        self, vocabulary: v.Vocab, tokenizer: t.Callable[[str], list[str]]
    ) -> denc.DocumentEncodeProtocol:
        """Implement the protocol."""
        return denc.DocumentEncoder(vocabulary)

    def create_collate_fn(self, encoder) -> ag.AgNewsCollateSentenceFn:
        """Impl the protocol."""
        return ag.AgNewsCollateDocumentFn(encoder)

    def create_model(
        self, num_classes: int, vocabulary_size: int
    ) -> nn.Module:
        """Impl the protocol."""
        return d.DocumentClassifier(
            vocabulary_size=vocabulary_size,
            num_of_classes=num_classes,
        )

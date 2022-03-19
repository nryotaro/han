"""Tokenize text, and encode words to integers."""
import typing
import torch
import torchtext.vocab as v
from .. import token as t


class SentenceEncodeProtocol(typing.Protocol):
    """Encode a text to a tensor."""

    def forward(texts: list[str]) -> list[torch.Tensor]:
        """Transform texts to tensors."""


class SentenceEncoder:
    """Implement `SentenceEncodeProtocol`."""

    def __init__(self, vocab: v.Vocab, tokenizer: t.Tokenizer = t.Tokenizer()):
        """`vocab` has vocabulary."""
        self._vocab = vocab
        self.tokenizer = tokenizer

    def forward(self, texts: list[str]) -> list[torch.Tensor]:
        """Implement `forward`."""
        return [
            torch.Tensor(self._vocab(self.tokenizer(text))) for text in texts
        ]
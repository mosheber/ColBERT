import os
import random
from collections import OrderedDict, defaultdict

import torch
import ujson
from colbert.modeling.colbert import ColBERT
from colbert.parameters import DEVICE
from colbert.utils.utils import load_checkpoint, print_message


def load_model(args, do_print=True):
    colbert = ColBERT.from_pretrained(
        "bert-base-uncased",
        query_maxlen=args.query_maxlen,
        doc_maxlen=args.doc_maxlen,
        dim=args.dim,
        similarity_metric=args.similarity,
        mask_punctuation=args.mask_punctuation,
    )
    colbert = colbert.to(DEVICE)

    print_message("#> Loading model checkpoint.", condition=do_print)

    checkpoint = load_checkpoint(args.checkpoint, colbert, do_print=do_print)

    colbert.eval()

    return colbert, checkpoint

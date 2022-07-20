import torch
import json
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1" 
configs = {
    "train_source_data":"./data/train_sub.code",
    "train_target_data":"./data/train_sub.comm",
    "valid_source_data":"./data/test_sub.code",
    "valid_target_data":"./data/test_sub.comm",
    "source_tokenizer":"bert-base-uncased",
    "target_tokenizer":"vinai/phobert-base",
    "source_max_seq_len":128,
    "target_max_seq_len":16,
    "batch_size":64,
    "device":"cuda:0" if torch.cuda.is_available() else "cpu",
    "embedding_dim": 512,
    "n_layers": 6,
    "n_heads": 8,
    "dropout": 0.1,
    "lr":0.0001,
    "n_epochs":100,
    "print_freq": 5,
    "beam_size":3,
    "model_path":"./model_transformer_translate_sub.pt",
    "early_stopping":15
}

import matplotlib.pyplot as plt

# visualize log
def plot_loss(log_path, log_dir):
    log = json.load(open(log_path, "r"))

    plt.figure()
    plt.plot(log["train_loss"], label="train loss")
    plt.plot(log["valid_loss"], label="valid loss")
    plt.title("Loss per epoch")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig(os.path.join(log_dir, "loss_epoch.png"))

    # plot batch loss
    plt.figure()
    lst = log["train_batch_loss"]
    n = int(len(log["train_batch_loss"]) / len(log["valid_batch_loss"]))
    train_batch_loss = [lst[i:i + n][0] for i in range(0, len(lst), n)]
    plt.plot(train_batch_loss, label="train loss")
    plt.plot(log["valid_batch_loss"], label="valid loss")
    plt.title("Loss per batch")
    plt.xlabel("Batch")
    plt.ylabel("Loss")
    plt.legend()
    plt.savefig(os.path.join(log_dir, "loss_batch.png"))

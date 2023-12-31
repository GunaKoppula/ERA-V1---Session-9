import torch
import random
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from torchsummary import summary


def is_cuda(debug=True):
    cuda = torch.cuda.is_available()
    if debug:
        print("[INFO] Cuda Avaliable : ", cuda)
    return cuda


def get_device():
    use_cuda = is_cuda(debug=False)
    device = torch.device("cuda" if use_cuda else "cpu")
    print("[INFO] device : ", device)
    return device


def set_seed(seed=1):
    cuda = is_cuda(debug=False)
    torch.manual_seed(seed)
    if cuda:
        torch.cuda.manual_seed(seed)
    print(f"[INFO] seed set {seed}")


def show_random_images_for_each_class(
    train_data,
    num_images_per_class=16
):
    for c, cls in enumerate(train_data.classes):
        rand_targets = random.sample([
            n
            for n, x in enumerate(train_data.targets)
            if x==c
        ], k=num_images_per_class)
        show_img_grid(
            np.transpose(train_data.data[rand_targets], axes=(0, 3, 1, 2))
        )
        plt.title(cls)
    

def show_img_grid(data):
    try:
        grid_img = torchvision.utils.make_grid(data.cpu().detach())
    except:
        data = torch.from_numpy(data)
        grid_img = torchvision.utils.make_grid(data)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(grid_img.permute(1, 2, 0))
    

def show_random_images(data_loader):
    data, target  = next(iter(data_loader))
    show_img_grid(data)


def show_model_summary(model, input_size=(1, 28, 28)):
    summary(model, input_size=input_size)




# -*- coding: utf-8 -*-
"""Step02 Yuwei train PKL

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CCXqgTq1MeHifXdzDjGrxcQC5KKCKtdL

<p align="center">
    <a
    href="https://youtu.be/dcb4Ckpkx2o"
    target="_blank"
    rel="noopener noreferrer">
        <img
        alt="Night Sky Latent Walk"
        width="350" height="350"
        src="https://github.com/ArthurFDLR/GANightSky/blob/main/.github/random_walk.gif?raw=true">
    </a>
</p>

# 🚀 StyleGan2-ADA for Google Colab

1.   [Install StyleGAN2-ADA on your Google Drive](#scrollTo=5YcUMPQp6ipP)
2.   [Train a custom model](#scrollTo=Ti11YiPAiQpb)
3.   [Generate images from pre-trained model](#scrollTo=f0A9ZNtferpk)
4.   [Latent space exploration](#scrollTo=5yG1UyHXXqsO)

## Install StyleGAN2-ADA on your Google Drive

StyleGAN2-ADA only works with Tensorflow 1. Run the next cell before anything else to make sure we’re using TF1 and not TF2.
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
!nvidia-smi

"""Then, mount your Drive to the Colab notebook: """

from google.colab import drive
from pathlib import Path

content_path = Path('/').absolute() / 'content'
drive_path = content_path / 'drive'
drive.mount(str(drive_path))

"""Finally, run this cell to install StyleGAN2-ADA on your Drive. If you’ve already installed the repository, it will skip the installation process and only check for updates. If you haven’t installed it, it will install all the necessary files. Beside, **in**, **out**, **datasets** and **training** folders are generated for data storage. Everything will be available on your Google Drive in the folder **StyleGAN2-ADA** even after closing this Notebook."""

# Commented out IPython magic to ensure Python compatibility.
stylegan2_repo_url  = 'https://github.com/dvschultz/stylegan2-ada' # or https://github.com/NVlabs/stylegan2-ada
project_path        = drive_path / 'MyDrive' / 'StyleGAN2-ADA'
stylegan2_repo_path = project_path / 'stylegan2-ada'

# Create project folder if inexistant
if not project_path.is_dir():
#     %mkdir "{project_path}"
# %cd "{project_path}"

for dir in ['in', 'out', 'datasets', 'training']:
    if not (project_path / dir).is_dir():
#         %mkdir {dir}
if not (project_path / 'datasets' / 'source').is_dir():
#     %mkdir "{project_path / 'datasets' / 'source'}"

# Download StyleGAN2-ada
!git config --global user.name "GANightSky"
!git config --global user.email "NightSky@gan.com"
if stylegan2_repo_path.is_dir():
    !git -C "{stylegan2_repo_path}" fetch origin
    !git -C "{stylegan2_repo_path}" checkout origin/main -- *.py
else:
    print("Install StyleGAN2-ADA")
    !git clone {stylegan2_repo_url}

"""## Train a custom model

Once you have installed StyleGAN2-ADA on your Google Drive and set up the working directory, you can upload your training dataset images in the associated folder.
"""

dataset_name = 'dataset01output1024'
datasets_source_path = project_path / 'datasets' / 'source' / (dataset_name + '.zip')
if datasets_source_path.is_file():
    print("Dataset ready for import.")
else:
    print('Upload your images dataset as {}'.format(datasets_source_path))

"""Unfortunately, large datasets might exceed the Google Drive quota after a few training batches. Indeed, StyleGAN2 download datasets multiple times during training. You might have to import your dataset in the local storage session. However, large files cannot be copy/paste from Drive *(Input/Output error)*. 

Run this cell to download your zipped dataset from your Drive and unzip it in the local session.

### Convert dataset to .tfrecords

Next, we need to convert our image dataset to a format that StyleGAN2-ADA can read:`.tfrecords`.

This can take a while.

There are numerous arguments to tune the training of your model. To obtain nice results, you will certainly have to experiment. Here are the most popular parameters:


*   *mirror:* Should the images be mirrored vertically?
*   *mirrory:* Should the images be mirrored horizontally?
*   *snap:* How often should the model generate image samples and a network pickle (.pkl file)?
*   *resume:* Network pickle to resume training from?

To see all the options, run the following ```help``` cell.

Please note that Google Colab Pro gives access to V100 GPUs, which drastically decreases (~3x) processing time over P100 GPUs.
"""

!pip install -U numpy==1.18.5

# Commented out IPython magic to ensure Python compatibility.
training_path = project_path / 'training' / 'yw'
if not training_path.is_dir():
#     %mkdir "{training_path}"

#how often should the model generate samples and a .pkl file
snapshot_count = 2
#should the images be mirrored left to right?
mirrored = True
#should the images be mirrored top to bottom?
mirroredY = False
#metrics? 
metric_list = None
#augments
augs = 'bgc'

!python "{stylegan2_repo_path / 'train.py'}" --outdir="{training_path}" \
    --data="/content/drive/MyDrive/StyleGAN2-ADA/datasets/outputgan" \
    --snap={snapshot_count} --augpipe={augs} \
    --mirror={mirrored} --mirrory={mirroredY} \
    --metrics={metric_list} --resume /content/drive/MyDrive/StyleGAN2-ADA/training/yw/00002-outputgan-mirror-auto1-bgc-resumecustom/network-snapshot-000016.pkl #--dry-run

#!python "{stylegan2_repo_path / 'train.py'}" --help

#（用前面两行码就行，断了就用resume继续跑）

"""## Generate images from pre-trained model

You can finally generate images using a pre-trained network once everything is set-up. You can naturally use [your own model once it is trained](#scrollTo=Ti11YiPAiQpb&uniqifier=1) or use the ones NVLab published on [their website](https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada/pretrained/).

<p align="center">
    <img
    alt="Night Sky Latent Walk"
    width="450" height="300"
    src="https://github.com/ArthurFDLR/GANightSky/blob/main/.github/Random_Generation.png?raw=true">
</p>
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install opensimplex
!python "{stylegan2_repo_path / 'generate.py'}" generate-images --help

from numpy import random
seed_init = random.randint(10000)
nbr_images = 6

generation_from = '/content/drive/MyDrive/StyleGAN2-ADA/training/NightSky/StyleGAN2ADA_NightSky.pkl'

!python "{stylegan2_repo_path / 'generate.py'}" generate-images \
    --outdir="{project_path / 'out'}" --trunc=0.7 \
    --seeds={seed_init}-{seed_init+nbr_images-1} --create-grid \
    --network={generation_from}

"""## Latent space exploration

It is also possible to explore the latent space associated with our model and [generate videos like this one](https://youtu.be/dcb4Ckpkx2o).
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install opensimplex
!python "{stylegan2_repo_path / 'generate.py'}" generate-latent-walk --help

"""### Explore through multiple seeds"""

# Commented out IPython magic to ensure Python compatibility.
from numpy import random
walk_types = ['line', 'sphere']
latent_walk_path = project_path / 'out' / 'latent_walk'
if not latent_walk_path.is_dir():
#     %mkdir "{latent_walk_path}"

explored_network = 'ffhq1024'

seeds = [random.randint(10000) for i in range(3)]
print("Base seeds:", seeds)
!python "{stylegan2_repo_path / 'generate.py'}" generate-latent-walk --network="{explored_network}" \
    --outdir="{latent_walk_path}" --trunc=0.5 --walk-type="{walk_types[0]}" \
    --seeds={','.join(map(str, seeds))} --frames {len(seeds)*30}

"""### Explore around a single seed"""

# Commented out IPython magic to ensure Python compatibility.
from numpy import random
walk_types = ['noiseloop', 'circularloop']

latent_walk_path = project_path / 'out' / 'latent_walk'
if not latent_walk_path.is_dir():
#     %mkdir "{latent_walk_path}"

explored_network = 'ffhq1024'

start_seed = random.randint(10000)

!python "{stylegan2_repo_path / 'generate.py'}" generate-latent-walk --network="{explored_network}" \
    --outdir="{latent_walk_path}" --trunc=0.4 --walk-type=="{walk_types[1]}" \
    --start_seed="{start_seed}" --diameter=20 --frames {24*5}

"""## While you wait ...

... learn more about Generative Adversarial Networks and StyleGAN2-ADA:

*   [This Night Sky Does Not Exist](https://arthurfindelair.com/thisnightskydoesnotexist/): Generation of images from a model created using this Notebook on Google Colab Pro.
*   [This **X** Does Not Exist](https://thisxdoesnotexist.com/): Collection of sites showing the power of GANs.
*   [Karras, Tero, et al. _Analyzing and Improving the Image Quality of StyleGAN._ CVPR 2020.](https://arxiv.org/pdf/2006.06676.pdf): Paper published for the release of StyleGAN2-ADA.
*   [Official implementation of StyleGAN2-ADA](https://github.com/NVlabs/stylegan2-ada)
*   [StyleGAN v2: notes on training and latent space exploration](https://towardsdatascience.com/stylegan-v2-notes-on-training-and-latent-space-exploration-e51cf96584b3): Interesting article from Toward Data Science
"""
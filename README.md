# Golf Swing Analysis Tool
## Environment
- Python version: 3.8.18
- torch version: 1.13.1+cu117
- torchvision version: 0.14.1+cu117
- mmpose version: 1.2.0
- cuda version: 11.7
- compiler information: GCC 9.3

## Installation
### Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Install Pytorch
```bash
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```

### Install MMEngine and MMCV using MIM
```bash
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.1"
```

### Install mmdet
```bash
mim install "mmdet>=3.1.0"
```

### Install mmpose
```bash
git clone https://github.com/open-mmlab/mmpose.git
cd mmpose
pip install -r requirements.txt
pip install -v -e .
```

## MMPE (mmpose estimation)
### Installation
```Bash
git clone git@github.com:shuzo57/MMPE.git
cd MMPE
pip install -e .
```

### Download pretrained model (example)
```Bash
mim download mmpose --config rtmpose-l_8xb32-270e_coco-wholebody-384x288 --dest models
mim download mmdet --config rtmdet_m_8xb32-300e_coco --dest models
```
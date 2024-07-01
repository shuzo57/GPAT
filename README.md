# Golf Swing Analysis Tool
## Environment
- Python version: 3.8.18
- torch version: 1.13.1+cu117
- torchvision version: 0.14.1+cu117
- mmpose version: 1.2.0
- cuda version: 11.7
- compiler information: GCC 9.3

## Installation
### 1. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 2. Install Pytorch
```bash
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```

### 3. Install MMEngine and MMCV using MIM
```bash
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.1"
```

### 4. Install mmdet
```bash
mim install "mmdet>=3.1.0"
```

### 5. Install mmpose
```bash
git clone https://github.com/open-mmlab/mmpose.git
cd mmpose
pip install -r requirements.txt
pip install -v -e .
cd ..
```

### 6. Download pretrained model (example)
```Bash
mim download mmpose --config rtmpose-l_8xb32-270e_coco-wholebody-384x288 --dest models
mim download mmdet --config rtmdet_m_8xb32-300e_coco --dest models
```

#### For experiment
```Bash
mim download mmpose --config rtmpose-l_8xb256-420e_body8-384x288 --dest models
mim download mmdet --config rtmdet_l_8xb32-300e_coco --dest models
```

### 7. Copy and Write the configuration file
```ini
[model-setting]
pose_model = ~/GPAT/models/rtmpose-l_8xb32-270e_coco-wholebody-384x288.py
pose_checkpoint = ~/GPAT/models/rtmpose-l_simcc-coco-wholebody_pt-aic-coco_270e-384x288-eaeb96c8_20230125.pth
det_model = ~/GPAT/models/rtmdet_m_8xb32-300e_coco.py
det_checkpoint = ~/GPAT/models/rtmdet_m_8xb32-300e_coco_20220719_112220-229f527c.pth

[exp-setting]
pose_model = ~/GPAT/models/rtmpose-l_8xb256-420e_body8-384x288.py
pose_checkpoint = ~/GPAT/models/rtmpose-l_simcc-body7_pt-body7_420e-384x288-3f5a1437_20230504.pth
det_model = ~/GPAT/models/rtmdet_l_8xb32-300e_coco.py
det_checkpoint = ~/GPAT/models/rtmdet_l_8xb32-300e_coco_20220719_112030-5a0be7c4.pth
```

## USAGE
The Golf Player Analysis Tool (GPAT) offers a comprehensive solution for analyzing golf players' poses from video input. It is divided into two main parts: human detection and tracking (`first`), and pose estimation from tracking data (`second`). Here's how to use each component:

### General Syntax
The general command syntax for GPAT is as follows:

```bash
python -m gpat [-h] -i INPUT [-o OUTPUT] [-pm POSE_MODEL] [-pc POSE_CONFIG] [-dm DET_MODEL] [-dc DET_CONFIG] {first,second} ...
```

### Arguments
- `-h, --help`: Show this help message and exit.
- `-i INPUT, --input INPUT`: Input video file path.
- `-o OUTPUT, --output OUTPUT`: Output directory path (optional).
- `-pm POSE_MODEL, --pose-model POSE_MODEL`: Pose model path (optional).
- `-pc POSE_CONFIG, --pose-config POSE_CONFIG`: Pose config path (optional).
- `-dm DET_MODEL, --det-model DET_MODEL`: Detection model path (optional).
- `-dc DET_CONFIG, --det-config DET_CONFIG`: Detection config path (optional).

### 17のキーポイント
```bash
python -m gpat.exp [-h] -i INPUT [-o OUTPUT] [-pm POSE_MODEL] [-pc POSE_CONFIG] [-dm DET_MODEL] [-dc DET_CONFIG] [-f] [-s]
```

#### 引数
- `-h, --help`: ヘルプメッセージを表示して終了します。
- `-i INPUT, --input INPUT`: 入力ビデオファイルのパス。
- `-o OUTPUT, --output OUTPUT`: 出力ディレクトリのパス（オプション）。
- `-pm POSE_MODEL, --pose-model POSE_MODEL`: ポーズモデルのパス（オプション）。
- `-pc POSE_CONFIG, --pose-config POSE_CONFIG`: ポーズ設定のパス（オプション）。
- `-dm DET_MODEL, --det-model DET_MODEL`: 検出モデルのパス（オプション）。
- `-dc DET_CONFIG, --det-config DET_CONFIG`: 検出設定のパス（オプション）。
- `-f, --fpat`: GPATデータをFPATデータに変換します。
- `-s, --save_img`: 画像を保存します。

#### 使用方法
画像を保存する
```bash
python -m gpat.exp -i input_video.mp4 -o output_directory -s
```

### First: Human Detection and Tracking
To perform human detection and tracking on an input video file, use the `first` command with the following syntax:

```bash
python -m gpat first -i INPUT [-o OUTPUT] [-m DET_MODEL] [-c DET_CONFIG]
```

#### Arguments for `first`
- `-i INPUT, --input INPUT`: Input video file path.
- `-o OUTPUT, --output OUTPUT`: Output directory path (optional).
- `-m DET_MODEL, --det-model DET_MODEL`: Detection model path (optional).
- `-c DET_CONFIG, --det-config DET_CONFIG`: Detection config path (optional).

### Second: Pose Estimation from Tracking Data
After performing human detection and tracking, use the `second` command to estimate poses from the tracking data:

```bash
python -m gpat second -i INPUT -t TRACKING_DATA [-o OUTPUT] [-m POSE_MODEL] [-c POSE_CONFIG]
```

#### Arguments for `second`
- `-i INPUT, --input INPUT`: Input video file path.
- `-t TRACKING_DATA, --tracking_data TRACKING_DATA`: Tracking data file path.
- `-o OUTPUT, --output OUTPUT`: Output directory path (optional).
- `-m POSE_MODEL, --pose-model POSE_MODEL`: Pose model path (optional).
- `-c POSE_CONFIG, --pose-config POSE_CONFIG`: Pose config path (optional).
import os

import pandas as pd

from GPAT.gpat.utils.skeleton_keypoints import keypoints_list


def gpat2fpat(
    input_path: str,
) -> None:
    old_path = input_path + ".old"
    
    df = pd.read_csv(input_path)
    columns = ['frame'] + [f"{kpt}_{xyz}" for kpt in keypoints_list for xyz in ['x', 'y', 'z']]
    new_df = pd.DataFrame(columns=columns)
    
    for col in new_df.columns:
        if not col.endswith('z'):
            new_df[col] = df[col].copy()
        else:
            new_df[col] = df[col.replace('z', 'x')].copy()
    
    os.rename(input_path, old_path)
    new_df.to_csv(input_path, index=False)
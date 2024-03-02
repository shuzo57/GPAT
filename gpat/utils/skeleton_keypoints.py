keypoints_list = [
    "NOSE",
    "LEFT_EYE",
    "RIGHT_EYE",
    "LEFT_EAR",
    "RIGHT_EAR",
    "LEFT_SHOULDER",
    "RIGHT_SHOULDER",
    "LEFT_ELBOW",
    "RIGHT_ELBOW",
    "LEFT_WRIST",
    "RIGHT_WRIST",
    "LEFT_GROIN",
    "RIGHT_GROIN",
    "LEFT_KNEE",
    "RIGHT_KNEE",
    "LEFT_ANKLE",
    "RIGHT_ANKLE",
    "LEFT_BIG_TOE",
    "LEFT_LITTLE_TOE",
    "LEFT_HEEL",
    "RIGHT_BIG_TOE",
    "RIGHT_LITTLE_TOE",
    "RIGHT_HEEL",
]

keypoints_info = {
    "NOSE": "鼻",
    "LEFT_EYE": "左目",
    "RIGHT_EYE": "右目",
    "LEFT_EAR": "左耳",
    "RIGHT_EAR": "右耳",
    "LEFT_SHOULDER": "左肩",
    "RIGHT_SHOULDER": "右肩",
    "LEFT_ELBOW": "左肘",
    "RIGHT_ELBOW": "右肘",
    "LEFT_WRIST": "左手首",
    "RIGHT_WRIST": "右手首",
    "LEFT_GROIN": "左鼠径部",
    "RIGHT_GROIN": "右鼠径部",
    "LEFT_KNEE": "左膝",
    "RIGHT_KNEE": "右膝",
    "LEFT_ANKLE": "左足首",
    "RIGHT_ANKLE": "右足首",
    "LEFT_BIG_TOE": "左親指",
    "LEFT_LITTLE_TOE": "左小指",
    "LEFT_HEEL": "左踵",
    "RIGHT_BIG_TOE": "右親指",
    "RIGHT_LITTLE_TOE": "右小指",
    "RIGHT_HEEL": "右踵",
}

keypoints_connections ={
    "NOSE_LEFT_EYE": ["NOSE", "LEFT_EYE"],
    "NOSE_RIGHT_EYE": ["NOSE", "RIGHT_EYE"],
    "LEFT_EYE_EAR": ["LEFT_EYE", "LEFT_EAR"],
    "RIGHT_EYE_EAR": ["RIGHT_EYE", "RIGHT_EAR"],
    "SHOULDER": ["LEFT_SHOULDER", "RIGHT_SHOULDER"],
    "LEFT_UPPER_ARM": ["LEFT_SHOULDER", "LEFT_ELBOW"],
    "RIGHT_UPPER_ARM": ["RIGHT_SHOULDER", "RIGHT_ELBOW"],
    "LEFT_FORE_ARM": ["LEFT_ELBOW", "LEFT_WRIST"],
    "RIGHT_FORE_ARM": ["RIGHT_ELBOW", "RIGHT_WRIST"],
    "LEFT_TORSO": ["LEFT_SHOULDER", "LEFT_GROIN"],
    "RIGHT_TORSO": ["RIGHT_SHOULDER", "RIGHT_GROIN"],
    "LEFT_THIGH": ["LEFT_GROIN", "LEFT_KNEE"],
    "RIGHT_THIGH": ["RIGHT_GROIN", "RIGHT_KNEE"],
    "LEFT_LOWER_LEG": ["LEFT_KNEE", "LEFT_ANKLE"],
    "RIGHT_LOWER_LEG": ["RIGHT_KNEE", "RIGHT_ANKLE"],
    "LEFT_FOOT_1": ["LEFT_ANKLE", "LEFT_BIG_TOE"],
    "LEFT_FOOT_2": ["LEFT_ANKLE", "LEFT_LITTLE_TOE"],
    "LEFT_FOOT_3": ["LEFT_ANKLE", "LEFT_HEEL"],
    "RIGHT_FOOT_1": ["RIGHT_ANKLE", "RIGHT_BIG_TOE"],
    "RIGHT_FOOT_2": ["RIGHT_ANKLE", "RIGHT_LITTLE_TOE"],
    "RIGHT_FOOT_3": ["RIGHT_ANKLE", "RIGHT_HEEL"],
}
from typing import List, Dict


class StructureInfo:
    def __init__(
            self,
            root_name: str,
            root_channels: List[str],
            joint_channels: List[str],
            index_to_name_map: Dict[int, str],
            name_to_children_map: Dict[str, List[str]],
            rotation_order: str
    ):
        self.root_name = root_name
        self.root_channels = root_channels
        self.joint_channels = joint_channels
        self.index_to_name_map = index_to_name_map
        self.name_to_children_map = name_to_children_map
        self.rotation_order = rotation_order


def default_structure_info() -> StructureInfo:
    return StructureInfo(
        root_name="Hips",
        root_channels=["Xposition", "Yposition", "Zposition", "Zrotation", "Yrotation", "Xrotation"],
        joint_channels=["Zrotation", "Yrotation", "Xrotation"],
        index_to_name_map={
            0: "Hips",
            1: "LeftUpperLeg",
            2: "RightUpperLeg",
            3: "Spine",
            4: "LeftLowerLeg",
            5: "RightLowerLeg",
            6: "Chest",
            7: "LeftFoot",
            8: "RightFoot",
            9: "UpperChest",
            10: "LeftToe",
            11: "RightToe",
            12: "Neck",
            13: "LeftShoulder",
            14: "RightShoulder",
            15: "Head",
            16: "LeftUpperArm",
            17: "RightUpperArm",
            18: "LeftLowerArm",
            19: "RightLowerArm",
            20: "LeftHand",
            21: "RightHand",
        },
        name_to_children_map={
            "Hips": ["LeftUpperLeg", "RightUpperLeg", "Spine"],
            "Spine": ["Chest"],
            "Chest": ["UpperChest"],
            "UpperChest": ["Neck", "LeftShoulder", "RightShoulder"],
            "Neck": ["Head"],
            "Head": [],
            "LeftShoulder": ["LeftUpperArm"],
            "LeftUpperArm": ["LeftLowerArm"],
            "LeftLowerArm": ["LeftHand"],
            "LeftHand": [],
            "RightShoulder": ["RightUpperArm"],
            "RightUpperArm": ["RightLowerArm"],
            "RightLowerArm": ["RightHand"],
            "RightHand": [],
            "LeftUpperLeg": ["LeftLowerLeg"],
            "LeftLowerLeg": ["LeftFoot"],
            "LeftFoot": ["LeftToe"],
            "LeftToe": [],
            "RightUpperLeg": ["RightLowerLeg"],
            "RightLowerLeg": ["RightFoot"],
            "RightFoot": ["RightToe"],
            "RightToe": [],
        },
        rotation_order="ZYX",
    )

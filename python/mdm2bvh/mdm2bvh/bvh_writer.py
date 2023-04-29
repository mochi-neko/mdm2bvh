from typing import List, Any

from mdm2bvh.bone import Bone, find_bone


def write_bone(bone: Bone, skeleton: List[Bone], f: Any, depth: int) -> None:
    indent = '\t' * depth
    f.write(indent + ("ROOT {}\n".format(bone.name) if bone.is_root else "JOINT {}\n".format(bone.name)))
    f.write(indent + "{\n")
    f.write(indent + "\tOFFSET {} {} {}\n".format(bone.offset[0], bone.offset[1], bone.offset[2]))
    f.write(indent + "\tCHANNELS {} {}\n".format(len(bone.channels), " ".join(bone.channels)))
    if len(bone.children) > 0:
        for child_name in bone.children:
            child_index = find_bone(skeleton, child_name)
            if child_index is not None:
                write_bone(skeleton[child_index], skeleton, f, depth + 1)
    else:
        f.write(indent + "\tEnd Site\n")
        f.write(indent + "\t{\n")
        f.write(indent + "\t\tOFFSET {} {} {}\n".format(0, 0, 0))
        f.write(indent + "\t}\n")
    f.write(indent + "}\n")


def write_bvh(
        output_file: str,
        skeleton: List[Bone],
        number_of_frames: int,
        seconds_per_frame: float,
) -> None:
    with open(output_file, 'w') as f:
        # Write HIERARCHY
        f.write("HIERARCHY\n")
        write_bone(skeleton[0], skeleton, f, 0)

        # Write MOTION
        f.write("MOTION\n")
        f.write("Frames: {}\n".format(number_of_frames))
        f.write("Frame Time: {}\n".format(seconds_per_frame))

        for frame_idx in range(number_of_frames):
            frame_data = []
            for bone in skeleton:
                for channel in bone.motion_data[frame_idx]:
                    frame_data.append(channel)
            frame_str = " ".join(map(str, frame_data))
            f.write("{}\n".format(frame_str))

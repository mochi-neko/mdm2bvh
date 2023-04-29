from mdm2bvh.bvh_writer import write_bvh
from mdm2bvh.bone import dummy_skeleton


output_bvh_file = 'sample.bvh'
number_of_frames = 2
seconds_per_frame = 1.0 / 30.0  # = 30 FPS
skeleton = dummy_skeleton()

write_bvh(output_bvh_file, skeleton, number_of_frames, seconds_per_frame)

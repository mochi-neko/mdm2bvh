from mdm2bvh.mdm2bvh import convert_npy_to_bvh


source_npy_file = 'results.npy'
output_bvh_file = 'results.bvh'
seconds_per_frame = 1.0 / 30.0

convert_npy_to_bvh(source_npy_file, output_bvh_file, seconds_per_frame)

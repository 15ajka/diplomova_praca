import random 
import subprocess


# 20 000 images

for i in range(0,100):
	to_call = [
		# "python",'single_video.py',
		"python3",'single_video_pybullet.py',
		#'--spp','10',
		'--nb_frames', '10',
		'--nb_objects',str(int(random.uniform(4, 5))),
		'--nb_distractors','0',
                '--width','400',
                '--height','400',
                #"--easy",
		#'--static_camera',
		# '--nb_frames', '1',
		# '--nb_objects',str(1),
		'--outf',f"dataset4/{str(i).zfill(3)}",
	]
	subprocess.call(to_call)
	#subprocess.call(['mv',f'dataset/{str(i).zfill(3)}/video.mp4',f"dataset/{str(i).zfill(3)}.mp4"])
	# break
	# subprocess.Popen(["rsync",'-r',f'output/dataset/{str(i).zfill(3)}',
	# 	"/mnt/adlr/dataset_2/",";",
	# 	'rm','-rf',f'output/dataset/{str(i).zfill(3)}'])
	# subprocess.call([])
	# break

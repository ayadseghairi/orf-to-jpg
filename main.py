import glob
import rawpy
import imageio
import os
path = input('Enter The path : ')
if os.path.isdir(path):
	path1 = path+ "/*.ORF"
	path2 = path+ "/*.orf"
	lst1 = glob.glob(path1)
	lst2 = glob.glob(path2)
	for i in lst1 :
		if i in lst2 :
			pass
		else :
			lst2.append(i)
	try :
		os.mkdir("ayadseghairi")
	except FileExistsError:
		pass
	for infile in lst2:
		with rawpy.imread(infile) as raw:
			rgb = raw.postprocess()
			nouwfilename = "ayadseghairi/" + os.path.basename(infile)[:-4]+'.jpg'
			imageio.imwrite((str(nouwfilename)), rgb)
elif os.path.isfile(path):
	with rawpy.imread(path) as raw:
		rgb = raw.postprocess()
		nouwfilename = "ayadseghairi/" + os.path.basename(path)[:-4]+'.jpg'
		imageio.imwrite((str(nouwfilename)), rgb)
else :
	print(f"Error '{path}' Not found.")

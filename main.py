import glob
import rawpy
import imageio
import os

def progress_bar(progress,total):
	percent = 100 * (progress / float(total))
	bar = '#' * int(percent) + '_' * int(100 - percent)
	print(f"\r|{bar}| {progress:.2f}%",end="\r")
	


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
	i = 1
	progress_bar(0,len(lst2))
	for infile in lst2:
		progress_bar(i,len(lst2))
		with rawpy.imread(infile) as raw:
			rgb = raw.postprocess()
			nouwfilename = "ayadseghairi/" + os.path.basename(infile)[:-4]+'.jpg'
			imageio.imwrite((str(nouwfilename)), rgb)
			i+=1
elif os.path.isfile(path):
	with rawpy.imread(path) as raw:
		rgb = raw.postprocess()
		nouwfilename = "ayadseghairi/" + os.path.basename(path)[:-4]+'.jpg'
		imageio.imwrite((str(nouwfilename)), rgb)
else :
	print(f"Error '{path}' Not found.")

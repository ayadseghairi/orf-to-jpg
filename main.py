import glob
import rawpy
import imageio
import os
def progress_bar(progress,total,infile):
	percent = 50 * (progress / float(total))
	bar = '█' * int(percent) + ' ' * int(50 - percent)
	print(f"\r{os.path.basename(infile)}|{bar}| {percent*2:.2f}% |{progress}/{total}",end="\r")
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
	if len(lst2) !=0:
		try :
			os.mkdir("ayadseghairi")
		except FileExistsError:
			pass
		i = 1
		for infile in lst2:
			progress_bar(i,len(lst2),infile)
			with rawpy.imread(infile) as raw:
				rgb = raw.postprocess()
				nouwfilename = "ayadseghairi/" + os.path.basename(infile)[:-4]+'.jpg'
				imageio.imwrite((str(nouwfilename)), rgb)	
				i+=1
		print('\nDone.')
	else :
		print(f"Error no \"*.ORF\" image on \"{path}\".")
elif os.path.isfile(path):
	try :
		os.mkdir("ayadseghairi")
	except FileExistsError:
		pass
	with rawpy.imread(path) as raw:
		rgb = raw.postprocess()
		nouwfilename = "ayadseghairi/" + os.path.basename(path)[:-4]+'.jpg'
		imageio.imwrite((str(nouwfilename)), rgb)
	print('\nDone.')
else :
	print(f"Error '{path}' Not found.")

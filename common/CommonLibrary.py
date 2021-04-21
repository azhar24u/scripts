#Common Libraries to use
import glob
import os
from datetime import *
def WriteTechLog():
	log_dir=glob.glob("/gpfs/users/ggr03_d/log")[0]
	print(type(log_dir))
	log_file="ggr03_d_"+str(datetime.now().strftime("%Y%m%d")[0])+".log"
	print(type(log_file))
	dir_file=log_dir+"/"+log_file
	os.system("sudo mkdir -p log_dir")
	f=open(dir_file, "w+")
	f.write("start writing into the file")

WriteTechLog()


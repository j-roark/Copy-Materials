import os
import shutil
import time

mats  = ['eyeball_r', 'eyeball_l', 'eyeball_r_blue', 'eyeball_l_blue', 'eyeball_r_green', 'eyeball_l_green', 'mouth', 'hat', 'tc_beanies', 'tc_gasmask', 'tc_gasmask_glass', 'tc_helmet', 'hats', 'tc_male_citizen_torso_refugee', 'tc_male_citizen_torso1', 'tc_male_citizen_torso2', 'tc_male_citizen_torso_medic', 'tc_loyalist_suit', 'tc_pin', 'tc_male_loyalist_torso1', 'tc_labcoat', 'tc_male_citizen_worker1', 'tc_worker_armband', 'tc_male_citizen_worker2', 'tc_male_citizen_rebel', 'tc_male_citizen_rebel_why', 'tc_male_citizen_torso2', 'tc_citizen_trenchcoat', 'coat1', 'coat2a4a5a6', 'coat3', 'coat7', 'coat8', 'coat9', 'coat10', 'tc_male_citizen_torso_refugee', 'tc_male_citizen_pants_blue', 'legs_female', 'tc_male_citizen_rebel', 'shoes', 'booties', 'bootsandformalshoes', 'bootsandformalshoes', 'hands_b', 'hands_w', 'hands_w_glove', 'hands_glove', 'hands_b_glove', 'bags', 'bags', 'glass2', 'glassesfront_walter', 'glassesside_walter', 'tc_facewrap', 'facialhair02', 'tc_female_torso_refugee', 'tc_female_citizen_torso1', 'tc_female_citizen_torso2', 'tc_female_citizen_torso_medic', 'tc_loyalist_femsuit', 'tc_female_loyalist_torso1', 'tc_female_citizen_worker1', 'tc_female_citizen_worker2', 'tc_female_citizen_rebel', 'tc_female_citizen_rebel_why', 'coat1', 'coat2a4a5a6', 'coat3', 'coat7', 'coat8', 'coat9', 'coat10', 'shoes', 'female_hands', 'female_hands_black', 'female_hands_glove', 'female_hands_glove2', 'female_hands_glove2b']

# ^^ Materials go here
# Inserted are some simple examples

params = ['$basetexture','$bumpmap','$Iris','$AmbientOcclTexture','$Envmap','$CorneaTexture','$phongexponenttexture', '$detail']
# Insert your desired parameters to look for

path = 'C:/example/path/use/forward/slashes/thanks/old/'
newdir = 'C:/example/path/use/forward/slashes/thanks/new'
    

def CopyMats(subdirs, childs):
    
    for subdir in subdirs:        
        os.chdir(subdir)
        for file in os.listdir(subdir):
            if file.endswith('.vmt'):
                if os.path.splitext(file)[0] in mats:
                
                    print(os.path.splitext(file)[0])
                    dst = newdir + subdir.split('/old/')[1]
                
                    if not os.path.exists(dst):
                        
                        os.makedirs(dst)
                        print(dst, "-- doesn't exist, creating...")
                    
                    lines = []
                    with open(file, 'rt') as f:                    
                        for line in f:
                            lines.append(line)
                        
                    for key, value in enumerate(lines):
                        v = value.lstrip().replace('"', '').split(' ', 1)
                        line = v[0]
                        
                        for param in params:
                            if param == line:
                                a = lines[key]
                                b = a.lstrip().replace('"', '').split(' ', 1)
                                c = b[1].strip().split(' ', 1)
                                fin = c[0].replace('\\', '/')
                                
                                ## define target directories for dependencies. if it's not in one of these it won't copy the vtf!
                                if fin.startswith('models/willardnetworks') or fin.startswith('models/wn'):
                                    childs.append(fin)

                    shutil.copy(file, dst)
 
    return childs

def CopyVtf(childs):

    for child in childs:
        child = child.replace('\t', '')
        oldpath = path + child + '.vtf'
        newpath = newdir + child + '.vtf'
        
        if not os.path.exists(newpath):
            try:
                shutil.copy(oldpath,newpath)
                
            except OSError as e:
                print('Error in: ', child)
                print(e)


def main():

    subdirs = []
    childs = []
    
    for dir in os.walk(path):
        subdirs.append(dir[0].replace('\\','/'))
    
    CopyMats(subdirs, childs)
    print("\nParent material file transfer complete, grabbing children files...\n")
    CopyVtf(childs)
    print("\nDone!")
    exit()
    
main()

import os
path = 'Appliance/wicker'
i = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path,'data'+str(i)+'.jpg'))
    # print(os.path.join(path,filename))
    i = i +1
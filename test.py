import os
import argparse
import pandas as pd
import datetime



start_time = datetime.datetime.now()


parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('--jpg', type=str, default='1',help='opt number')
args = parser.parse_args()

# test per img
if args.jpg == '1':
    sheet = pd.read_excel('/home/yolov5/df.xlsx')
    sheet.columns = ['Class','Images','Labels','P','R','mAP50','mAP95']
    sheet.drop(sheet.columns[[1,2,3,4]],axis=1, inplace=True)
    print(sheet)
    

else:
    try:
        filename = str(args.jpg).split('/')[-1].replace('.jpg','')
        os.system('rm -rf /home/yolov5/runs/detect')
        os.system('mkdir /home/yolov5/runs/detect')
        os.system(f'/root/anaconda3/envs/yolov5/bin/python /home/yolov5/detect.py --weights /home/yolov5/model.pt --source {args.jpg} --save-txt --img-size 640')
        with open(f'/home/yolov5/runs/detect/exp/labels/{filename}.txt') as f:
            lines = f.readlines()

        lines = [line.rstrip('\n') for line in lines]
        #print(lines)
        print('\n')
        for row in lines:
            print(row)
    except:
        print('please check your path. try again')

end_time = datetime.datetime.now()


if args.jpg == '1':
    print('\ncommand  : ', f'python test.py')
else :
    print('\ncommand  : ', f'python test.py --jpg {args.jpg}')

print('start_time : ', start_time)
print('end_time   : ', end_time)






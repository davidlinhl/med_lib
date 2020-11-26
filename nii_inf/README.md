python nii2png.py
python infer.py --conf=model/deploy.yaml --input_dir /home/lin/Desktop/git/med/med_lib/nii_inf/imgs --ext png


`count=0
total=`ls -l | wc -l`
for f in `ls`;
do count=`expr $count + 1`;
echo $count / $total;
dcm2niix -f $f -o ../nii_raw/ -c $f $f
echo -e "\n"
echo -e "\n"
done
`


count=0
for f in `ls`;
do count=`expr $count + 1`;
echo $count / `ls -l | wc -l`;
echo ${f};
echo -e "\n";
itksnap -s ../label/${f} -g ${f} --geometry 1920x1080+0+0;
cp ../label/${f} ../manual-label/
done

import sys,glob
from PIL import Image
def sheet(files,out,w=360,cols=6):
    ims=[Image.open(f).convert('RGB') for f in files]
    ims=[i.resize((w,int(i.height*w/i.width))) for i in ims]
    H=max(i.height for i in ims); rows=(len(ims)+cols-1)//cols
    S=Image.new('RGB',(w*cols,H*rows),'white')
    for k,i in enumerate(ims): S.paste(i,((k%cols)*w,(k//cols)*H))
    S.save(out,quality=85)
if __name__=='__main__':
    d=sys.argv[1]; fs=sorted(glob.glob(f'/home/claude/repos/raquetada-posts/semana-2/{d}*/slide-*.jpg'))+sorted(glob.glob(f'/home/claude/repos/raquetada-posts/semana-2/{d}*/story*.jpg'))
    sheet(fs,sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 330, 7)

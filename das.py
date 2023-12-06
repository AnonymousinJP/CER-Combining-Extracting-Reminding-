import PyPDF2 as pdf2
import tkinter as tk
import glob,pyocr,pdfminer,schedule,time #エラーではない
from pdfminer.high_level import extract_text
from PIL import Image

#指定時間に指定のurlを開きたい
#分岐でurlの有無を判定

sp='>>>'
ch_,lang_=sp+"choose ",sp+"言語を選択："
def end():print("quit")
def pdf():
    dir=input("結合したいPDFが入ったフォルダのパスを指定：")
    fol=glob.glob(str(dir)+"/*")
    fol.sort()
    print(fol,dir)
    merger=pdf2.PdfMerger()
    for file in fol:merger.append(file)
    place=input("結合したPDFファイルを配置するフォルダのパスを指定：")
    merger.write(str(place)+"/new.pdf")
    merger.close()
def read():
    IF0=input(sp+"画像=>a, PDF=>b：")
    def pic_(): #画像
        print(sp+"画像")
        lang0=input(lang_) #言語選択
        img0=input(ch_+"picture：") #画像選択
        engines=pyocr.get_available_tools() #OCRエンジン取得
        engine=engines[0]
        txt=engine.image_to_string(Image.open(img0),lang=lang0) #読み込み
        txt0=txt.replace(' ','') #空白削除
        #テキスト出力
        if lang0=="eng":print(txt) #英語
        elif lang0=="jpn"or"jpn_vert":print(txt0) #日本語
        elif lang0=="chi_sim"or"chi_sim_vert":print(txt0) #簡体字
        elif lang0=="chi_tra"or"chi_tra_vert":print(txt0) #繁体字
        word0=input() in txt0
        print(word0)
    def pdf_(): #pdf
        FILE_PATH=input(sp+"PDF\n"+ch_+"file：") #ファイル選択
        #if FILE_PATH==False or None:print("error")
        pdftxt=extract_text(FILE_PATH)
        print(pdftxt) #テキスト出力
    if IF0=='a':pic_()
    elif IF0=='b':pdf_()
    else:end()
def remind():
    for br in range(5):br='\n'
    msg_val=input("予定：")#内容
    time_val=input("時間：")#時間
    def task():
        base0=tk.Tk()
        base0.title("リマインダー")
        label0=tk.Label(text=br+msg_val+'\n'+time_val,font=("MSゴシック","30","bold"),foreground='black',background='white')
        base0.geometry('500x500')
        base0.configure(bg='white')
        label0.pack()
        base0.mainloop()
    schedule.every().day.at(time_val).do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)
WHICH=input("機能\n"+sp+"PDFを結合=>a\n"+sp+"画像・PDFからテキストを抽出=>b\n"+sp+"リマインダー=>c\n")
if WHICH=="a":pdf()
elif WHICH=="b":read()
elif WHICH=="c":remind()
else:end()


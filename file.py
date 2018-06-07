#ファイル入出力とzip圧縮の練習

#ファイル名のセパレータ
sep = '/'

class FileMaker:
    #ワーキングディレクトリとプレフィクス文字列を与えて初期化
    def __init__(self, working_directory, prefix):
        self.wd = working_directory
        self.prefix = prefix
        self.counter = 1


    #関数的動作の本体　ファイルを書き込む
    def __call__(self, content):
        filename = self.wd + sep + self.prefix + str(self.counter) + '.txt'
        try:
            f = open(filename, "w")
            f.write(content)
            f.flush()
            f.close()
        except:
            print('Failed writing file. filename = ', filename, ', content = ', content)
        else:
            self.counter += 1
        return

#ファイルの中身を読み込み、表示する関数
import io
def cat(f):
    if (isinstance(f, str)): #fileが文字列ならファイル名として扱う
        with open(f, 'r') as fp: #with記法の練習
            print(fp.read())
            #with記法ではcloseは不要
    elif (isinstance(f, io.IOBase)): #fileがファイルオブジェクトなら
        alreadyopen = not f.closed #!ではない
        if not alreadyopen: #すでに閉じられたものであれば再オープンする
            f = open(f.name, 'r')
        loc = f.tell() #ストリーム位置の保存
        f.seek(0) #先頭に戻る
        print(f.read())
        f.seek(loc) #ストリーム位置を戻す

        #もともとopenされた状態で渡された場合はopenのまま終了する
        #そうでない場合はcloseする
        if not alreadyopen:
            f.close()
    else:
        raise ValueError('cat: f must be a str or a file')
    return

#メインルーチン

#カレントディレクトリを取得
from os import getcwd #from記法の練習
cd =getcwd()

#FileMakerオブジェクトを作成
fm = FileMaker(cd, 'a')

#a1-a5ファイルを作成、中身は筋肉の名前シリーズ
fm('Biceps brachii')
fm('Serratus anterior')
fm('Sternocleidomastoideus')
fm('Lattisimus dorsi')
fm('Gluteus medius')

#a1-a5ファイルの中身を表示
#a1-a3は文字列で渡す
for i in range(1, 4):
    fname = cd + sep + 'a' + str(i) + '.txt'
    cat(fname)

#a4-a5はファイルオブジェクトで渡す
for i in range(4, 6):
    with open(cd + sep + 'a' + str(i) + '.txt', 'r') as fp:
        cat(fp)

#zipに圧縮
import zipfile
zipname = cd + sep + 'texts.zip'
zip = zipfile.ZipFile(zipfile, mode='w')

#a1-5.txtをzipに書き込む
for i in range(1, 6):
    fname = 'a' + str(i) + '.txt'
    zip.write(fname)

zip.close()

#zipに書き込めているかの確認
zip = zipfile.ZipFile(zipname, mode='r')
list = zip.namelist()
print(list)
zip.close()

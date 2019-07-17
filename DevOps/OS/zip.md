GNU / Linux 各種壓縮與解壓縮指令
Contents
.tar
.gz	.tar.gz
.bz	.tar.bz
.bz2	.tar.bz2
.xz	.tar.xz
.Z	.tar.Z
.tgz	.tar.tgz
.7z	.zip
.rar	.lha

.tar (僅打包，無壓縮)
套件名稱：tar。
打包：
[ jonny@linux ~ ]
$ tar cvf FileName.tar DirName
解包：
[ jonny@linux ~ ]
$ tar xvf FileName.tar


.gz
套件名稱：gzip。
壓縮
[ jonny@linux ~ ]
$ gzip FileName
解壓縮 1：
[ jonny@linux ~ ]
$ gunzip FileName.gz
解壓縮 2：
[ jonny@linux ~ ]
$ gzip -d FileName.gz


.tar.gz
套件名稱：gzip。
壓縮：
[ jonny@linux ~ ]
$ tar zcvf FileName.tar.gz DirName
解壓縮：
[ jonny@linux ~ ]
$ tar zxvf FileName.tar.gz


bz
壓縮：unkown。
解壓縮 1：
[ jonny@linux ~ ]
$ bzip2 -d FileName.bz
解壓縮 2：
[ jonny@linux ~ ]
$ bunzip2 FileName.bz


.tar.bz
壓縮：unkown。
解壓縮：
[ jonny@linux ~ ]
$ tar jxvf FileName.tar.bz


.bz2
套件名稱：bzip2。
壓縮：
[ jonny@linux ~ ]
$ bzip2 -z FileName
解壓縮 1：
[ jonny@linux ~ ]
$ bzip2 -d FileName.bz2
解壓縮 2：
[ jonny@linux ~ ]
$ bunzip2 FileName.bz2


.tar.bz2
套件名稱：bzip2。
壓縮：
[ jonny@linux ~ ]
$ tar jcvf FileName.tar.bz2 DirName
解壓縮：
[ jonny@linux ~ ]
$ tar jxvf FileName.tar.bz2
.tar.bz2 (parallel)
套件名稱：lbzip2。
壓縮：
[ jonny@linux ~ ]
$ tar -I lbzip2 -cvf FileName.tar.bz2 DirName


.xz
套件名稱：xz-utils。
壓縮：
[ jonny@linux ~ ]
$ xz -z FileName
解壓縮：
[ jonny@linux ~ ]
$ xz -d FileName.xz


.tar.xz
套件名稱：xz-utils。
壓縮：
[ jonny@linux ~ ]
$ tar Jcvf FileName.tar.xz DirName
解壓縮：
[ jonny@linux ~ ]
$ tar Jxvf FileName.tar.xz


.Z
壓縮：
[ jonny@linux ~ ]
$ compress FileName
解壓縮：
[ jonny@linux ~ ]
$ uncompress FileName.Z

.tar.Z
壓縮：
[ jonny@linux ~ ]
$ tar Zcvf FileName.tar.Z DirName
解壓縮：
[ jonny@linux ~ ]
$ tar Zxvf FileName.tar.Z

.tgz
套件名稱：gzip。
壓縮：
[ jonny@linux ~ ]
$ tar zcvf FileName.tgz FileName
解壓縮：
[ jonny@linux ~ ]
$ tar zxvf FileName.tgz

.tar.tgz
套件名稱：gzip。
壓縮：
[ jonny@linux ~ ]
$ tar zcvf FileName.tar.tgz FileName
解壓縮：
[ jonny@linux ~ ]
$ tar zxvf FileName.tar.tgz

.7z
套件名稱：p7zip-full。
壓縮：
[ jonny@linux ~ ]
$ 7z a FileName.7z FileName
使用密碼 (PASSWORD) 壓縮：
[ jonny@linux ~ ]
$ 7z a FileName.7z FileName -pPASSWORD
解壓縮：
[ jonny@linux ~ ]
$ 7z x FileName.7z

.zip
套件名稱：zip。
壓縮：
[ jonny@linux ~ ]
$ zip -r FileName.zip DirName
解壓縮：
[ jonny@linux ~ ]
$ unzip FileName.zip

.rar
套件名稱：rar, unrar。
壓縮：
[ jonny@linux ~ ]
$ rar a FileName.rar DirName
解壓縮 1：
[ jonny@linux ~ ]
$ rar e FileName.rar
解壓縮 2：
[ jonny@linux ~ ]
$ unrar e FileName.rar
解壓縮 3：在指定目錄內解壓縮。
[ jonny@linux ~ ]
$ rar x FileName.rar DirName

.lha
套件名稱：lha。
壓縮：
[ jonny@linux ~ ]
$ lha -a FileName.lha FileName
解壓縮：
[ jonny@linux ~ ]
$ lha -e FileName.lha
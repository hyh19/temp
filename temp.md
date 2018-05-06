# 第 9 章 基本文本处理

- [第 9 章 基本文本处理](#9)
  - [9.3 使用 sort 命令对文本排序](#93--sort)
    - [9.3.1 sort 命令的基本用法](#931-sort)
    - [9.3.2 使用单个关键字排序](#932)
  - [9.5 使用 `cut` 命令选取文本列](#95--cut)
    - [9.5.1 cut 命令及其语法](#951-cut)
    - [9.5.2 选择指定的文本列](#952)
    - [9.5.3 选择指定数量的字符](#953)
    - [9.5.4 排除不包含列分隔符的行](#954)
  - [9.6 使用 `paste` 命令拼接文本列](#96--paste)
    - [9.6.1 `paste` 命令及其语法](#961-paste)
    - [9.6.2 自定义列分隔符](#962)
    - [9.6.3 拼接指定的文本列](#963)

## 9.3 使用 sort 命令对文本排序

### 9.3.1 sort 命令的基本用法

demo5.txt
```
Toy_Story                 HK           239          3972
The_Hill                  KL           63           2972
Star_Wars                 HK           301          4102
Boys_in_Company_C         HK           192          2192
Aliens                    HK           532          4892
Alien                     HK           119          1982
A_Few_Good_Men            KL           445          5851
```

如果不指定任何选项，则 sort 命令会将整个文本行作为一个关键字来排序。
```
$ sort demo5.txt 
A_Few_Good_Men            KL           445          5851
Alien                     HK           119          1982
Aliens                    HK           532          4892
Boys_in_Company_C         HK           192          2192
Star_Wars                 HK           301          4102
The_Hill                  KL           63           2972
Toy_Story                 HK           239          3972
```

### 9.3.2 使用单个关键字排序

pos1 表示排序关键字的起始位置，pos2 表示排序关键字的结束位置，这两者之间用逗号隔开。通常情况下，组成排序关键字都是以列为单位的。此时，pos1 和 pos2 就是关键字的起始列和结束列的列号。列号从 1 开始，即第 1 列为 1，第 2 列为 2，依此类推。
```
-k pos1[,pos2]
```
**注意：sort 命令中，一个文本行最多只能包括 10 列。**


```
$ sort -k 2,3 demo5.txt 
Alien                     HK           119          1982
Boys_in_Company_C         HK           192          2192
Toy_Story                 HK           239          3972
Star_Wars                 HK           301          4102
Aliens                    HK           532          4892
A_Few_Good_Men            KL           445          5851
The_Hill                  KL           63           2972
```
**注意：sort 命令会将列的值作为字符串来排序。而 “63” 中的第 1 个字符 “6” 的 ASCII 码比其余的值的第 1 个字符的 ASCII 码值都大，所以排到了最后。**


表示从 pos 参数指定的列开始，一直到文本行的结尾都是排序关键字。
```
-k pos
```

demo6.txt
```
Toy_Story                 HK           239          3972
The_Hill                  KL           63           2972
Star_Wars                 HK           301          4102
Boys_in_Company_C         HK           239          2192
Aliens                    HK           532          4892
Alien                     HK           119          1982
A_Few_Good_Men            KL           445          5851
```

```
$ sort -k 2 demo6.txt 
Alien                     HK           119          1982
Boys_in_Company_C         HK           239          2192
Toy_Story                 HK           239          3972
Star_Wars                 HK           301          4102
Aliens                    HK           532          4892
A_Few_Good_Men            KL           445          5851
The_Hill                  KL           63           2972
```
## 9.5 使用 `cut` 命令选取文本列

### 9.5.1 cut 命令及其语法


```bash
$ cut --help
Usage: cut OPTION... [FILE]...
Print selected parts of lines from each FILE to standard output.

Mandatory arguments to long options are mandatory for short options too.
  -b, --bytes=LIST        select only these bytes
  -c, --characters=LIST   select only these characters
  -d, --delimiter=DELIM   use DELIM instead of TAB for field delimiter
  -f, --fields=LIST       select only these fields;  also print any line
                            that contains no delimiter character, unless
                            the -s option is specified
  -n                      with -b: don't split multibyte characters
      --complement        complement the set of selected bytes, characters
                            or fields
  -s, --only-delimited    do not print lines not containing delimiters
      --output-delimiter=STRING  use STRING as the output delimiter
                            the default is to use the input delimiter
      --help     display this help and exit
      --version  output version information and exit

Use one, and only one of -b, -c or -f.  Each LIST is made up of one
range, or many ranges separated by commas.  Selected input is written
in the same order that it is read, and is written exactly once.
Each range is one of:

  N     N'th byte, character or field, counted from 1
  N-    from N'th byte, character or field, to end of line
  N-M   from N'th to M'th (included) byte, character or field
  -M    from first to M'th (included) byte, character or field

With no FILE, or when FILE is -, read standard input.

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
For complete documentation, run: info coreutils 'cut invocation'
```


### 9.5.2 选择指定的文本列

指定分隔符是 `:`，选择 1 和 6 两列。
```bash
# 逗号指定单独多列
$ cut -d ":" -f 1,6 /etc/passwd
root:/root
bin:/bin
daemon:/sbin
adm:/var/adm
lp:/var/spool/lpd
sync:/sbin
shutdown:/sbin
halt:/sbin
mail:/var/spool/mail
operator:/root
games:/usr/games
ftp:/var/ftp
nobody:/
systemd-network:/
dbus:/
polkitd:/
rpc:/var/lib/rpcbind
rpcuser:/var/lib/nfs
nfsnobody:/var/lib/nfs
postfix:/var/spool/postfix
sshd:/var/empty/sshd
chrony:/var/lib/chrony
centos:/home/centos
```

选择 1 至 6 列
```bash
# 连字符指定连续多列
$ cut -d ":" -f 1-6 /etc/passwd 
root:x:0:0:root:/root
bin:x:1:1:bin:/bin
daemon:x:2:2:daemon:/sbin
adm:x:3:4:adm:/var/adm
lp:x:4:7:lp:/var/spool/lpd
sync:x:5:0:sync:/sbin
shutdown:x:6:0:shutdown:/sbin
halt:x:7:0:halt:/sbin
mail:x:8:12:mail:/var/spool/mail
operator:x:11:0:operator:/root
games:x:12:100:games:/usr/games
ftp:x:14:50:FTP User:/var/ftp
nobody:x:99:99:Nobody:/
systemd-network:x:192:192:systemd Network Management:/
dbus:x:81:81:System message bus:/
polkitd:x:999:997:User for polkitd:/
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind
rpcuser:x:29:29:RPC Service User:/var/lib/nfs
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs
postfix:x:89:89::/var/spool/postfix
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd
chrony:x:998:995::/var/lib/chrony
centos:x:1000:1000:Cloud User:/home/centos
```

选择第一列至 3 列
```bash
$ cut -d ":" -f -3 /etc/passwd   
root:x:0
bin:x:1
daemon:x:2
adm:x:3
lp:x:4
sync:x:5
shutdown:x:6
halt:x:7
mail:x:8
operator:x:11
games:x:12
ftp:x:14
nobody:x:99
systemd-network:x:192
dbus:x:81
polkitd:x:999
rpc:x:32
rpcuser:x:29
nfsnobody:x:65534
postfix:x:89
sshd:x:74
chrony:x:998
centos:x:1000
```


选择 3 至最后一列
```bash
$ cut -d ":" -f 3- /etc/passwd  
0:0:root:/root:/bin/bash
1:1:bin:/bin:/sbin/nologin
2:2:daemon:/sbin:/sbin/nologin
3:4:adm:/var/adm:/sbin/nologin
4:7:lp:/var/spool/lpd:/sbin/nologin
5:0:sync:/sbin:/bin/sync
6:0:shutdown:/sbin:/sbin/shutdown
7:0:halt:/sbin:/sbin/halt
8:12:mail:/var/spool/mail:/sbin/nologin
11:0:operator:/root:/sbin/nologin
12:100:games:/usr/games:/sbin/nologin
14:50:FTP User:/var/ftp:/sbin/nologin
99:99:Nobody:/:/sbin/nologin
192:192:systemd Network Management:/:/sbin/nologin
81:81:System message bus:/:/sbin/nologin
999:997:User for polkitd:/:/sbin/nologin
32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
89:89::/var/spool/postfix:/sbin/nologin
74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
998:995::/var/lib/chrony:/sbin/nologin
1000:1000:Cloud User:/home/centos:/bin/bash
```

选择 1、2 和 4 至 5 列
```bash
# 混用逗号和连字符
$ cut -d ":" -f 1,2,4-5 /etc/passwd
root:x:0:root
bin:x:1:bin
daemon:x:2:daemon
adm:x:4:adm
lp:x:7:lp
sync:x:0:sync
shutdown:x:0:shutdown
halt:x:0:halt
mail:x:12:mail
operator:x:0:operator
games:x:100:games
ftp:x:50:FTP User
nobody:x:99:Nobody
systemd-network:x:192:systemd Network Management
dbus:x:81:System message bus
polkitd:x:997:User for polkitd
rpc:x:32:Rpcbind Daemon
rpcuser:x:29:RPC Service User
nfsnobody:x:65534:Anonymous NFS User
postfix:x:89:
sshd:x:74:Privilege-separated SSH
chrony:x:995:
centos:x:1000:Cloud User
```

### 9.5.3 选择指定数量的字符

选择第 1 至 3 个和第 5 个字符
```bash
$ cut -c 1-3,5 /etc/passwd
roo:
binx
daeo
admx
lp::
syn:
shud
hal:
mai:
opea
gams
ftpx
nobd
syse
dbu:
poli
rpcx
rpcs
nfso
posf
ssh:
chrn
ceno
```

**注意：由于选择字符是将整个文本行看做一个字符串进行的，所以不需要也不能指定列分隔符。**

### 9.5.4 排除不包含列分隔符的行

```bash
cp /etc/passwd passwd.txt
# 加一行不带分隔符的行
echo pig >> passwd.txt

# 不带 -s 选项
$ cut -d ":" -f 1 passwd.txt 
root
bin
daemon
adm
lp
sync
shutdown
halt
mail
operator
games
ftp
nobody
systemd-network
dbus
polkitd
rpc
rpcuser
nfsnobody
postfix
sshd
chrony
centos
pig # 没有列分隔符的行也输出了

# 带 -s 选项
$ cut -d ":" -f 1 -s passwd.txt 
root
bin
daemon
adm
lp
sync
shutdown
halt
mail
operator
games
ftp
nobody
systemd-network
dbus
polkitd
rpc
rpcuser
nfsnobody
postfix
sshd
chrony
centos
# 没有列分隔符的行被排除了
```

## 9.6 使用 `paste` 命令拼接文本列

测试数据

```bash
$ cat students.txt
i       12
b       13
c       14

$ cat phone.txt
200200110            13611499594
200200164            13682239867
200200167            13710153203
200200168            13622259071
200200172            13430324699
200200179            13640656767
```

### 9.6.1 `paste` 命令及其语法

```bash
$ paste students.txt phones.txt 
200200110            Abdul      200200110            13611499594
200200164            Abram      200200164            13682239867
200200167            Bartley    200200167            13710153203
200200168            Bennett    200200168            13622259071
200200172            Cecil      200200172            13430324699
200200173            John       200200179            13640656767 # 注意：不进行关键字的比较，学号不一样也拼接在一起。
200200187            Cat
```

### 9.6.2 自定义列分隔符

```bash
$ paste -d "," students.txt phones.txt  
200200110            Abdul,200200110            13611499594
200200164            Abram,200200164            13682239867
200200167            Bartley,200200167            13710153203
200200168            Bennett,200200168            13622259071
200200172            Cecil,200200172            13430324699
200200173            John,200200179            13640656767
200200187            Cat,
```

### 9.6.3 拼接指定的文本列


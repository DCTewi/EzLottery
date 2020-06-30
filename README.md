# EzLottery

受人所托简单搓的一个PyQt写的简单的抽奖小工具。

### Screenshot

![](https://s1.ax1x.com/2020/06/30/NIGwvR.png)

# Usage

部署：

```sh
pyinstaller -F -w -i static/icon.ico -n EzLottery app.py
```

或者直接用Python运行：

```sh
python app.py
```

或者直接在[Release页](https://github.com/DCTewi/EzLottery/releases)下载。

（顺便一提，新版本的Github真好看，界面布置也变得合理了许多。）

左边输入名字列表，右边输入序列号。点一下按钮随机分配一下，没有被分配到的会被忽略。

## License

![License-MIT](https://img.shields.io/badge/license-MIT-66ccff.svg)
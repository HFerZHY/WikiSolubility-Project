# WikiSolubility-Project
This is a development repository of the Wikisoluble gadget.

Wikisoluble is a project for searching solubility and it was inspired by my `python` homework. All data was crawled from [wikipedia](https://wikipedia.org) via `scrapy`, that's why the name of this project is `wikisolubility`.
Currently there are some functions supported:
>More than 650 substances available
>Comparision of two different substances by chart
>Chart export
>Theme changing (dark mode and light mode)

TODOs:
>Chinese
>Code structure optimization
>Chart optimization

## Usage:
### Installation:
```sh
git clone https://github.com/HFerZHY/WikiSolubility-Project/
cd WikiSolubility-Project/
pip3 install -r requirements.txt
```
### Start:
```sh
python3 wikisoluble.py
```

### Enjoy!


Wikisoluble是我python学校作业所产生出来的一个衍生小项目，主要功能就是查询物质的溶解度，所有数据都是通过scrapy从维基百科上面爬下来的，所以有了这个名字。
现有功能：
>超过650种物质的溶解度查询
>单一物质溶解度折线图以及两种物质的溶解度对比折线图绘制
>更改主题颜色
>导出折线图

待处理事项：
>中文查询支持（毕竟数据是英文维基百科上的）
>优化代码设计
>优化绘图功能，避免文字重叠


## 使用方法:
### 安装:
```sh
git clone https://github.com/HFerZHY/WikiSolubility-Project/
cd WikiSolubility-Project/
pip3 install -r requirements.txt
```
### 启动应用:
```sh
python3 wikisoluble.py
```

# ImageHemorrhage
Image hemorrhage operation.  

## 使用说明：  

一般用户请打开**Win32Release**文件夹。  
将所有待处理的图像放到**ImageSrc**文件夹内，之后运行**Run.exe**即可。  
在此之前，您需要设定一下**Setting.json**内的内容，内容如下：  

    {
    "border":
    {
        "top":40,
        "bottom":40,
        "left":40,
        "right":40
    },
    "opcity":0.5
    }

border内的四项分别表示要出血的**像素值**，如果是毫米请自行换算，只需要更改数字即可，为整数。  
opcity表示出血部分的透明度。  

结果存储在**ImageRes**文件夹内。

## 作者

**戴天宇(dtysky)**   
[http://dtysky.github.io](http://dtysky.github.io)  
[dtysky@outlook.com](dtysky@outlook.com)  
[http://github.com/dtysky](http://github.com/dtysky)

## 版权

Copyright © 2014, 戴天宇(dtysky)。 拥有所有权利。  
此项目属于自由软件，遵守[MIT License (MIT)](http://mit-license.org/)开源软件协议。
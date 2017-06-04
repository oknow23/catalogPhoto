# catalogPhoto

Catalog photo to different folder by date
Put raw and video file to Individually folder


### Environment:
- Install python 2.7
- pyexiv2, a python binding to exiv2 - https://goo.gl/Qp3E1

### How to use:
#### Linux:
- Put catalogPhoto.py and photos in the same folde
- python catalogPhoto.py
#### Wdindows:
- dowload https://github.com/oknow23/catalogPhoto/raw/master/dist/catalogPhoto.exe
- Put catalogPhoto.exe and photos in the same folder and double click to execute it.

### The result like below:

D:\catalogPhoto\dist content

		2017/06/04  下午 11:14    <DIR>          .
		2017/06/04  下午 11:14    <DIR>          ..
		2017/06/04  下午 10:04         4,758,489 catalogPhoto.exe
		2017/05/16  下午 08:12           488,975 DSCF0144.jpg
		2017/05/08  下午 11:08           593,162 DSCF0178-fix-combine.jpg
		2017/04/10  下午 10:22           974,751 DSCF8037.jpg
		2017/04/02  下午 05:59        33,817,088 DSCF8044.RAF
		2017/04/10  下午 10:22           740,063 DSCF8047.jpg
		2014/03/24  下午 05:32        34,286,061 DSCF8048.mov
		2017/04/14  下午 09:57           268,051 DSCF8422.jpg
		2017/04/14  下午 09:57           832,694 DSCF8452-fix.jpg
		               9 Files      76,759,334 bits

- When launch catalogPhoto,CatalogPhoto will catalog photo to folder and the result as follow

		2017-05-10 [Taipei]
		2017-05-07 [Taipei]
		2017-04-10 [Taipei]
		2017-04-02 [Taipei]
		2017-04-10 [Taipei]
		2017-04-10 [Taipei]
		2017-04-13 [Taipei]
		2017-04-13 [Taipei]
		Done!!
		請按任意鍵繼續 . . .

- And folder tree as follow

		 D:\catalogPhoto\dist\2017-04-02 [Taipei] content

		2017/06/05  上午 07:38    <DIR>          raw
		               0 Files               0 bits

		 D:\catalogPhoto\dist\2017-04-02 [Taipei]\raw content

		2017/04/02  下午 05:59        33,817,088 DSCF8044.RAF
		               1 Files      33,817,088 H

		 D:\catalogPhoto\dist\2017-04-10 [Taipei] content

		2017/04/10  下午 10:22           974,751 DSCF8037.jpg
		2017/04/10  下午 10:22           740,063 DSCF8047.jpg
		2017/06/05  上午 07:38    <DIR>          video
		               2 Files       1,714,814 bits

		 D:\catalogPhoto\dist\2017-04-10 [Taipei]\video content

		2014/03/24  下午 05:32        34,286,061 DSCF8048.mov
		               1 Files      34,286,061 bits

		 D:\catalogPhoto\dist\2017-04-13 [Taipei] content

		2017/04/14  下午 09:57           268,051 DSCF8422.jpg
		2017/04/14  下午 09:57           832,694 DSCF8452-fix.jpg
		               2 Files       1,100,745 bits

		 D:\catalogPhoto\dist\2017-05-07 [Taipei] content

		2017/05/08  下午 11:08           593,162 DSCF0178-fix-combine.jpg
		               1 Files         593,162 bits

		 D:\catalogPhoto\dist\2017-05-10 [Taipei] content

		2017/05/16  下午 08:12           488,975 DSCF0144.jpg
		               1 Files         488,975 bits

### Reffer:

null

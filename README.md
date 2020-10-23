# drawing_chat
![GIFアニメ](https://raw.githubusercontent.com/wiki/n3xem/drawing_chat/images/drawing_chat.gif)    
大学の講義の課題として、お絵描きを同期して二人でお絵描きを楽しめるアプリケーションを作りました。PythonのPySimpleGUIというライブラリを用いて作成しています。  
機能としては、  
・テキストチャット  
・お絵描き（色指定可、消しゴムあり）  
・チャット時に付与される名前の変更
・サーバー側にチャットログが流れる  
があります。  

# Requirement
* Python3.8.2

# Instllation
```bash
$ pip install PySimpleGUI
```

# Usage Server
```
$ python main.py
```

# Usage Client
(サーバーが起動しているときのみ)
```
$ python client.py
```

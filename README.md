# Mypkg2
ロボットシステム学第二回課題　ros


# 目的

　・この課題はROSを学ぶために製作したものです。

# 概要

# 動作環境

| OS  | Ubuntu20.04server  |
|---|---|
|  Hardware |   Rasberry Pi 4  |

# 用意したもの

　・Raspberry Pi 4
　・LANケーブル
  ・typeCケーブル

# 実行手順

　　<インストール手順>
  
       $ git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server.git
       
       $ source step0.bash
       
       $ source step1.bash
      



　　<動画内の実行手順>
  
  
　1.<端末1>でroscoreを起動させる。
   
       $ roscore
       
 2.<端末2>でプログラムを起動させる。
    
       $ rosrun mypkg count.py
       
 3.<端末3>でプログラムを起動させる。
    
       $ rosrun mypkg twice.py
       
 4.<端末4>でプログラムを起動させる。
    
       $ rostopic echo /twice

# 実行結果
　以下のリンクからyoutubeの動画がご視聴出来ます。

    https://youtu.be/LPz54DryZ0E

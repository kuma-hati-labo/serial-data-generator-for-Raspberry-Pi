# serial-data-generator-for-Raspberry-Pi
ラズパイで動くシリアルデータ生成プログラム  
Raspberry-Pi のシリアルポートから循環データを出力し続けます。

serial-data-generator.py &lt;speed&gt;  
　0x00-0xFF の循環データを出力

serial-data-generator-A-Z.py &lt;speed&gt;  
　0x41-0x5A ('A'-'Z') の循環データを出力

開発環境　
  Raspberry Pi B
  
  pi@raspberrypi:~/sdg $ uname -a  
  Linux raspberrypi 4.4.21+ #911 Thu Sep 15 14:17:52 BST 2016 armv6l GNU/Linux
  
  pi@raspberrypi:~/sdg $ python --version  
  Python 2.7.9

  OS への変更点はこちらを参照  
  http://qiita.com/ryugyoku/items/bf5fd10512c84a55d030

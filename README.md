# Print Landmark
各ランドマークの場所にチーム名が書き込まれたマップを出力する。

## DEMO
ランドマーク候補地は以下。

#### Erangel
![erangel_landmarks](https://user-images.githubusercontent.com/16263574/74584049-e038ca00-5008-11ea-92a2-9d25ea6bb1e2.png)

#### Miramar
![miramar_landmarks](https://user-images.githubusercontent.com/16263574/74584054-f34b9a00-5008-11ea-9a71-9bb0c846237d.png)

#### Sanhok
![sanhok_landmarks](https://user-images.githubusercontent.com/16263574/74584061-02324c80-5009-11ea-8f99-eab7e7662a29.png)

#### (Example)Erangelでチームのランドマークを出す。
![erangel_demo](https://user-images.githubusercontent.com/16263574/74584177-538f0b80-500a-11ea-9fb6-e80620f51ea7.png)
※ランドマーク被りはちょっとずらして表示（Rozhok）  
※ランドマークの情報がない場合は左下に表示（Team14）

## File/Directory
##### print_landmark.py
メインスクリプトファイル

##### landmark_coords.py
各ランドマークの座標をまとめたファイル

##### /maps
出力するマップの元画像
※[PUBG API Developer Resources](https://github.com/pubg/api-assets)より

## Installation
出力までの説明を雑に書きますが、使ってもらうということを今のところあまり考えてないです。

#### 環境とか(細かいバージョンは気にしないと思います。）
- Python3
- matplotlib
- gspread
- oauth2client
- Ubuntu 18.04(WSL)

#### keys.py
↑Googleスプレッドシートのキーとかをまとめたもの。（プライベートなものなのでリポジトリには加えてません。）  
筆者はkeys.pyに以下変数を定義して動かしてます。

- spreadsheetkey:認証用jsonファイル
- json_keyfile:読み込むGoogleスプレッドシートのキー（スプレッドシートファイル名でもいけるらしい）

※（参考）[Google スプレッドシートをpythonで操作する](https://qiita.com/Hidekazu-Karino/items/5201fce7249693357602)

#### Font
`# For Print Japanese`部分  
matplotlibは日本語出力回りがよろしくないようなので、日本語が出力できるフォントをダウンロードして指定してやる。  
筆者はTakaoフォントをダウンロードして指定してます。  
※環境によってさまざまかもしれないのでGoogleに質問するのが良いと思います。

#### Googleスプレッドシート
以下のシートを持つGoogleスプレッドシートを作成する。

##### landmark
チーム名と各マップのランドマーク/サブサンドマークをまとめたもの  
（例えば以下だとDEMOのようなマップがでます。）
![landmark_sheet](https://user-images.githubusercontent.com/16263574/74584881-f303cc80-5011-11ea-8c08-4df91fa91bac.png)

##### roster
出力するチームを書いておく  
![roster_sheet](https://user-images.githubusercontent.com/16263574/74584905-36f6d180-5012-11ea-92f6-9bd9a794be6a.png)

## Usage
`python3 print_landmark.py`

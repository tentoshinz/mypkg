# mypkg: Zeller's congruence ROS 2 package
![test](https://github.com/tentoshinz/mypkg/actions/workflows/test.yml/badge.svg)

ツェラーの公式を用いて曜日を求める ROS 2 パッケージ

## 概要
- この ROS 2 パッケージは、映画サマーウォーズの冒頭で登場するツェラーの公式を用いて曜日を求め、パブリッシュします。
- このパッケージを用いて曜日計算することで夏を感じることができます。

## ノード

### zellers
ツェラーの公式を使用して曜日を計算するノード。
サブスクライブしたデータを元に計算し、パブリッシュします。

#### サブスクライブするトピック
- date (std_msgs/UInt32)
    - ```yyyymmdd``` 形式の日付を読み込み曜日の計算をする

#### パブリッシュするトピック
- calc_week (std_msgs/Int16)
    - 計算した曜日のデータ
    - 0~6で曜日を表す
        | 日 | 月 | 火 | 水 | 木 | 金 | 土 |
        | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
        | 1 | 2 | 3 | 4 | 5 | 6 | 0 |
    - 出力例
        ```
        data: 5
        ```

- calc_week_str (std_msgs/String)
    - 計算した曜日と日時の文字列データ
    - 出力例
        ```
        data: 1978/02/16 is Thu
        ```

### pubdate
現在の日付から1日ずつ増える ```yyyymmdd``` 形式の日付を、0.5秒ずつパブリッシュする。

#### パブリッシュするトピック
- date (std_msgs/UInt32)
    - ```yyyymmdd```形式の日付
    - 出力例
        ```
        data: 20250110
        ---
        data: 20250111
        ---
        data: 20250112
        ---
        ```

### listener
テスト用


## テスト環境
- Ubuntu 22.04 LTS
- ROS 2 Humble

## 参考
[Wikipedia ツェラーの公式](https://ja.wikipedia.org/wiki/%E3%83%84%E3%82%A7%E3%83%A9%E3%83%BC%E3%81%AE%E5%85%AC%E5%BC%8F)

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 tento
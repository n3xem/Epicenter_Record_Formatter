# Epicenter_Record_Formatter
気象庁が[こちらのページ](https://www.data.jma.go.jp/svd/eqev/data/bulletin/hypo.html)で配布している震源レコードを加工してjsonにします。  
jsonのキーは非英語専攻者が調べて英訳したものなので、本来の意味とは違う可能性があります。  
レコードの各項目の詳細については、[気象庁の震源レコードフォーマットのページ](https://www.data.jma.go.jp/svd/eqev/data/bulletin/data/format/hypfmt_j.html)をご覧ください。

## Requirements
Python 3.*

## Usage
```
$ python src/record2json.py レコードファイルのパス 出力先ファイル名.json
```

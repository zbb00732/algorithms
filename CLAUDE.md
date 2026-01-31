# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

C言語からPythonへの翻訳を通じたアルゴリズム学習プロジェクト。底本は「Cで書くアルゴリズム」(疋田輝雄著)、「プログラミングの宝箱 アルゴリズムとデータ構造」(紀平拓男・春日伸弥著)。

## コマンド

```bash
# C言語のコンパイルと実行
gcc <ディレクトリ>/original.c -o <ディレクトリ>/a.out
./<ディレクトリ>/a.out

# Pythonの実行
python3 <ディレクトリ>/pythonic.py

# テスト実行（各ディレクトリ内で）
python3 -m unittest <ディレクトリ>/test.py
```

## ディレクトリ構成パターン

`00_template/` をテンプレートとして、各アルゴリズムは `XX_名前/` ディレクトリに以下の4ファイル+READMEで構成される:

| ファイル | 役割 |
|---------|------|
| `original.c` | 底本のC実装を忠実に再現（処理の改変禁止、フォーマット変更のみ可） |
| `direct.py` | Cの処理の流れをそのままPythonに直訳（極力忠実に） |
| `pythonic.py` | Pythonの流儀に従った翻訳（より良い手段があれば積極的に改変） |
| `test.py` | `pythonic.py` の関数に対するunittestテストコード |
| `README.md` | アルゴリズム概要・学習メモ・ベンチマーク結果 |

## 翻訳の3段階ルール

- **原語版** (`original.c`): 底本に忠実。処理を改変してはならない
- **直訳版** (`direct.py`): Cの流れをそのまま直訳。直訳できない部分のみ翻訳可
- **翻訳版** (`pythonic.py`): Pythonic に書く。型ヒント・docstring・`if __name__ == '__main__'`パターンを使用。テスト対象はこのファイル

## 言語設定

日本語で応対すること。コード中のコメント・docstringも日本語。

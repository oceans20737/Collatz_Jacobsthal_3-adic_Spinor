# **Jacobsthal Spinor Transfer Model from J3 to J2 Space in Collatz Inverse Trees**

**Hiroshi Harada — July 6, 2026**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Collatz逆木（Inverse Tree）の生成メカニズムを、3-adic Jacobsthal（J3）空間から 2-adic Jacobsthal（J2）空間への **スピノル転写（Spinor Transfer）** として定式化した理論モデルと、その計算・可視化ツール群です。

---

## **概要 (Overview)**

従来の Collatz 逆木生成は「3n+1」の逆算に依存していましたが、本研究では **乗算・除算を一切使わず、加算と位相（mod 3）のみ** で逆木を生成できる構造を示します。

1. **J3空間（3-adic）**  
   奇数核の局所位相（Balanced Ternary）から J3 スピノル $J_3(a,b)$ を決定。

2. **スピノル転写 (Spinor Transfer)**  
   線形写像 $J_3(a,b) \rightarrow J_2(b-a,\; b+a)$ により、J2空間の初期条件へ位相をダイレクトに転写。

3. **J2空間（2-adic）**  
   漸化式 $x_{k+2} = x_{k+1} + 2x_k$ による指数展開と、Balanced Ternary による偶奇パリティ分岐が、逆木の親ノード（$3n+1$ / $3n-1$）を幾何学的に抽出する。

---

## **ファイル構成 (Files)**

- **`code_01_spinor.py`**  
  任意の初期値から奇数核 Collatz 軌道を算出し、各ノードの J3/J2 スピノルおよび  
  J2 展開数列を計算して CSV 出力する Python スクリプト。

- **`TITLE_EN.pdf`**  
  J3 → J2 スピノル転写の概念アーキテクチャ図。

- **`REPORT_EN.pdf` / `REPORT_JP.pdf`**  
  本理論の公式リサーチレポート（英語 / 日本語）。

---

## **使い方 (Usage)**

Python 3.x 環境で以下を実行します：

```bash
python code_01_spinor.py
```

プロンプトに任意の正の整数（例：`7`）を入力すると、逆木軌道に沿ったスピノル転写の結果がコンソールに表示され、詳細データが次の形式で保存されます：

```
collatz_spinor_orbit_<初期値>.csv
```

---

## **出力例 (CSV)**

| Node(b) | Phase | a | J3(a,b) | J2(x1,x2) | J2 Sequence |
| --- | --- | --- | --- | --- | --- |
| 1 | +1 | 0 | J3(0, 1) | J2(1, 1) | [1, 1, 3, 5, 11] |
| 5 | -1 | 2 | J3(2, 5) | J2(3, 7) | [3, 7, 13, 27, 53] |
| … | … | … | … | … | … |

---

## **ライセンス (License)**

- Research documents: **CC BY 4.0**  
- Python source code: **MIT License**  
- © 2026 Hiroshi Harada

---

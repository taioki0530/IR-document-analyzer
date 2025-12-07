# IR Document Analyzer

AIを活用したIR資料自動分析システム

## 🎯 概要

PDF形式の決算短信やIR資料を読み込み、Google Colab GPUで要約を生成するシステム。
ローカル環境（WSL/Linux）とクラウドGPUを連携させたハイブリッドアーキテクチャ。

## 🛠️ 技術スタック

- **言語**: Python 3.12
- **PDF解析**: pdfplumber
- **GPU推論**: Google Colab (T4 GPU)
- **API**: FastAPI + ngrok
- **環境**: WSL2 (Ubuntu 24.04)

## 📁 プロジェクト構成
```
ir-analyzer/
├── local/              # ローカル実行コード
│   ├── pdf_parser.py   # PDF解析
│   ├── ir_analyzer.py  # 統合クライアント
│   └── test_*.py       # テストスクリプト
├── colab/              # Colab notebook用
└── samples/            # サンプルPDF（非公開）
```

## 🚀 使い方

### 1. セットアップ
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Colab GPUサーバー起動

Google Colabでサーバーコードを実行し、ngrok URLを取得

### 3. 分析実行
```bash
python local/analyze_wealthnavi.py
```

## 🎓 学習ポイント

- Linux環境構築（WSL2）
- Git/GitHubワークフロー
- Python仮想環境管理
- API設計（FastAPI）
- クラウドGPU活用
- PDF処理

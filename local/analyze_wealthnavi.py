"""
ウェルスナビ決算短信の分析
"""
from ir_analyzer import IRAnalyzer

# Colab URL
COLAB_URL = "https://unremaining-neymar-concealedly.ngrok-free.dev"

# アナライザー初期化
analyzer = IRAnalyzer(COLAB_URL)

# ウェルスナビPDFを分析（最初の3ページのみテスト）
result = analyzer.analyze_pdf(
    "samples/ウェルスナビ＿決算短信.pdf",
    pages=[1, 2, 3]
)

# レポート表示
analyzer.print_report(result)

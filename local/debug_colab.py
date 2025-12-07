"""
Colabサーバーのデバッグ
"""
import requests
from pdf_parser import extract_text_from_pdf

COLAB_URL = "https://unremaining-neymar-concealedly.ngrok-free.dev"

# PDFから1ページ目のテキスト抽出
pdf_data = extract_text_from_pdf("samples/ウェルスナビ＿決算短信.pdf")
page1_text = pdf_data['pages'][0]['text'][:500]  # 最初の500文字のみ

print("Page 1 text (first 500 chars):")
print(page1_text)
print("\n" + "="*60)

# Colabに送信
print("Sending to Colab...")
try:
    response = requests.post(
        f"{COLAB_URL}/summarize",
        json={"text": page1_text},
        timeout=30
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")

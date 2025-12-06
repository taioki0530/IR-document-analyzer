"""
PDF解析モジュール
IRレポートからテキストを抽出
"""
import pdfplumber
from pathlib import Path


def extract_text_from_pdf(pdf_path: str) -> dict:
    """
    PDFからテキストを抽出
    
    Args:
        pdf_path: PDFファイルのパス
    
    Returns:
        dict: ページごとのテキストと全体テキスト
    """
    if not Path(pdf_path).exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    
    pages_text = []
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Total pages: {len(pdf.pages)}")
        
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                pages_text.append({
                    "page": i + 1,
                    "text": text
                })
    
    full_text = "\n\n".join([p["text"] for p in pages_text])
    
    return {
        "total_pages": len(pages_text),
        "pages": pages_text,
        "full_text": full_text
    }


if __name__ == "__main__":
    # テスト用
    print("PDF Parser ready")

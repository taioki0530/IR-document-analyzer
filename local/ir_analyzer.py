"""
IR資料分析システム
PDFを読み込み、Colab GPUで要約
"""
import requests
from pdf_parser import extract_text_from_pdf
from pathlib import Path


class IRAnalyzer:
    def __init__(self, colab_url: str):
        """
        Args:
            colab_url: Colab GPUサーバーのngrok URL
        """
        self.colab_url = colab_url.rstrip('/')
        self._check_connection()
    
    def _check_connection(self):
        """Colabサーバー接続確認"""
        try:
            response = requests.get(f"{self.colab_url}/", timeout=5)
            if response.status_code == 200:
                print(f"✅ Connected to Colab GPU server")
                print(f"   GPU available: {response.json().get('gpu', False)}")
            else:
                print(f"⚠️ Server responded with status {response.status_code}")
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            raise
    
    def analyze_pdf(self, pdf_path: str, pages: list = None):
        """
        PDFを分析して要約を生成
        
        Args:
            pdf_path: PDFファイルのパス
            pages: 分析するページ番号リスト（Noneなら全ページ）
        
        Returns:
            dict: 分析結果
        """
        print(f"\n📄 Analyzing: {pdf_path}")
        
        # PDFからテキスト抽出
        print("Extracting text from PDF...")
        pdf_data = extract_text_from_pdf(pdf_path)
        
        # ページ選択
        target_pages = pdf_data['pages']
        if pages:
            target_pages = [p for p in pdf_data['pages'] if p['page'] in pages]
        
        print(f"Processing {len(target_pages)} pages...")
        
        # 各ページを要約
        results = []
        for page_data in target_pages:
            page_num = page_data['page']
            text = page_data['text']
            
            # 短すぎるページはスキップ
            if len(text) < 100:
                print(f"  Page {page_num}: Skipped (too short)")
                continue
            
            print(f"  Page {page_num}: Summarizing...", end=" ")
            
            try:
                response = requests.post(
                    f"{self.colab_url}/summarize",
                    json={"text": text},
                    timeout=30
                )
                
                if response.status_code == 200:
                    summary = response.json()['summary']
                    print("✅")
                    results.append({
                        "page": page_num,
                        "summary": summary,
                        "original_length": len(text)
                    })
                else:
                    print(f"❌ (status {response.status_code})")
            
            except Exception as e:
                print(f"❌ ({str(e)[:50]})")
        
        return {
            "pdf_path": pdf_path,
            "total_pages": pdf_data['total_pages'],
            "analyzed_pages": len(results),
            "summaries": results
        }
    
    def print_report(self, result: dict):
        """分析結果を表示"""
        print("\n" + "="*60)
        print(f"📊 IR Analysis Report")
        print("="*60)
        print(f"File: {result['pdf_path']}")
        print(f"Total pages: {result['total_pages']}")
        print(f"Analyzed pages: {result['analyzed_pages']}")
        print("-"*60)
        
        for item in result['summaries']:
            print(f"\n📄 Page {item['page']} (original: {item['original_length']} chars)")
            print(f"💡 {item['summary']}")
        
        print("\n" + "="*60)


if __name__ == "__main__":
    # 使用例
    COLAB_URL = "https://unremaining-neymar-concealedly.ngrok-free.dev"
    
    analyzer = IRAnalyzer(COLAB_URL)
    
    # テスト用のPDFパスを指定
    # pdf_path = "path/to/your/ir_report.pdf"
    # result = analyzer.analyze_pdf(pdf_path)
    # analyzer.print_report(result)
    
    print("\n✅ IR Analyzer initialized successfully!")
    print("Usage:")
    print("  analyzer = IRAnalyzer(COLAB_URL)")
    print("  result = analyzer.analyze_pdf('path/to/pdf')")
    print("  analyzer.print_report(result)")

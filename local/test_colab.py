"""
Colab GPUサーバーへの接続テスト
"""
import requests

# ColabのngrokURL（あなたのURLに書き換えてください）
COLAB_URL = "https://unremaining-neymar-concealedly.ngrok-free.dev"

def test_connection():
    """サーバー接続テスト"""
    print("Testing connection to Colab GPU server...")
    try:
        response = requests.get(f"{COLAB_URL}/")
        print(f"✅ Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_summarize():
    """要約機能テスト"""
    print("\nTesting summarization...")
    
    test_text = """
    Apple Inc. reported strong quarterly earnings today, with revenue 
    reaching $90 billion, up 8% year-over-year. The company's iPhone 
    sales drove much of this growth, while services revenue also showed 
    significant gains. CEO Tim Cook stated that the company remains 
    optimistic about future growth prospects despite global economic 
    uncertainties.
    """
    
    try:
        response = requests.post(
            f"{COLAB_URL}/summarize",
            json={"text": test_text}
        )
        print(f"✅ Status: {response.status_code}")
        result = response.json()
        print(f"\n📄 Original length: {result['original_length']} chars")
        print(f"📝 Summary length: {result['summary_length']} chars")
        print(f"\n💡 Summary:\n{result['summary']}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_connection()
    test_summarize()

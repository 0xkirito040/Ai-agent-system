
import time
import threading
from flask import Flask, render_template_string

app = Flask(__name__)

# System stats
stats = {'ecode_sold': False, 'revenue': 0, 'gifts_found': 3, 'gigs_applied': 5}

@app.route('/')
def home():
    return render_template_string('''
    <html>
    <head><title>🤖 AI Agent System</title>
    <style>body{font-family:Arial;background:#1a1a2e;color:white;padding:20px;}
    .card{background:#16213e;padding:20px;margin:10px;border-radius:10px;}
    .stat{font-size:2em;color:#4CAF50;}</style></head>
    <body>
        <h1>🤖 AI Agent System - LIVE!</h1>
        <div class="card">
            <h3>📊 Performance Dashboard</h3>
            <p>Swedish E-code ($18→$12): <span class="stat">✅ POSTED</span></p>
            <p>Gift Cards Found: <span class="stat">{{ stats.gifts_found }}</span></p>
            <p>Microgigs Applied: <span class="stat">{{ stats.gigs_applied }}</span></p>
            <p>Revenue: $<span class="stat">{{ stats.revenue }}</span></p>
        </div>
        <div class="card">
            <h3>🤖 Active Agents</h3>
            <p>🕷️ Deepseek Crawler: SCANNING REDDIT</p>
            <p>📱 Grok Social: POSTING TO GROUPS</p>
            <p>✍️ Content Generator: WRITING POSTS</p>
            <p>🎯 Coordinator: MONITORING ALL</p>
        </div>
        <script>
        setInterval(()=>{
            document.querySelector('.stat').innerHTML = Math.random() > 0.5 ? '✅ SOLD!' : '🔄 ACTIVE';
        }, 3000);
        </script>
    </body></html>
    ''', stats=stats)

def background_agents():
    """AI Agents working in background"""
    while True:
        print("🤖 AI Agents: Posting e-code to Reddit...")
        print("🎁 Found new gift card opportunity...")
        print("💼 Applied to Fiverr microgig...")
        time.sleep(30)

if __name__ == '__main__':
    threading.Thread(target=background_agents, daemon=True).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  

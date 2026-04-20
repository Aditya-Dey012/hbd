# app.py — Khushi Dinkar Happy Birthday App
# Place images as: assets/image-1.png, assets/image-2.png, etc.

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Happy Birthday Khushi! 🎂",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
}

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* Responsive page container */
.block-container {
    padding: 1.25rem 1.25rem 3rem 1.25rem !important;
    max-width: min(1100px, 92vw) !important;
    margin: auto !important;
}

/* Page 1 background */
.page-quiz-bg {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(160deg, #ffe4f0 0%, #fff0f5 50%, #fef9c3 100%);
    z-index: -1;
}

/* Quiz title */
.quiz-title {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(2rem, 4.5vw, 3rem);
    text-align: center;
    color: #c0006e;
    margin-bottom: 0.2rem;
    text-shadow: 1px 1px 6px rgba(255,105,180,0.3);
}
.quiz-subtitle {
    font-size: clamp(1.05rem, 2.1vw, 1.3rem);
    text-align: center;
    color: #7a3060;
    margin-bottom: 2rem;
    font-weight: 600;
}

/* Khushi button */
div[data-testid="stButton"] button[kind="secondary"].khushi-btn,
div.khushi-btn > div > button {
    background: linear-gradient(135deg, #ff6b9d, #ff8fab) !important;
    color: white !important;
}

/* Buttons scale well on desktop + mobile */
div[data-testid="stButton"] > button {
    width: 100% !important;
    min-height: clamp(54px, 7vw, 65px) !important;
    font-size: clamp(1rem, 2.2vw, 1.2rem) !important;
    border-radius: 18px !important;
    border: none !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700 !important;
    margin-bottom: 12px !important;
    transition: transform 0.2s ease !important;
}

/* Celebration background */
.page-celebration-bg {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(160deg, #1a0010 0%, #3d0030 40%, #1a0025 100%);
    z-index: -1;
}

/* Hero title rainbow */
@keyframes rainbow {
    0%   { color: #ff6b9d; }
    20%  { color: #ffd700; }
    40%  { color: #ff8c00; }
    60%  { color: #da70d6; }
    80%  { color: #ff69b4; }
    100% { color: #ff6b9d; }
}
.hero-title {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(2rem, 8vw, 3rem);
    text-align: center;
    animation: rainbow 3s linear infinite;
    text-shadow: 0 0 20px rgba(255,105,180,0.6), 0 0 40px rgba(255,215,0,0.3);
    line-height: 1.3;
    margin-bottom: 0.3rem;
}
.hero-sub {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(1.2rem, 2.8vw, 1.7rem);
    text-align: center;
    color: #ffd6e7;
    margin-bottom: 1.5rem;
    opacity: 0.9;
}

/* Section title */
.section-title {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(1.45rem, 3.3vw, 2.1rem);
    text-align: center;
    color: #ffd6e7;
    margin: 1.5rem 0 1rem 0;
    text-shadow: 0 0 10px rgba(255,150,180,0.5);
}

/* Image card */
.img-wrapper {
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(255,105,180,0.45);
    margin-bottom: 12px;
    transition: transform 0.3s ease;
}

/* Caption */
.img-caption {
    text-align: center;
    font-family: 'Dancing Script', cursive;
    font-size: 1.1rem;
    color: #ffb3d1;
    margin-top: -8px;
    margin-bottom: 14px;
}

/* Wish card */
.wish-card {
    background: linear-gradient(135deg, rgba(255,215,0,0.15), rgba(255,105,180,0.2));
    border: 1px solid rgba(255,150,180,0.4);
    border-radius: 24px;
    padding: 28px 22px;
    text-align: center;
    font-family: 'Dancing Script', cursive;
    font-size: clamp(1.1rem, 2.2vw, 1.5rem);
    color: #ffe4f0;
    box-shadow: 0 6px 30px rgba(255,105,180,0.25), inset 0 0 40px rgba(255,215,0,0.05);
    margin: 20px 0;
    line-height: 1.9;
}

/* Emoji tile cards */
.emoji-card {
    background: linear-gradient(135deg, rgba(255,105,180,0.15), rgba(255,215,0,0.1));
    border: 1px solid rgba(255,150,180,0.3);
    border-radius: 20px;
    padding: 18px 8px;
    text-align: center;
    color: #ffe4f0;
}
.emoji-card .big-emoji { font-size: 2.5rem; display: block; margin-bottom: 8px; }
.emoji-card .card-text { font-size: 0.85rem; font-weight: 600; color: #ffb3d1; }

/* Fine-tuned mobile overrides */
@media (max-width: 640px) {
    .block-container {
        max-width: 100% !important;
        padding: 0.9rem 0.8rem 2.4rem 0.8rem !important;
    }
    .wish-card {
        padding: 20px 16px;
        line-height: 1.75;
    }
}

/* Pulse animation on Khushi button via override */
@keyframes pulse-pink {
    0%, 100% { box-shadow: 0 0 18px rgba(255,107,157,0.5); }
    50%       { box-shadow: 0 0 40px rgba(255,107,157,0.95); }
}

/* Floating flowers overlay */
@keyframes floatUp {
    0%   { transform: translateY(100vh) rotate(0deg); opacity: 0.8; }
    100% { transform: translateY(-120px) rotate(360deg); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# ─── SESSION STATE INIT ───────────────────────────────────────────────────────
if 'page' not in st.session_state:
    st.session_state['page'] = 'quiz'
if 'show_correct_popup' not in st.session_state:
    st.session_state['show_correct_popup'] = False


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — QUIZ
# ══════════════════════════════════════════════════════════════════════════════
def show_quiz_page():
    # Floating background flowers
    st.markdown('<div class="page-quiz-bg"></div>', unsafe_allow_html=True)

    st.components.v1.html("""
    <div id="flowers-container" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;">
    </div>
    <script>
    const flowers = ['🌸','🌺','🌹','🌷','💐','✨'];
    const container = document.getElementById('flowers-container');
    function createFlower() {
        const el = document.createElement('span');
        el.textContent = flowers[Math.floor(Math.random() * flowers.length)];
        el.style.cssText = `
            position:absolute;
            font-size:${Math.random()*1.2+0.8}rem;
            left:${Math.random()*100}%;
            bottom:-30px;
            animation: floatUp ${Math.random()*6+6}s linear forwards;
            opacity:0.75;
        `;
        container.appendChild(el);
        el.addEventListener('animationend', () => el.remove());
    }
    const style = document.createElement('style');
    style.textContent = `@keyframes floatUp {
        0% { transform: translateY(0) rotate(0deg); opacity:0.8; }
        100% { transform: translateY(-110vh) rotate(360deg); opacity:0; }
    }`;
    document.head.appendChild(style);
    setInterval(createFlower, 700);
    </script>
    """, height=0)

    st.markdown('<div class="quiz-title">🌸 A Special Question 🌸</div>', unsafe_allow_html=True)
    st.markdown('<div class="quiz-subtitle">Whose birthday is on 24th April? 🎂</div>', unsafe_allow_html=True)

    # ── IMPOSSIBLE BUTTON (Aditya Dey) ──────────────────────────────────────
    st.components.v1.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      * { margin:0; padding:0; box-sizing:border-box; }
      body { background: transparent; overflow: visible; }

      #runBtn {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 18px 30px;
        font-size: 1.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ff4e00, #ff9a00);
        color: white;
        border: none;
        border-radius: 18px;
        cursor: pointer;
        font-family: 'Poppins', sans-serif;
        width: calc(100vw - 48px);
        max-width: 420px;
        min-height: 65px;
        box-shadow: 0 4px 18px rgba(255,78,0,0.4);
        animation: shake 0.6s infinite;
        z-index: 10;
        transition: left 0.12s ease, top 0.12s ease;
        touch-action: none;
      }
      @keyframes shake {
        0%,100%{ transform: translate(-50%,-50%) rotate(-1.5deg); }
        50%    { transform: translate(-50%,-50%) rotate(1.5deg); }
      }

      /* RED ALERT OVERLAY */
      #alertOverlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 0, 0, 0.8);
        z-index: 10000;
        justify-content: center;
        align-items: center;
        animation: redFlash 0.2s infinite;
      }
      #alertOverlay.show { display: flex; }

      @keyframes redFlash {
        0%, 100% { background: rgba(255, 0, 0, 0.8); }
        50% { background: rgba(255, 0, 0, 0.5); }
      }

      #alertBox {
        background: rgba(0, 0, 0, 0.95);
        border: 4px solid #ff0000;
        border-radius: 20px;
        padding: 40px 30px;
        text-align: center;
        max-width: 400px;
        width: 90%;
        box-shadow: 0 0 50px rgba(255, 0, 0, 0.8);
        animation: alertPop 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      }

      @keyframes alertPop {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
      }

      #alertBox .alert-icon {
        font-size: 4rem;
        margin-bottom: 15px;
        animation: spin 0.6s linear infinite;
      }

      @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }

      #alertBox h2 {
        color: #ff0000;
        font-size: 2rem;
        font-weight: 900;
        margin: 10px 0;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-family: monospace;
        text-shadow: 0 0 10px rgba(255, 0, 0, 0.8);
      }

      #alertBox p {
        color: #ffff00;
        font-size: 1.3rem;
        font-weight: 700;
        margin: 15px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-family: monospace;
        animation: textGlow 0.5s infinite alternate;
      }

      @keyframes textGlow {
        from { text-shadow: 0 0 5px rgba(255, 255, 0, 0.5); }
        to { text-shadow: 0 0 15px rgba(255, 255, 0, 1); }
      }

      .bar {
        display: inline-block;
        background: #ff0000;
        width: 8px;
        height: 30px;
        margin: 0 3px;
        animation: barFlash 0.3s infinite;
      }
      .bar:nth-child(1) { animation-delay: 0s; }
      .bar:nth-child(2) { animation-delay: 0.1s; }
      .bar:nth-child(3) { animation-delay: 0.2s; }

      @keyframes barFlash {
        0%, 100% { background: #ff0000; }
        50% { background: #ffff00; }
      }

      /* Mobile responsiveness */
      @media (max-width: 768px) {
        #alertBox {
          padding: 30px 20px;
          width: 95%;
          border: 3px solid #ff0000;
        }

        #alertBox .alert-icon {
          font-size: clamp(3rem, 8vw, 5rem);
          margin-bottom: 12px;
        }

        #alertBox h2 {
          font-size: clamp(1.5rem, 5vw, 2.5rem);
          margin: 8px 0;
          letter-spacing: 1px;
        }

        #alertBox p {
          font-size: clamp(1rem, 3.5vw, 1.5rem);
          margin: 12px 0;
          letter-spacing: 0.5px;
          line-height: 1.5;
        }
      }

      @media (max-width: 480px) {
        #alertBox {
          padding: 25px 15px;
          border-radius: 15px;
        }

        #alertBox .alert-icon {
          font-size: clamp(2.5rem, 10vw, 4rem);
        }

        #alertBox h2 {
          font-size: clamp(1.2rem, 6vw, 2rem);
          margin: 5px 0;
        }

        #alertBox p {
          font-size: clamp(0.9rem, 4vw, 1.3rem);
          margin: 10px 0;
        }

        .bar {
          width: 6px;
          height: 25px;
          margin: 0 2px;
        }
      }
    </style>
    </head>
    <body>

    <button id="runBtn">1️⃣ &nbsp; Aditya Dey 😈</button>

    <div id="alertOverlay">
      <div id="alertBox">
        <div class="alert-icon">⚠️</div>
        <h2>WRONG!</h2>
        <p>WRONG ANSWER<br>PLEASE CLICK OTHER</p>
        <div style="margin-top: 20px;">
          <span class="bar"></span>
          <span class="bar"></span>
          <span class="bar"></span>
        </div>
      </div>
    </div>

    <script>
      const btn = document.getElementById('runBtn');
      const alertOverlay = document.getElementById('alertOverlay');
      let escaped = 0;
      let alertActive = false;

      function playBeep() {
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.frequency.value = 800;
        oscillator.type = 'sine';
        
        gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.15);
        
        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.15);
      }

      function showAlert() {
        if (alertActive) return;
        alertActive = true;
        alertOverlay.classList.add('show');
        
        // Play beeps
        for (let i = 0; i < 5; i++) {
          setTimeout(() => playBeep(), i * 200);
        }
        
        // Auto-hide after 3 seconds
        setTimeout(() => {
          alertOverlay.classList.remove('show');
          alertActive = false;
        }, 3000);
      }

      function randomPos() {
        const bw = btn.offsetWidth || 300;
        const bh = btn.offsetHeight || 65;
        const vw = window.innerWidth;
        const vh = window.innerHeight;
        const x = Math.random() * Math.max(vw - bw - 20, 10) + 10;
        const y = Math.random() * Math.max(vh - bh - 20, 10) + 10;
        btn.style.left = x + 'px';
        btn.style.top = y + 'px';
        btn.style.transform = 'none';
      }

      // Desktop: flee on proximity
      document.addEventListener('mousemove', function(e) {
        const r = btn.getBoundingClientRect();
        const cx = r.left + r.width / 2;
        const cy = r.top + r.height / 2;
        const dx = e.clientX - cx;
        const dy = e.clientY - cy;
        if (Math.sqrt(dx * dx + dy * dy) < 130) {
          randomPos();
          escaped++;
        }
      });

      // Mobile: flee on touch
      document.addEventListener('touchstart', function(e) {
        const t = e.touches[0];
        const r = btn.getBoundingClientRect();
        const cx = r.left + r.width / 2;
        const cy = r.top + r.height / 2;
        const dx = t.clientX - cx;
        const dy = t.clientY - cy;
        if (Math.sqrt(dx * dx + dy * dy) < 160) {
          e.preventDefault();
          randomPos();
          escaped++;
        }
      }, { passive: false });

      // If somehow clicked
      btn.addEventListener('click', showAlert);
    </script>
    </body>
    </html>
    """, height=120, scrolling=False)

    # ── CORRECT BUTTON (Khushi) ──────────────────────────────────────────────
    st.markdown("""
    <style>
    /* Target second stButton */
    div[data-testid="stButton"]:last-of-type > button {
        background: linear-gradient(135deg, #ff6b9d, #ff8fab) !important;
        color: white !important;
        box-shadow: 0 0 22px rgba(255,107,157,0.55) !important;
        animation: pulse-pink 2s infinite !important;
    }
    @keyframes pulse-pink {
        0%,100% { box-shadow: 0 0 18px rgba(255,107,157,0.5); }
        50%      { box-shadow: 0 0 42px rgba(255,107,157,0.95); }
    }
    </style>
    """, unsafe_allow_html=True)

    if st.button("2️⃣   Khushi 💖", key="khushi_btn"):
        st.session_state['show_correct_popup'] = True
        st.session_state['page'] = 'celebration'
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — CELEBRATION
# ══════════════════════════════════════════════════════════════════════════════
def show_celebration_page():
    st.markdown('<div class="page-celebration-bg"></div>', unsafe_allow_html=True)

    # ── AUTO-PLAY MUSIC ──────────────────────────────────────────────────────
    music_file = Path("assets/birthday_song.mp3")
    if music_file.exists():
        st.audio(str(music_file), autoplay=True, loop=False)

    # ── CONFETTI RAIN ────────────────────────────────────────────────────────
    st.components.v1.html("""
    <!DOCTYPE html>
    <html><head>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
    </head>
    <body style="margin:0;background:transparent;">
    <canvas id="canvas" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:999;"></canvas>
    <script>
      var myConfetti = confetti.create(document.getElementById('canvas'), { resize: true, useWorker: true });
      function burst() {
        myConfetti({
          particleCount: 80,
          spread: 100,
          origin: { x: Math.random(), y: 0.1 },
          colors: ['#ff6b9d','#ffd700','#ff8fab','#da70d6','#fff','#ff4e00','#a8edea'],
          startVelocity: 35,
          gravity: 0.7,
          ticks: 200
        });
      }
      // Initial big burst
      setTimeout(() => {
        for(let i=0;i<5;i++) setTimeout(burst, i*180);
      }, 200);
      // Continuous gentle confetti
      setInterval(burst, 2200);
    </script>
    </body></html>
    """, height=0)

    # ── HERO TITLE ───────────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding-top:10px;">
      <div class="hero-title">🎂 Happy 24th Running,<br>Khushi! 💐</div>
      <div class="hero-sub">May your day be as beautiful as you are ✨🌸</div>
    </div>
    """, unsafe_allow_html=True)

    # Floating balloons
    st.components.v1.html("""
    <div id="balloons" style="position:fixed;bottom:0;left:0;width:100%;pointer-events:none;z-index:1;overflow:hidden;height:100%;"></div>
    <style>
    @keyframes riseUp {
        0%   { transform: translateY(0) rotate(-5deg); opacity:0.9; }
        50%  { transform: translateY(-50vh) rotate(5deg); opacity:0.7; }
        100% { transform: translateY(-110vh) rotate(-3deg); opacity:0; }
    }
    </style>
    <script>
    const balContainer = document.getElementById('balloons');
    const bals = ['🎈','🎀','🎊','🎁','🎉'];
    function addBalloon() {
        const el = document.createElement('span');
        el.textContent = bals[Math.floor(Math.random()*bals.length)];
        el.style.cssText = `
            position:absolute;
            font-size:${Math.random()*1.5+1.2}rem;
            left:${Math.random()*95}%;
            bottom:-40px;
            animation: riseUp ${Math.random()*5+7}s ease-in forwards;
        `;
        balContainer.appendChild(el);
        el.addEventListener('animationend', ()=>el.remove());
    }
    setInterval(addBalloon, 900);
    </script>
    """, height=0)

    # ── PHOTO GALLERY ────────────────────────────────────────────────────────
    st.markdown('<div class="section-title">📸</div>', unsafe_allow_html=True)

    assets_dir = Path("assets")
    image_files = sorted([
        f for f in assets_dir.glob("image-*.*")
        if f.is_file() and f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.webp']
    ]) if assets_dir.exists() else []

    if image_files:
        cols_per_row = 2
        for i in range(0, len(image_files), cols_per_row):
            row_imgs = image_files[i:i + cols_per_row]
            cols = st.columns(cols_per_row)
            for j, img_path in enumerate(row_imgs):
                with cols[j]:
                    st.markdown('<div class="img-wrapper">', unsafe_allow_html=True)
                    st.image(str(img_path), use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Placeholder if no images yet
        st.markdown("""
        <div style="text-align:center; padding:20px; border-radius:18px;
                    background:rgba(255,105,180,0.1); border:1px dashed rgba(255,150,180,0.4);
                    color:#ffb3d1; font-size:1rem; margin:10px 0;">
            📁 Add your photos as <b>assets/image-1.png</b>, <b>image-2.png</b>, etc.
        </div>
        """, unsafe_allow_html=True)

    # ── BIRTHDAY WISH CARD ───────────────────────────────────────────────────
    st.markdown("""
    <div class="wish-card"><br><br>
        Khushiiiiiiiiiiiii 🎃<br>
        <b>Happy Birthday, Birthday Girl! 🎂💐</b><br><br>
    </div>
    """, unsafe_allow_html=True)

    # ── EMOJI CARDS ROW ──────────────────────────────────────────────────────
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="emoji-card">
          <span class="card-text">Khushi</span>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="emoji-card">
          <span class="card-text">Rudrapratap Singh</span>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="emoji-card">
          <span class="card-text">Dinkar</span>
        </div>""", unsafe_allow_html=True)

    # ── FOOTER ───────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center; margin-top:30px; padding:20px;
                font-family:'Dancing Script',cursive; font-size:1.3rem;
                color:rgba(255,180,210,0.7);">
        Made by Aditya<br>
        <span style="font-size:2rem;">Hope this will make you smile a littleee 🤏🏼</span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# ROUTER
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state['page'] == 'quiz':
    show_quiz_page()
elif st.session_state['page'] == 'celebration':
    show_celebration_page()

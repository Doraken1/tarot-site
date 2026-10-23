const form = document.getElementById('questionForm');
const questionInput = document.getElementById('questionInput');
const questionScreen = document.getElementById('questionScreen');
const loading = document.getElementById('loading');
const resultScreen = document.getElementById('resultScreen');
const userQuestion = document.getElementById('userQuestion');
const cardsRow = document.getElementById('cards');
const readingsList = document.getElementById('readings');
const resetBtn = document.getElementById('resetBtn');

const delay = (ms) => new Promise((r) => setTimeout(r, ms));

/* ============================================================
   PARTICLE SYSTEM
   ============================================================ */
const canvas = document.getElementById('particlesCanvas');
const ctx = canvas.getContext('2d');
let particles = [];
let animationId = null;

function resizeCanvas() {
    const dpr = window.devicePixelRatio || 1;
    canvas.width = window.innerWidth * dpr;
    canvas.height = window.innerHeight * dpr;
    canvas.style.width = window.innerWidth + 'px';
    canvas.style.height = window.innerHeight + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const PARTICLE_COLORS = [
    '#e6c869', '#ffd700', '#c986e8', '#a56ee8', '#f3e9c7', '#ffffff'
];

function spawnBurst(x, y, count = 45) {
    for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = 1.5 + Math.random() * 5.5;
        particles.push({
            x, y,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed - 2,
            gravity: 0.06 + Math.random() * 0.08,
            friction: 0.985,
            life: 1,
            decay: 0.008 + Math.random() * 0.018,
            size: 1.5 + Math.random() * 3.5,
            color: PARTICLE_COLORS[Math.floor(Math.random() * PARTICLE_COLORS.length)],
            isStar: Math.random() < 0.3,
            rotation: Math.random() * Math.PI,
            rotSpeed: (Math.random() - 0.5) * 0.2,
        });
    }
    if (!animationId) animateParticles();
}

function drawStar(cx, cy, spikes, outerR, innerR, rotation) {
    let rot = rotation;
    let x = cx;
    let y = cy;
    const step = Math.PI / spikes;
    ctx.beginPath();
    ctx.moveTo(cx + Math.cos(rot) * outerR, cy + Math.sin(rot) * outerR);
    for (let i = 0; i < spikes; i++) {
        rot += step;
        x = cx + Math.cos(rot) * innerR;
        y = cy + Math.sin(rot) * innerR;
        ctx.lineTo(x, y);
        rot += step;
        x = cx + Math.cos(rot) * outerR;
        y = cy + Math.sin(rot) * outerR;
        ctx.lineTo(x, y);
    }
    ctx.closePath();
    ctx.fill();
}

function animateParticles() {
    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);

    for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.vy += p.gravity;
        p.vx *= p.friction;
        p.vy *= p.friction;
        p.rotation += p.rotSpeed;
        p.life -= p.decay;

        if (p.life <= 0 || p.y > window.innerHeight + 80) {
            particles.splice(i, 1);
            continue;
        }

        ctx.globalAlpha = Math.max(0, p.life);
        ctx.fillStyle = p.color;
        ctx.shadowBlur = 10;
        ctx.shadowColor = p.color;
        const size = p.size * p.life;

        if (p.isStar) {
            drawStar(p.x, p.y, 4, size * 1.6, size * 0.6, p.rotation);
        } else {
            ctx.beginPath();
            ctx.arc(p.x, p.y, size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;

    if (particles.length > 0) {
        animationId = requestAnimationFrame(animateParticles);
    } else {
        animationId = null;
        ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    }
}

function getElementCenter(el) {
    const rect = el.getBoundingClientRect();
    return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
}

/* ============================================================
   DOM HELPERS
   ============================================================ */
function makeCardEl(card) {
    const el = document.createElement('div');
    el.className = 'tarot-card';
    el.style.opacity = '0';
    el.style.transform = 'translateY(-30px) rotateY(90deg)';
    el.innerHTML =
        '<div class="card-header">' + card.num + '</div>' +
        '<div class="card-symbol">' + card.symbol + '</div>' +
        '<div class="card-name">' + card.name + '</div>' +
        '<div class="card-desc">' + card.description + '</div>';
    return el;
}

function makeReadingEl(reading, card) {
    const el = document.createElement('div');
    el.className = 'card-reading';
    el.style.opacity = '0';
    el.innerHTML =
        '<div class="reading-position">' + reading.position +
        ' — «' + card.name + '»</div>' +
        '<div class="reading-text">' + reading.text + '</div>';
    return el;
}

function makeOverallEl(text) {
    const el = document.createElement('div');
    el.className = 'overall';
    el.style.opacity = '0';
    el.innerHTML =
        '<h2>✨ Общий расклад</h2>' +
        '<div class="reading-text">' + text + '</div>';
    return el;
}

/* ============================================================
   REVEAL
   ============================================================ */
async function revealAll(data) {
    cardsRow.innerHTML = '';
    readingsList.innerHTML = '';
    particles = [];

    for (let i = 0; i < data.cards.length; i++) {
        const card = data.cards[i];
        const reading = data.readings[i];

        const cardEl = makeCardEl(card);
        cardsRow.appendChild(cardEl);
        await delay(20);

        const center = getElementCenter(cardEl);
        spawnBurst(center.x, center.y, 55);

        cardEl.style.transition = 'opacity 0.5s ease, transform 0.75s cubic-bezier(0.2, 0.8, 0.3, 1.2)';
        cardEl.style.opacity = '1';
        cardEl.style.transform = 'translateY(0) rotateY(0)';

        setTimeout(() => {
            const c = getElementCenter(cardEl);
            spawnBurst(c.x, c.y, 25);
        }, 380);

        await delay(750);

        const c2 = getElementCenter(cardEl);
        spawnBurst(c2.x, c2.y, 18);

        const readingEl = makeReadingEl(reading, card);
        readingsList.appendChild(readingEl);
        readingEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        await delay(20);
        readingEl.style.transition = 'opacity 0.8s ease';
        readingEl.style.opacity = '1';

        await delay(1100);
    }

    const overallEl = makeOverallEl(data.overall);
    readingsList.appendChild(overallEl);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    await delay(20);
    overallEl.style.transition = 'opacity 1s ease';
    overallEl.style.opacity = '1';

    const oc = getElementCenter(overallEl);
    setTimeout(() => {
        spawnBurst(oc.x, oc.y - 30, 90);
        setTimeout(() => spawnBurst(oc.x - 120, oc.y, 40), 180);
        setTimeout(() => spawnBurst(oc.x + 120, oc.y, 40), 360);
    }, 250);

    await delay(600);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/* ============================================================
   SUBMIT / RESET
   ============================================================ */
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const question = questionInput.value.trim();
    if (!question) {
        questionInput.focus();
        return;
    }

    questionScreen.style.display = 'none';
    resultScreen.style.display = 'none';
    loading.style.display = 'block';

    try {
        const res = await fetch('/api/reading', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || 'Ошибка сервера');

        userQuestion.textContent = '«' + question + '»';
        loading.style.display = 'none';
        resultScreen.style.display = 'block';
        window.scrollTo({ top: 0, behavior: 'smooth' });

        await revealAll(data);
    } catch (err) {
        alert('Ошибка: ' + err.message);
        loading.style.display = 'none';
        questionScreen.style.display = 'block';
    }
});

resetBtn.addEventListener('click', () => {
    resultScreen.style.display = 'none';
    questionScreen.style.display = 'block';
    cardsRow.innerHTML = '';
    readingsList.innerHTML = '';
    particles = [];
    questionInput.value = '';
    questionInput.focus();
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

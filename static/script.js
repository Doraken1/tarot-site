const form = document.getElementById('questionForm');
const questionInput = document.getElementById('questionInput');
const questionScreen = document.getElementById('questionScreen');
const loading = document.getElementById('loading');
const resultScreen = document.getElementById('resultScreen');
const userQuestion = document.getElementById('userQuestion');
const cardsGrid = document.getElementById('cardsGrid');
const readingsList = document.getElementById('readings');
const resetBtn = document.getElementById('resetBtn');

const delay = (ms) => new Promise((r) => setTimeout(r, ms));

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
    let x = cx, y = cy;
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
        p.x += p.vx; p.y += p.vy;
        p.vy += p.gravity;
        p.vx *= p.friction; p.vy *= p.friction;
        p.rotation += p.rotSpeed;
        p.life -= p.decay;
        if (p.life <= 0 || p.y > window.innerHeight + 80) {
            particles.splice(i, 1); continue;
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

function makeCardBlock(card, readingText) {
    const wrapper = document.createElement('div');
    wrapper.className = 'card-block';
    wrapper.style.opacity = '0';
    wrapper.style.transform = 'translateY(-20px)';
    
    const cardEl = document.createElement('div');
    cardEl.className = 'tarot-card';
    cardEl.innerHTML =
        '<div class="card-header">' + card.num + '</div>' +
        '<div class="card-symbol">' + card.symbol + '</div>' +
        '<div class="card-name">' + card.name + '</div>' +
        '<div class="card-desc">' + card.description + '</div>';
        
    const textEl = document.createElement('div');
    textEl.className = 'card-mini-reading';
    textEl.innerText = readingText;

    wrapper.appendChild(cardEl);
    wrapper.appendChild(textEl);
    
    return wrapper;
}

function makeOverallEl(text) {
    const el = document.createElement('div');
    el.className = 'overall';
    el.style.opacity = '0';
    el.innerHTML =
        '<h2>✨ Итоговый прогноз</h2>' +
        '<div class="reading-text">' + text + '</div>';
    return el;
}

async function revealAll(data) {
    cardsGrid.innerHTML = '';
    readingsList.innerHTML = '';
    particles = [];

    for (let i = 0; i < data.cards.length; i++) {
        const card = data.cards[i];
        const reading = data.readings[i];

        const blockEl = makeCardBlock(card, reading.text);
        cardsGrid.appendChild(blockEl);
        
        await delay(50);

        const cardVisual = blockEl.querySelector('.tarot-card');
        const center = getElementCenter(cardVisual);

        blockEl.style.transition = 'opacity 0.5s ease, transform 0.6s ease-out';
        blockEl.style.opacity = '1';
        blockEl.style.transform = 'translateY(0)';
        
        spawnBurst(center.x, center.y, 45);
        
        setTimeout(() => {
            spawnBurst(center.x, center.y, 20);
        }, 300);

        await delay(800);
    }

    const overallEl = makeOverallEl(data.overall);
    readingsList.appendChild(overallEl);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    await delay(20);
    overallEl.style.transition = 'opacity 1s ease';
    overallEl.style.opacity = '1';

    const oc = getElementCenter(overallEl);
    setTimeout(() => {
        spawnBurst(oc.x, oc.y - 30, 80);
        setTimeout(() => spawnBurst(oc.x - 120, oc.y, 40), 180);
        setTimeout(() => spawnBurst(oc.x + 120, oc.y, 40), 360);
    }, 250);

    await delay(600);
    overallEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const question = questionInput.value.trim();

    if (!question || question.length < 2 || !/[а-яА-Яa-zA-Z]/.test(question)) {
        alert('Пожалуйста, напишите ваш вопрос текстом');
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
    cardsGrid.innerHTML = '';
    readingsList.innerHTML = '';
    particles = [];
    questionInput.value = '';
    questionInput.focus();
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
